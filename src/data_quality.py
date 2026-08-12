from datetime import datetime

def check_required(row, required_fields):
    missing = [f for f in required_fields if not str(row.get(f, "")).strip()]
    return [f"missing required field: {f}" for f in missing]

def validate_claim(row, required_fields):
    errors = check_required(row, required_fields)

    try:
        if float(row.get("claim_amount", -1)) < 0:
            errors.append("claim_amount must be zero or greater")
    except (TypeError, ValueError):
        errors.append("claim_amount must be numeric")

    for field in ["claim_date", "modified_date"]:
        try:
            datetime.strptime(str(row.get(field, "")), "%Y-%m-%d")
        except ValueError:
            errors.append(f"{field} must use YYYY-MM-DD")
    return errors

def find_duplicates(rows, key):
    seen, duplicates = set(), set()
    for row in rows:
        value = row[key]
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates

def referential_integrity(child_rows, child_key, parent_rows, parent_key):
    parent_values = {row[parent_key] for row in parent_rows}
    return [row[child_key] for row in child_rows if row[child_key] not in parent_values]
