from src.data_quality import validate_claim, find_duplicates, referential_integrity

REQ = ["claim_id","policy_id","claim_date","claim_amount","claim_status","modified_date"]

def test_negative_claim_amount_rejected():
    row = {
        "claim_id":"CL1","policy_id":"P1","claim_date":"2026-08-01",
        "claim_amount":"-1","claim_status":"OPEN","modified_date":"2026-08-01"
    }
    errors = validate_claim(row, REQ)
    assert "claim_amount must be zero or greater" in errors

def test_duplicate_detection():
    rows = [{"claim_id":"CL1"},{"claim_id":"CL1"},{"claim_id":"CL2"}]
    assert find_duplicates(rows, "claim_id") == {"CL1"}

def test_referential_integrity():
    children = [{"policy_id":"P1"},{"policy_id":"P9"}]
    parents = [{"policy_id":"P1"}]
    assert referential_integrity(children, "policy_id", parents, "policy_id") == ["P9"]
