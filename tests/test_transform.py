from src.transform import transform_customer, transform_claim

def test_transform_customer():
    result = transform_customer({
        "customer_id": " C001 ",
        "customer_name": "alice smith",
        "country": "uk",
        "modified_date": "2026-08-01",
    })
    assert result["customer_name"] == "Alice Smith"
    assert result["country"] == "UK"

def test_transform_claim():
    result = transform_claim({
        "claim_id": "CL1",
        "policy_id": "P1",
        "claim_date": "2026-08-01",
        "claim_amount": "100.555",
        "claim_status": "open",
        "modified_date": "2026-08-01",
    })
    assert result["claim_amount"] == 100.56
    assert result["claim_status"] == "OPEN"
