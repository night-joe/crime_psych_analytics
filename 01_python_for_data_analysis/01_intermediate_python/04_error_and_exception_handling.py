"""
Script 04: Error and Exception Handling for Data Pipelines
Chapter: 01_intermediate_python

In Data Analytics, real-world data is dirty, corrupted, and unpredictable.
Robust exception handling ensures pipelines don't crash on bad rows, records errors for auditing,
and maintains data pipeline reliability.
"""

from typing import Any, Dict, List, Optional, Tuple


# =====================================================================
# 1. Custom Domain Exceptions
# =====================================================================
class DataValidationError(Exception):
    """Raised when a data record violates business domain validation rules."""
    pass


# =====================================================================
# 2. Defensive Type Casting & Parsing
# =====================================================================
def parse_numeric_metric(raw_val: Any, metric_name: str) -> float:
    """Safely convert dirty raw values to float with descriptive error context.

    Raises:
        DataValidationError: If conversion fails or value is negative.
    """
    if raw_val is None:
        raise DataValidationError(f"Missing value for '{metric_name}'")

    try:
        if isinstance(raw_val, str):
            cleaned = raw_val.strip().replace("$", "").replace(",", "")
            numeric_val = float(cleaned)
        else:
            numeric_val = float(raw_val)
    except (ValueError, TypeError) as err:
        raise DataValidationError(
            f"Cannot parse '{metric_name}' from value '{raw_val}': {err}"
        ) from err

    if numeric_val < 0:
        raise DataValidationError(
            f"Invalid negative value {numeric_val} for '{metric_name}'"
        )

    return numeric_val


# =====================================================================
# 3. Handling ZeroDivisionError in Analytics Ratios
# =====================================================================
def compute_conversion_rate(conversions: int, impressions: int) -> float:
    """Calculate conversion rate percentage, handling zero impressions defensively."""
    try:
        rate = (conversions / impressions) * 100.0
    except ZeroDivisionError:
        # Business logic: 0 impressions equals 0.0% conversion rate
        return 0.0
    else:
        # Runs only if NO exception occurred
        return round(rate, 2)
    finally:
        # Runs unconditionally (useful for cleanup, timing, or telemetry)
        pass


# =====================================================================
# 4. Pipeline Row Ingestion with Error Auditing
# =====================================================================
def ingest_records(
    raw_records: List[Dict[str, Any]]
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Process incoming records. Separate clean rows from dirty rows with error logs.

    Returns:
        (valid_records, rejected_records_audit_log)
    """
    valid_records: List[Dict[str, Any]] = []
    rejected_audit: List[Dict[str, Any]] = []

    for row_idx, row in enumerate(raw_records, start=1):
        try:
            # 1. Check for required keys (KeyError)
            user_id = row["user_id"]
            action = row["action"]

            # 2. Parse numerical value safely (ValueError / DataValidationError)
            amount = parse_numeric_metric(row.get("amount"), "amount")

            # 3. If all validations pass, append to valid list
            valid_records.append({
                "row_number": row_idx,
                "user_id": user_id,
                "action": action,
                "amount": amount,
            })

        except KeyError as ke:
            rejected_audit.append({
                "row_number": row_idx,
                "error_type": "MissingRequiredField",
                "message": f"Missing key: {ke}",
                "raw_data": row,
            })
        except DataValidationError as dve:
            rejected_audit.append({
                "row_number": row_idx,
                "error_type": "DataValidationError",
                "message": str(dve),
                "raw_data": row,
            })
        except Exception as e:
            # Catch-all for unexpected pipeline bugs
            rejected_audit.append({
                "row_number": row_idx,
                "error_type": "UnexpectedSystemError",
                "message": str(e),
                "raw_data": row,
            })

    return valid_records, rejected_audit


def main() -> None:
    print("=" * 60)
    print("LESSON 04: ERROR AND EXCEPTION HANDLING IN DATA ANALYTICS")
    print("=" * 60)

    # 1. ZeroDivision Defensive Handling
    print("\n--- 1. Handling ZeroDivisionError Safely ---")
    print(f"  15 conv / 1,000 imp: {compute_conversion_rate(15, 1000)}%")
    print(f"  0 conv / 0 imp:       {compute_conversion_rate(0, 0)}% (handled gracefully)")

    # 2. Parsing Dirty Numerical Data
    print("\n--- 2. Parsing Dirty Currency/Numerical Metrics ---")
    test_inputs = ["$450.00", "  1,200.75 ", "-50.0", "N/A", None]
    for raw in test_inputs:
        try:
            res = parse_numeric_metric(raw, "revenue")
            print(f"  [OK]    Parsed '{raw}' -> {res}")
        except DataValidationError as ex:
            print(f"  [ERROR] Failed '{raw}' -> {ex}")

    # 3. Ingestion Pipeline Demonstration
    print("\n--- 3. Pipeline Ingestion with Rejection Logging ---")
    simulated_batch = [
        {"user_id": "U101", "action": "purchase", "amount": "$99.99"},
        {"action": "purchase", "amount": "45.00"},             # Missing user_id -> KeyError
        {"user_id": "U103", "action": "purchase", "amount": "invalid_num"}, # ValueError
        {"user_id": "U104", "action": "purchase", "amount": "-150.00"},     # Negative -> DataValidationError
        {"user_id": "U105", "action": "login", "amount": "0.0"},            # Valid
        {"user_id": "U106", "action": "purchase", "amount": "  1,500.50  "}  # Valid
    ]

    valid_rows, audit_log = ingest_records(simulated_batch)

    print(f"\n  Total Records Processed: {len(simulated_batch)}")
    print(f"  Successfully Ingested:   {len(valid_rows)}")
    print(f"  Rejected / Quarantined:  {len(audit_log)}")

    print("\n  Valid Records:")
    for r in valid_rows:
        print(f"    - User {r['user_id']}: ${r['amount']} ({r['action']})")

    print("\n  Quarantined Audit Log (For Pipeline Monitoring):")
    for log in audit_log:
        print(f"    - Row {log['row_number']} [{log['error_type']}]: {log['message']}")


if __name__ == "__main__":
    main()
