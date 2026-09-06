"""
Script 01: Functions and Modules for Data Analytics
Chapter: 01_intermediate_python

In Data Analytics, reusable and modular functions are essential for building
maintainable data pipelines, standardizing metric calculations, and avoiding code duplication.
"""

from typing import Any, Dict, List, Optional, Tuple


# =====================================================================
# 1. Clean Function Design & Type Hinting
# =====================================================================
def clean_currency_string(value: Optional[str], default: float = 0.0) -> float:
    """Clean a raw currency string and convert it to a float.

    Args:
        value: Raw currency string (e.g., " $1,250.50 ").
        default: Fallback numeric value if input is missing or empty.

    Returns:
        Cleaned float value.
    """
    if not value or not isinstance(value, str):
        return default

    # Strip whitespace, dollar signs, and commas
    cleaned = value.strip().replace("$", "").replace(",", "")
    try:
        return float(cleaned)
    except ValueError:
        return default


# =====================================================================
# 2. Positional vs Keyword Arguments & Default Values
# =====================================================================
def compute_net_revenue(
    gross_sales: float,
    discount_pct: float = 0.0,
    tax_rate: float = 0.08,
) -> float:
    """Calculate net revenue after applying discounts and taxes.

    Args:
        gross_sales: Total gross sales amount before deductions.
        discount_pct: Percentage discount (0.0 to 1.0).
        tax_rate: Tax rate to apply to discounted sales (default 8%).

    Returns:
        Net revenue rounded to two decimal places.
    """
    discounted = gross_sales * (1.0 - discount_pct)
    net = discounted * (1.0 + tax_rate)
    return round(net, 2)


# =====================================================================
# 3. Arbitrary Arguments: *args for Dynamic Metric Aggregation
# =====================================================================
def calculate_summary_stats(*values: float) -> Dict[str, float]:
    """Calculate summary statistics (count, sum, mean, min, max) for arbitrary values.

    Args:
        *values: Variable number of numeric values.

    Returns:
        Dictionary containing metric summaries.
    """
    valid_nums = [v for v in values if v is not None and isinstance(v, (int, float))]
    if not valid_nums:
        return {"count": 0, "sum": 0.0, "mean": 0.0, "min": 0.0, "max": 0.0}

    total = sum(valid_nums)
    count = len(valid_nums)
    return {
        "count": count,
        "sum": round(total, 2),
        "mean": round(total / count, 2),
        "min": round(min(valid_nums), 2),
        "max": round(max(valid_nums), 2),
    }


# =====================================================================
# 4. Arbitrary Keyword Arguments: **kwargs for Metadata & Configs
# =====================================================================
def build_dataset_metadata(dataset_name: str, **metadata: Any) -> Dict[str, Any]:
    """Package dataset metadata and configuration attributes into a structured dictionary.

    Args:
        dataset_name: Name or identifier of the dataset.
        **metadata: Arbitrary metadata fields (e.g., author, rows, version).

    Returns:
        Consolidated dictionary with standard and extra attributes.
    """
    payload: Dict[str, Any] = {
        "dataset_name": dataset_name,
        "total_attributes": len(metadata),
        "attributes": metadata,
    }
    return payload


# =====================================================================
# 5. Modular Execution Pattern
# =====================================================================
def main() -> None:
    """Run interactive demonstrations of function designs."""
    print("=" * 60)
    print("LESSON 01: FUNCTIONS & MODULES FOR DATA ANALYTICS")
    print("=" * 60)

    # 1. Cleaning currency demonstration
    raw_samples = [" $1,250.00 ", "$49.99", None, "invalid", "100.5"]
    cleaned_samples = [clean_currency_string(val) for val in raw_samples]
    print("\n--- 1. Currency Cleaning with Default Fallbacks ---")
    for raw, clean in zip(raw_samples, cleaned_samples):
        print(f"  Raw: {str(raw):<15} -> Cleaned Float: {clean}")

    # 2. Revenue calculation with keyword arguments
    print("\n--- 2. Revenue Calculation (Default & Custom Args) ---")
    base_rev = compute_net_revenue(1000.0)
    discounted_rev = compute_net_revenue(1000.0, discount_pct=0.15, tax_rate=0.05)
    print(f"  Gross $1000 with defaults:             ${base_rev}")
    print(f"  Gross $1000 (15% disc, 5% tax):        ${discounted_rev}")

    # 3. Dynamic metric aggregation with *args
    print("\n--- 3. Metric Aggregator with *args ---")
    stats = calculate_summary_stats(120.5, 450.0, None, 85.0, 920.25, 310.0)
    for metric, val in stats.items():
        print(f"  {metric:<8}: {val}")

    # 4. Dataset metadata packaging with **kwargs
    print("\n--- 4. Metadata Configuration with **kwargs ---")
    meta = build_dataset_metadata(
        "customer_churn_q3",
        source="Snowflake_DW",
        rows=154200,
        author="Analytics Team",
        validated=True,
    )
    print("  Metadata Payload:")
    for k, v in meta["attributes"].items():
        print(f"    - {k}: {v}")


if __name__ == "__main__":
    main()
