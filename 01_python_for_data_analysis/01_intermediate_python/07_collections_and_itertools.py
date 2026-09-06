"""
Script 07: Analytics Power Tools with Collections and Itertools
Chapter: 01_intermediate_python

The Python standard library contains specialized data structures in `collections` and
combinatoric iterators in `itertools` that function as the pure-Python precursors to Pandas.
"""

from collections import Counter, defaultdict, namedtuple
import itertools
from typing import Dict, List, Tuple


def main() -> None:
    print("=" * 60)
    print("LESSON 07: COLLECTIONS & ITERTOOLS FOR ANALYTICS")
    print("=" * 60)

    # =====================================================================
    # 1. collections.Counter: Frequency Analysis & Distribution
    # =====================================================================
    print("\n--- 1. collections.Counter (Pure Python Value Counts) ---")
    page_visits = [
        "/home", "/products", "/home", "/checkout", "/products",
        "/products", "/home", "/pricing", "/products", "/checkout",
        "/home", "/products", "/blog", "/home", "/checkout"
    ]

    visit_counts = Counter(page_visits)
    print(f"  Total Visits Recorded: {len(page_visits)}")
    print(f"  Unique Pages:          {len(visit_counts)}")

    # Top 3 most visited endpoints
    print("  Top 3 Visited Pages:")
    for endpoint, count in visit_counts.most_common(3):
        pct = (count / len(page_visits)) * 100
        print(f"    - {endpoint:<12}: {count:>2} visits ({pct:.1f}%)")

    # =====================================================================
    # 2. collections.defaultdict: Group-By Operations
    # =====================================================================
    print("\n--- 2. collections.defaultdict (Group-By Aggregations) ---")
    sales_transactions = [
        {"department": "Electronics", "revenue": 450.0},
        {"department": "Home & Garden", "revenue": 120.0},
        {"department": "Electronics", "revenue": 890.0},
        {"department": "Apparel", "revenue": 65.0},
        {"department": "Home & Garden", "revenue": 210.0},
        {"department": "Electronics", "revenue": 130.0},
        {"department": "Apparel", "revenue": 195.0},
    ]

    # Group revenue amounts by department without needing 'if dept not in dict'
    dept_revenues: Dict[str, List[float]] = defaultdict(list)
    for tx in sales_transactions:
        dept_revenues[tx["department"]].append(tx["revenue"])

    print("  Department Aggregation Summaries:")
    for dept, amounts in dept_revenues.items():
        total = sum(amounts)
        avg = total / len(amounts)
        print(f"    - {dept:<15}: Count = {len(amounts)}, Total = ${total:,.2f}, Avg = ${avg:,.2f}")

    # =====================================================================
    # 3. collections.namedtuple: Lightweight Structured Records
    # =====================================================================
    print("\n--- 3. collections.namedtuple (Structured Schema) ---")
    # Defines an immutable row record with named fields and zero extra memory overhead
    CustomerRecord = namedtuple("CustomerRecord", ["cust_id", "name", "plan", "mrr"])

    customers = [
        CustomerRecord("C01", "Acme Corp", "Enterprise", 2500.0),
        CustomerRecord("C02", "StartupX", "Pro", 499.0),
        CustomerRecord("C03", "DevLab", "Starter", 99.0),
    ]

    print("  Customer Records:")
    for cust in customers:
        print(f"    - {cust.name} ({cust.plan}) pays MRR: ${cust.mrr}")

    # =====================================================================
    # 4. itertools.islice: Peeking / Sampling Streams
    # =====================================================================
    print("\n--- 4. itertools.islice (Sampling Large Streams) ---")
    # Pretend we have a large generator stream of numbers
    large_number_stream = (x ** 3 for x in range(1_000_000))

    # islice extracts only the first 5 elements without computing the rest
    preview_sample = list(itertools.islice(large_number_stream, 5))
    print(f"  First 5 cubic values sampled: {preview_sample}")

    # =====================================================================
    # 5. itertools.chain: Combining Disparate Data Streams
    # =====================================================================
    print("\n--- 5. itertools.chain (Stream Merging) ---")
    q1_regions = ["North", "South"]
    q2_regions = ["East", "West"]
    expansion_regions = ["Central", "International"]

    # itertools.chain iterates over all iterables sequentially without creating a combined list in RAM
    all_regions = list(itertools.chain(q1_regions, q2_regions, expansion_regions))
    print(f"  Consolidated Regions: {all_regions}")

    # =====================================================================
    # 6. itertools.accumulate: Cumulative Totals Over Time
    # =====================================================================
    print("\n--- 6. itertools.accumulate (Running Cumulative Sum) ---")
    monthly_sales = [12000, 15000, 14000, 18000, 22000, 25000]
    cumulative_sales = list(itertools.accumulate(monthly_sales))

    for month_idx, (month_val, running_total) in enumerate(zip(monthly_sales, cumulative_sales), 1):
        print(f"  Month {month_idx}: Monthly = ${month_val:>5} | Running Total = ${running_total:>6}")


if __name__ == "__main__":
    main()
