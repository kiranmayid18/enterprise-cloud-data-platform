from datetime import datetime

def transform_customer(row):
    return {
        "customer_id": row["customer_id"].strip(),
        "customer_name": row["customer_name"].strip().title(),
        "country": row["country"].strip().upper(),
        "modified_date": row["modified_date"].strip(),
    }

def transform_policy(row):
    return {
        "policy_id": row["policy_id"].strip(),
        "customer_id": row["customer_id"].strip(),
        "policy_type": row["policy_type"].strip().upper(),
        "start_date": datetime.strptime(row["start_date"], "%Y-%m-%d").date().isoformat(),
        "status": row["status"].strip().upper(),
        "modified_date": row["modified_date"].strip(),
    }

def transform_claim(row):
    amount = float(row["claim_amount"])
    return {
        "claim_id": row["claim_id"].strip(),
        "policy_id": row["policy_id"].strip(),
        "claim_date": datetime.strptime(row["claim_date"], "%Y-%m-%d").date().isoformat(),
        "claim_amount": round(amount, 2),
        "claim_status": row["claim_status"].strip().upper(),
        "modified_date": row["modified_date"].strip(),
    }
