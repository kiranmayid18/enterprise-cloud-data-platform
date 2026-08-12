from datetime import datetime

def filter_incremental(rows, watermark_column, last_watermark):
    threshold = datetime.strptime(last_watermark, "%Y-%m-%d")
    selected = []
    for row in rows:
        value = datetime.strptime(row[watermark_column], "%Y-%m-%d")
        if value > threshold:
            selected.append(row)
    return selected
