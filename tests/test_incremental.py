from src.incremental import filter_incremental

def test_filter_incremental():
    rows = [
        {"id": "1", "modified_date": "2026-07-30"},
        {"id": "2", "modified_date": "2026-08-01"},
        {"id": "3", "modified_date": "2026-08-02"},
    ]
    result = filter_incremental(rows, "modified_date", "2026-07-31")
    assert [r["id"] for r in result] == ["2", "3"]
