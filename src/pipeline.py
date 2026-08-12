import csv
from src.config import BASE_DIR, load_config
from src.data_quality import validate_claim, find_duplicates, referential_integrity
from src.incremental import filter_incremental
from src.reconcile import quality_failure_rate, reconcile_counts
from src.transform import transform_customer, transform_policy, transform_claim

DATA_DIR = BASE_DIR / "sample_data"
OUTPUT_DIR = BASE_DIR / "output"

def read_csv(name):
    with (DATA_DIR / name).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def write_csv(name, rows):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with (OUTPUT_DIR / name).open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

def run_pipeline(last_watermark="2026-07-31"):
    config = load_config()
    customers = read_csv("customers.csv")
    policies = read_csv("policies.csv")
    claims = read_csv("claims.csv")

    inc_customers = filter_incremental(customers, config["watermark_column"], last_watermark)
    inc_policies = filter_incremental(policies, config["watermark_column"], last_watermark)
    inc_claims = filter_incremental(claims, config["watermark_column"], last_watermark)

    customers_t = [transform_customer(r) for r in inc_customers]
    policies_t = [transform_policy(r) for r in inc_policies]

    valid_claims, rejected_claims = [], []
    for row in inc_claims:
        errors = validate_claim(row, config["required_claim_fields"])
        if errors:
            rejected_claims.append({**row, "validation_errors": " | ".join(errors)})
        else:
            valid_claims.append(transform_claim(row))

    duplicate_claims = find_duplicates(valid_claims, "claim_id")
    orphan_customer_ids = referential_integrity(
        policies_t, "customer_id", customers_t, "customer_id"
    )

    write_csv("customers_curated.csv", customers_t)
    write_csv("policies_curated.csv", policies_t)
    write_csv("claims_curated.csv", valid_claims)
    write_csv("claims_rejected.csv", rejected_claims)

    result = {
        "customers_processed": len(customers_t),
        "policies_processed": len(policies_t),
        "claims_processed": len(valid_claims),
        "claims_rejected": len(rejected_claims),
        "duplicate_claim_ids": sorted(duplicate_claims),
        "orphan_customer_ids": sorted(set(orphan_customer_ids)),
        "reconciliation": reconcile_counts(len(inc_claims), len(valid_claims) + len(rejected_claims)),
        "quality_failure_rate_percent": quality_failure_rate(len(inc_claims), len(rejected_claims)),
    }
    print(result)
    return result

if __name__ == "__main__":
    run_pipeline()
