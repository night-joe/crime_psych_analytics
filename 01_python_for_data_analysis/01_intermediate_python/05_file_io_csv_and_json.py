"""
Script 05: File I/O with Text, CSV, and JSON
Chapter: 01_intermediate_python

In Data Analytics, data arrives in diverse formats. Before using Pandas, mastering Python's
built-in `open()`, `csv`, and `json` modules is critical for lightweight scripts and cloud functions.
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List


def main() -> None:
    print("=" * 60)
    print("LESSON 05: FILE I/O (TEXT, CSV, AND JSON)")
    print("=" * 60)

    # Use pathlib for clean cross-platform path handling
    temp_dir = Path("./temp_demo_files")
    temp_dir.mkdir(exist_ok=True)

    # =====================================================================
    # 1. Plain Text Files & Context Managers
    # =====================================================================
    print("\n--- 1. Plain Text I/O with Context Managers ---")
    log_file_path = temp_dir / "system_log.txt"

    sample_logs = [
        "2026-09-01 10:00:01 INFO Pipeline started",
        "2026-09-01 10:00:15 WARN High memory usage detected",
        "2026-09-01 10:00:45 INFO Ingestion completed: 4,500 records",
    ]

    # Writing text lines
    with open(log_file_path, "w", encoding="utf-8") as f:
        for log in sample_logs:
            f.write(log + "\n")
    print(f"  Written {len(sample_logs)} log lines to {log_file_path.name}")

    # Reading lines efficiently
    with open(log_file_path, "r", encoding="utf-8") as f:
        read_logs = [line.strip() for line in f]
    print(f"  Read back {len(read_logs)} lines. First line: '{read_logs[0]}'")

    # =====================================================================
    # 2. Structured CSV Files with csv.DictWriter and csv.DictReader
    # =====================================================================
    print("\n--- 2. Tabular CSV Processing (csv.DictReader / DictWriter) ---")
    csv_file_path = temp_dir / "sales_report.csv"

    sales_data = [
        {"order_id": "1001", "customer": "Alice Corp", "revenue": "1250.00", "region": "North"},
        {"order_id": "1002", "customer": "Beta LLC", "revenue": "890.50", "region": "South"},
        {"order_id": "1003", "customer": "Gamma Co", "revenue": "2400.00", "region": "East"},
        {"order_id": "1004", "customer": "Delta Inc", "revenue": "450.25", "region": "West"},
    ]

    fieldnames = ["order_id", "customer", "revenue", "region"]

    # Writing CSV with headers
    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sales_data)
    print(f"  Exported CSV dataset to {csv_file_path.name}")

    # Reading CSV as dictionaries
    total_revenue = 0.0
    with open(csv_file_path, "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        print("  Parsed Rows:")
        for row in reader:
            rev = float(row["revenue"])
            total_revenue += rev
            print(f"    - Order #{row['order_id']} | {row['customer']:<12} | ${rev:>8.2f} ({row['region']})")

    print(f"  Total Calculated Revenue: ${total_revenue:,.2f}")

    # =====================================================================
    # 3. Semi-Structured JSON Files (json.dump & json.load)
    # =====================================================================
    print("\n--- 3. Semi-Structured JSON I/O ---")
    json_file_path = temp_dir / "user_events.json"

    api_response = {
        "batch_id": "batch_98124",
        "timestamp": "2026-09-03T14:30:00Z",
        "events": [
            {"event_id": 1, "type": "click", "page": "/checkout", "session_ms": 320},
            {"event_id": 2, "type": "view", "page": "/product/42", "session_ms": 1200},
            {"event_id": 3, "type": "purchase", "page": "/order/complete", "amount": 89.99},
        ],
    }

    # Writing formatted JSON with indent
    with open(json_file_path, "w", encoding="utf-8") as jf:
        json.dump(api_response, jf, indent=2)
    print(f"  Serialized JSON payload to {json_file_path.name}")

    # Reading JSON back into native Python dictionaries/lists
    with open(json_file_path, "r", encoding="utf-8") as jf:
        loaded_json: Dict[str, Any] = json.load(jf)

    events = loaded_json.get("events", [])
    print(f"  Successfully loaded batch '{loaded_json['batch_id']}' with {len(events)} events:")
    for ev in events:
        print(f"    - Event #{ev['event_id']} ({ev['type']}) on {ev['page']}")

    # Clean up temporary demo files
    for file in [log_file_path, csv_file_path, json_file_path]:
        if file.exists():
            file.unlink()
    temp_dir.rmdir()
    print("\n  Cleaned up temporary demonstration files cleanly.")


if __name__ == "__main__":
    main()
