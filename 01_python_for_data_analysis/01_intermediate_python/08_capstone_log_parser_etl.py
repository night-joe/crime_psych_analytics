"""
Script 08: Capstone Mini-Project - Server Log ETL & Analytics Pipeline
Chapter: 01_intermediate_python

This capstone project synthesizes all concepts learned in Chapter 1:
- Reusable modular functions and type hints (Lesson 1)
- Lambdas, sorting, and functional tools (Lesson 2)
- Dictionary and list comprehensions (Lesson 3)
- Defensive error and exception handling (Lesson 4)
- Context-managed File I/O for Text, CSV, and JSON (Lesson 5)
- Memory-efficient streaming with generators (Lesson 6)
- Frequency analysis & group-by with Counter and defaultdict (Lesson 7)
"""

from collections import Counter, defaultdict
import json
from pathlib import Path
import re
from typing import Any, Dict, Generator, List, Optional, Tuple


# =====================================================================
# 1. Custom Exceptions
# =====================================================================
class LogFormatError(Exception):
    """Raised when a log line cannot be parsed by the ETL pattern."""
    pass


# =====================================================================
# 2. Simulated Log Generator for Testing
# =====================================================================
def create_sample_log_file(file_path: Path) -> None:
    """Generate a realistic web server access log file with clean and corrupted lines."""
    sample_lines = [
        '192.168.1.10 - - [03/Sep/2026:10:00:01] "GET /api/v1/products HTTP/1.1" 200 452 35.2',
        '10.0.0.15 - - [03/Sep/2026:10:00:03] "POST /api/v1/checkout HTTP/1.1" 201 128 145.8',
        '192.168.1.22 - - [03/Sep/2026:10:00:05] "GET /api/v1/products HTTP/1.1" 200 452 28.4',
        'MALFORMED_LINE_RECORD_CORRUPTED_WITHOUT_PARTS',
        '172.16.0.4 - - [03/Sep/2026:10:00:08] "GET /api/v1/users/profile HTTP/1.1" 401 55 12.1',
        '192.168.1.10 - - [03/Sep/2026:10:00:12] "GET /api/v1/products HTTP/1.1" 500 102 210.6',
        '10.0.0.18 - - [03/Sep/2026:10:00:15] "GET /index.html HTTP/1.1" 200 1850 15.0',
        '192.168.1.99 - - [03/Sep/2026:10:00:18] "POST /api/v1/checkout HTTP/1.1" 400 89 55.4',
        '10.0.0.15 - - [03/Sep/2026:10:00:20] "GET /api/v1/products HTTP/1.1" 200 452 32.1',
        'INVALID_IP_BAD_TIMESTAMP_ROW',
        '172.16.0.4 - - [03/Sep/2026:10:00:25] "POST /api/v1/checkout HTTP/1.1" 201 128 160.2',
    ]

    with open(file_path, "w", encoding="utf-8") as f:
        for line in sample_lines:
            f.write(line + "\n")


# =====================================================================
# 3. Defensive Parsing of Individual Log Lines
# =====================================================================
LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<endpoint>\S+) [^"]+" (?P<status>\d{3}) (?P<bytes>\d+) (?P<latency>[\d\.]+)$'
)

def parse_log_line(line: str) -> Dict[str, Any]:
    """Parse a single raw log string into structured fields with strict validation."""
    match = LOG_PATTERN.match(line.strip())
    if not match:
        raise LogFormatError(f"Line does not conform to expected web log format: '{line[:40]}...'")

    data = match.groupdict()
    return {
        "ip": data["ip"],
        "timestamp": data["timestamp"],
        "method": data["method"],
        "endpoint": data["endpoint"],
        "status": int(data["status"]),
        "bytes": int(data["bytes"]),
        "latency_ms": float(data["latency"]),
    }


# =====================================================================
# 4. Streaming Generator Pipeline
# =====================================================================
def stream_and_parse_logs(
    file_path: Path
) -> Generator[Tuple[Optional[Dict[str, Any]], Optional[str]], None, None]:
    """Stream log file line-by-line yielding (parsed_record, error_msg) pairs."""
    with open(file_path, "r", encoding="utf-8") as file:
        for line_num, line in enumerate(file, start=1):
            if not line.strip():
                continue
            try:
                record = parse_log_line(line)
                yield (record, None)
            except LogFormatError as err:
                yield (None, f"Line {line_num}: {err}")


# =====================================================================
# 5. Core Aggregation & Metrics Engine
# =====================================================================
def analyze_log_stream(file_path: Path) -> Dict[str, Any]:
    """Execute streaming aggregation across log stream and compute key KPIs."""
    status_counts: Counter = Counter()
    endpoint_counts: Counter = Counter()
    ip_counts: Counter = Counter()
    endpoint_latencies: Dict[str, List[float]] = defaultdict(list)

    total_lines = 0
    valid_records = 0
    rejected_errors: List[str] = []
    total_bytes_transferred = 0

    # Stream through records using our generator
    for record, err in stream_and_parse_logs(file_path):
        total_lines += 1
        if err:
            rejected_errors.append(err)
            continue

        valid_records += 1
        status_counts[record["status"]] += 1
        endpoint_counts[record["endpoint"]] += 1
        ip_counts[record["ip"]] += 1
        endpoint_latencies[record["endpoint"]].append(record["latency_ms"])
        total_bytes_transferred += record["bytes"]

    # Calculate average latency per endpoint using dictionary comprehension
    avg_latency_by_endpoint = {
        ep: round(sum(lats) / len(lats), 2)
        for ep, lats in endpoint_latencies.items()
    }

    # Error rate: 4xx and 5xx status codes
    client_errors = sum(c for code, c in status_counts.items() if 400 <= code < 500)
    server_errors = sum(c for code, c in status_counts.items() if 500 <= code < 600)
    error_rate_pct = round(((client_errors + server_errors) / valid_records) * 100, 2) if valid_records else 0.0

    return {
        "pipeline_kpis": {
            "total_lines_read": total_lines,
            "valid_records": valid_records,
            "corrupted_records": len(rejected_errors),
            "total_bandwidth_kb": round(total_bytes_transferred / 1024, 2),
            "error_rate_pct": error_rate_pct,
        },
        "http_status_distribution": dict(status_counts),
        "top_endpoints": endpoint_counts.most_common(3),
        "endpoint_avg_latency_ms": avg_latency_by_endpoint,
        "top_clients": ip_counts.most_common(2),
        "rejection_log": rejected_errors,
    }


def main() -> None:
    print("=" * 60)
    print("LESSON 08: CAPSTONE MINI-PROJECT (LOG ETL & ANALYTICS)")
    print("=" * 60)

    demo_dir = Path("./capstone_data")
    demo_dir.mkdir(exist_ok=True)
    raw_log_path = demo_dir / "server_access.log"
    report_path = demo_dir / "analytics_summary_report.json"

    try:
        print("\n1. Generating sample server access log...")
        create_sample_log_file(raw_log_path)
        print(f"   Created {raw_log_path.name}")

        print("\n2. Running streaming ETL & metrics calculation...")
        report = analyze_log_stream(raw_log_path)

        print("\n============================================================")
        print("                 SERVER ANALYTICS DASHBOARD                  ")
        print("============================================================")
        kpis = report["pipeline_kpis"]
        print(f"  Processed Rows:        {kpis['total_lines_read']}")
        print(f"  Valid Requests:        {kpis['valid_records']}")
        print(f"  Corrupted Logs:        {kpis['corrupted_records']}")
        print(f"  Error Rate:            {kpis['error_rate_pct']}%")
        print(f"  Data Transferred:      {kpis['total_bandwidth_kb']} KB")

        print("\n  HTTP Status Distribution:")
        for status, count in sorted(report["http_status_distribution"].items()):
            print(f"    - Status {status}: {count} requests")

        print("\n  Average Latency by Endpoint:")
        for ep, lat in sorted(report["endpoint_avg_latency_ms"].items(), key=lambda x: x[1], reverse=True):
            print(f"    - {ep:<25}: {lat:>6.2f} ms")

        print("\n  Quarantined Malformed Rows (Audited):")
        for rejection in report["rejection_log"]:
            print(f"    - [QUARANTINED] {rejection}")

        print(f"\n3. Exporting final analytical report to {report_path.name}...")
        with open(report_path, "w", encoding="utf-8") as jf:
            json.dump(report, jf, indent=2)
        print(f"   Report saved successfully.")
    finally:
        # Cleanup demo files
        if raw_log_path.exists():
            raw_log_path.unlink()
        if report_path.exists():
            report_path.unlink()
        if demo_dir.exists():
            demo_dir.rmdir()
        print("   Cleaned up temporary capstone files.")


if __name__ == "__main__":
    main()
