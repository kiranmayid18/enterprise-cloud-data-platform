def reconcile_counts(source_count, target_count):
    diff = source_count - target_count
    return {
        "source_count": source_count,
        "target_count": target_count,
        "difference": diff,
        "matched": diff == 0,
    }

def quality_failure_rate(total_rows, rejected_rows):
    if total_rows == 0:
        return 0.0
    return round((rejected_rows / total_rows) * 100, 2)
