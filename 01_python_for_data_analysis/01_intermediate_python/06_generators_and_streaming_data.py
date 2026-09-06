"""
Script 06: Memory-Efficient Processing with Generators and Streaming
Chapter: 01_intermediate_python

In Data Analytics, datasets often exceed available memory (RAM).
Loading millions of rows into a Python list will cause an Out-Of-Memory (OOM) crash.
Generators compute items on-demand (lazy evaluation), maintaining O(1) constant memory usage.
"""

import sys
import time
from typing import Dict, Generator, Iterator, List


# =====================================================================
# 1. Memory Profiling: List vs Generator Expression
# =====================================================================
def memory_comparison_demo() -> None:
    """Compare memory consumption between eager list comprehension and lazy generator."""
    num_items = 1_000_000  # 1 Million numbers

    print("\n--- 1. Memory Footprint: List vs Generator (1 Million Items) ---")

    # List comprehension creates the entire collection in RAM immediately
    eager_list = [x ** 2 for x in range(num_items) if x % 2 == 0]
    list_bytes = sys.getsizeof(eager_list)
    list_mb = list_bytes / (1024 * 1024)

    # Generator expression creates an iterator object that yields values on demand
    lazy_gen = (x ** 2 for x in range(num_items) if x % 2 == 0)
    gen_bytes = sys.getsizeof(lazy_gen)
    gen_kb = gen_bytes / 1024

    print(f"  List Comprehension: {list_bytes:,} bytes (~{list_mb:.2f} MB)")
    print(f"  Generator Expression: {gen_bytes:,} bytes (~{gen_kb:.2f} KB)")
    print(f"  Efficiency Advantage: Generator uses ~{list_bytes // gen_bytes:,}x less RAM!")


# =====================================================================
# 2. Generator Functions using `yield`
# =====================================================================
def stream_simulated_transactions(total_records: int) -> Generator[Dict[str, float], None, None]:
    """Simulate streaming high-volume transaction records one at a time."""
    for record_id in range(1, total_records + 1):
        # Deterministic simulation of amounts
        amount = round(10.0 + (record_id % 150) * 3.75, 2)
        yield {"id": record_id, "amount": amount}


# =====================================================================
# 3. Generator Pipeline Architecture (Streaming ETL)
# =====================================================================
# In modern data engineering, generators can be chained into modular stages:
# Extract (Stream) -> Transform (Clean/Format) -> Filter -> Aggregate

def extract_records(count: int) -> Iterator[str]:
    """Stage 1: Generate simulated raw CSV line strings."""
    for i in range(1, count + 1):
        # Simulates: id,category,raw_price
        category = "Electronics" if i % 3 == 0 else "Home" if i % 2 == 0 else "Apparel"
        price = (i * 17) % 500 + 15.5
        yield f"{i},{category},{price:.2f}"


def transform_records(lines: Iterator[str]) -> Iterator[Dict[str, float]]:
    """Stage 2: Parse raw lines into structured dictionaries."""
    for line in lines:
        parts = line.split(",")
        yield {
            "id": int(parts[0]),
            "category": parts[1],
            "price": float(parts[2]),
        }


def filter_premium_orders(records: Iterator[Dict[str, float]], min_price: float = 200.0) -> Iterator[Dict[str, float]]:
    """Stage 3: Filter records that exceed the threshold."""
    for rec in records:
        if rec["price"] >= min_price:
            yield rec


def main() -> None:
    print("=" * 60)
    print("LESSON 06: GENERATORS & STREAMING DATA")
    print("=" * 60)

    # 1. Memory comparison
    memory_comparison_demo()

    # 2. Consuming generator values on-demand
    print("\n--- 2. Manual Consumption with next() ---")
    tx_stream = stream_simulated_transactions(10)
    print(f"  First transaction:  {next(tx_stream)}")
    print(f"  Second transaction: {next(tx_stream)}")
    print("  Remaining items in loop:")
    for tx in tx_stream:
        print(f"    - Order #{tx['id']:<2} | Amount: ${tx['amount']}")

    # 3. Chained Streaming Pipeline (100,000 Records)
    print("\n--- 3. Multi-Stage Generator Pipeline (100,000 Records) ---")
    total_pipeline_records = 100_000

    start_time = time.time()

    # Chain the generator stages together without loading everything into RAM
    stage1 = extract_records(total_pipeline_records)
    stage2 = transform_records(stage1)
    stage3 = filter_premium_orders(stage2, min_price=350.0)

    # Aggregate results in a single pass (O(1) memory)
    premium_count = 0
    premium_total_value = 0.0

    for item in stage3:
        premium_count += 1
        premium_total_value += item["price"]

    elapsed = time.time() - start_time
    avg_price = premium_total_value / premium_count if premium_count else 0.0

    print(f"  Total Records Streamed:   {total_pipeline_records:,}")
    print(f"  Premium Orders Filtered:  {premium_count:,}")
    print(f"  Total Premium Value:      ${premium_total_value:,.2f}")
    print(f"  Average Premium Order:    ${avg_price:,.2f}")
    print(f"  Processing Time:          {elapsed:.4f} seconds (constant RAM consumption)")


if __name__ == "__main__":
    main()
