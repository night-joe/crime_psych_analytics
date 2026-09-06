"""
Script 02: Lambda Functions and Functional Tools
Chapter: 01_intermediate_python

In Data Analytics, functional programming tools (lambda, map, filter, zip, enumerate, sorted)
allow you to perform expressive, inline data manipulations without writing verbose boilerplate loops.
"""

from functools import reduce
from typing import Any, Dict, List, Tuple


def main() -> None:
    print("=" * 60)
    print("LESSON 02: LAMBDA FUNCTIONS & FUNCTIONAL TOOLS")
    print("=" * 60)

    # =====================================================================
    # 1. Lambda Functions (Anonymous Functions)
    # =====================================================================
    # Syntax: lambda arguments: expression
    # Used for lightweight operations where defining a named function is overkill.
    print("\n--- 1. Lambda Functions ---")
    celsius_to_fahrenheit = lambda c: round((c * 9 / 5) + 32, 2)
    normalize_pct = lambda val, max_val: round((val / max_val) * 100, 1)

    print(f"  37.5°C to Fahrenheit: {celsius_to_fahrenheit(37.5)}°F")
    print(f"  Sales score (450 out of 500): {normalize_pct(450, 500)}%")

    # =====================================================================
    # 2. map() - Transforming Data Streams
    # =====================================================================
    # map(func, iterable) applies func to every item in the iterable lazily
    print("\n--- 2. map() for Feature Transformation ---")
    raw_prices = [19.99, 45.00, 120.50, 9.99, 85.00]
    tax_rate = 0.08

    # Apply 8% tax to all prices
    taxed_prices = list(map(lambda p: round(p * (1 + tax_rate), 2), raw_prices))
    print(f"  Raw Prices:   {raw_prices}")
    print(f"  Taxed Prices: {taxed_prices}")

    # Standardize country codes
    raw_countries = ["  us ", "Uk", " Germany  ", "FRANCE", "jp "]
    clean_countries = list(map(lambda c: c.strip().upper(), raw_countries))
    print(f"  Clean Countries: {clean_countries}")

    # =====================================================================
    # 3. filter() - Eliminating Noise and Outliers
    # =====================================================================
    # filter(predicate, iterable) keeps items where predicate(item) is True
    print("\n--- 3. filter() for Record Filtering ---")
    transactions = [
        {"id": 101, "amount": 250.0, "status": "completed"},
        {"id": 102, "amount": -15.0, "status": "refunded"},
        {"id": 103, "amount": 0.0, "status": "cancelled"},
        {"id": 104, "amount": 1450.0, "status": "completed"},
        {"id": 105, "amount": 89.99, "status": "pending"},
        {"id": 106, "amount": 520.0, "status": "completed"},
    ]

    # Filter: Keep only high-value completed transactions (> $200)
    high_value_completed = list(
        filter(
            lambda t: t["status"] == "completed" and t["amount"] > 200.0,
            transactions,
        )
    )
    print("  High-Value Completed Transactions:")
    for t in high_value_completed:
        print(f"    - Order #{t['id']}: ${t['amount']}")

    # =====================================================================
    # 4. zip() - Merging Parallel Feature Lists
    # =====================================================================
    # In raw ETL, columns often come as independent lists. zip combines them into records.
    print("\n--- 4. zip() for Combining Parallel Series ---")
    dates = ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"]
    products = ["Laptop", "Monitor", "Keyboard", "Desk Chair"]
    units_sold = [12, 28, 45, 14]
    unit_prices = [999.00, 249.99, 59.99, 189.50]

    # Combine into structured transaction summaries
    daily_sales: List[Dict[str, Any]] = [
        {
            "date": d,
            "product": p,
            "revenue": round(units * price, 2),
        }
        for d, p, units, price in zip(dates, products, units_sold, unit_prices)
    ]
    for row in daily_sales:
        print(f"  [{row['date']}] {row['product']:<12}: ${row['revenue']}")

    # =====================================================================
    # 5. enumerate() - Tracking Line / Row Indices for Data Quality
    # =====================================================================
    print("\n--- 5. enumerate() for Index Tracking & Anomaly Detection ---")
    incoming_records = [45.2, 88.0, None, 12.5, -999.0, 63.4]

    for idx, val in enumerate(incoming_records, start=1):
        if val is None or val < 0:
            print(f"  [WARN] Row {idx}: Invalid or anomaly reading detected -> {val}")

    # =====================================================================
    # 6. sorted() with Custom Lambda Keys
    # =====================================================================
    print("\n--- 6. Custom Multi-Criteria Sorting ---")
    customers = [
        {"name": "Alice", "tier": "Gold", "spend": 4500},
        {"name": "Bob", "tier": "Bronze", "spend": 320},
        {"name": "Charlie", "tier": "Silver", "spend": 1850},
        {"name": "David", "tier": "Gold", "spend": 8200},
        {"name": "Eve", "tier": "Silver", "spend": 2400},
    ]

    # Sort descending by customer spend
    top_spenders = sorted(customers, key=lambda c: c["spend"], reverse=True)
    print("  Top Customers by Spend:")
    for c in top_spenders:
        print(f"    - {c['name']:<10} ({c['tier']}): ${c['spend']}")

    # Multi-criteria sorting: Sort by tier priority, then spend descending
    tier_priority = {"Gold": 1, "Silver": 2, "Bronze": 3}
    sorted_by_tier_and_spend = sorted(
        customers,
        key=lambda c: (tier_priority[c["tier"]], -c["spend"]),
    )
    print("\n  Customers Sorted by Tier Hierarchy & Highest Spend First:")
    for c in sorted_by_tier_and_spend:
        print(f"    - Tier: {c['tier']:<7} | Name: {c['name']:<8} | ${c['spend']}")

    # =====================================================================
    # 7. reduce() - Cumulative Aggregation
    # =====================================================================
    print("\n--- 7. functools.reduce() for Cumulative Reductions ---")
    monthly_growth_multipliers = [1.05, 0.98, 1.12, 1.04, 1.07]
    compounded_growth = reduce(lambda acc, val: acc * val, monthly_growth_multipliers, 1.0)
    print(f"  Monthly Multipliers: {monthly_growth_multipliers}")
    print(f"  Cumulative Compound Growth: {round((compounded_growth - 1) * 100, 2)}%")


if __name__ == "__main__":
    main()
