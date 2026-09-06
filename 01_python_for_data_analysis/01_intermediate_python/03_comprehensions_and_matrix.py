"""
Script 03: Comprehensions and Matrix Manipulations
Chapter: 01_intermediate_python

List, dictionary, and set comprehensions are fundamental to writing Pythonic, high-performance
data transformations before transitioning to NumPy and Pandas.
"""

from typing import Dict, List, Set


def main() -> None:
    print("=" * 60)
    print("LESSON 03: COMPREHENSIONS & MATRIX MANIPULATIONS")
    print("=" * 60)

    # =====================================================================
    # 1. List Comprehensions: Data Cleaning & Normalization
    # =====================================================================
    print("\n--- 1. List Comprehensions: Cleaning Dirty Lists ---")
    raw_emails = [
        "  ALICE@Gmail.com ",
        "bob@yahoo.com",
        "  CHARLIE@OUTLOOK.COM",
        None,
        "invalid_email_no_at.com",
        "DAVID@gmail.com  ",
        "",
        "EVE@company.org ",
    ]

    # Syntax: [transform_expr for item in iterable if filter_condition]
    cleaned_emails = [
        email.strip().lower()
        for email in raw_emails
        if email and "@" in email
    ]
    print("  Cleaned Email List:")
    for email in cleaned_emails:
        print(f"    - {email}")

    # Extract domain names
    domains = [email.split("@")[1] for email in cleaned_emails]
    print(f"  Extracted Domains: {domains}")

    # =====================================================================
    # 2. Conditional Transformations (if-else inside comprehension)
    # =====================================================================
    print("\n--- 2. Conditional Values (Ternary Expression) ---")
    # Syntax: [val_if_true if condition else val_if_false for item in iterable]
    raw_scores = [85, 42, 91, 58, 76, 33, 99]
    grade_bands = [
        "Pass" if score >= 60 else "Review Needed"
        for score in raw_scores
    ]
    for score, band in zip(raw_scores, grade_bands):
        print(f"  Score: {score:<3} -> Status: {band}")

    # =====================================================================
    # 3. 2D Matrix Flattening with Nested Comprehensions
    # =====================================================================
    print("\n--- 3. Nested Comprehensions: Flattening 2D Matrices ---")
    # Matrix: Rows = Sales Regions (North, South, East, West), Cols = Q1-Q4 (in $k)
    regional_sales_matrix = [
        [120, 135, 150, 160],  # North
        [90, 110, 95, 105],    # South
        [200, 210, 220, 240],  # East
        [80, 85, 75, 90],      # West
    ]

    # Flatten 2D matrix into a 1D list:
    # Notice the loop order: outer loop first, inner loop second
    flattened_sales = [
        quarter_rev
        for region in regional_sales_matrix
        for quarter_rev in region
    ]
    print(f"  Total Quarters Processed: {len(flattened_sales)}")
    print(f"  All Quarterly Revenues:   {flattened_sales}")

    # Filter only high-performing quarters (> $150k) across all regions
    high_quarters = [
        rev
        for region in regional_sales_matrix
        for rev in region
        if rev > 150
    ]
    print(f"  High-Performing Quarters (> $150k): {high_quarters}")

    # =====================================================================
    # 4. Dictionary Comprehensions: Lookup Tables & Inverted Indices
    # =====================================================================
    print("\n--- 4. Dictionary Comprehensions ---")
    # Syntax: {key_expr: value_expr for item in iterable if condition}
    employees = [
        {"id": "E101", "name": "Alice", "dept": "Engineering", "salary": 115000},
        {"id": "E102", "name": "Bob", "dept": "Marketing", "salary": 78000},
        {"id": "E103", "name": "Charlie", "dept": "Engineering", "salary": 125000},
        {"id": "E104", "name": "Diana", "dept": "Product", "salary": 105000},
    ]

    # Create an O(1) direct lookup map: employee_id -> employee_record
    employee_lookup = {emp["id"]: emp for emp in employees}
    print(f"  Employee Lookup for 'E103': {employee_lookup['E103']['name']} ({employee_lookup['E103']['dept']})")

    # Map employee name -> annualized bonus (10%)
    bonuses = {emp["name"]: round(emp["salary"] * 0.10, 2) for emp in employees}
    print("  Calculated 10% Bonuses:")
    for name, bonus in bonuses.items():
        print(f"    - {name:<8}: ${bonus:,.2f}")

    # Invert a mapping: Currency Code -> Currency Name -> Inverted Name -> Code
    currencies = {"USD": "US Dollar", "EUR": "Euro", "GBP": "British Pound", "JPY": "Japanese Yen"}
    name_to_code = {name: code for code, name in currencies.items()}
    print(f"  Inverted Lookup ('Euro'): {name_to_code.get('Euro')}")

    # =====================================================================
    # 5. Set Comprehensions: Deduplication & Category Harvesting
    # =====================================================================
    print("\n--- 5. Set Comprehensions for Deduplication ---")
    # Syntax: {expr for item in iterable if condition}
    raw_tags = [
        "python", "PYTHON ", "sql", " data science", "SQL",
        "machine learning", "Python", "sql", "data science"
    ]
    distinct_tags: Set[str] = {tag.strip().lower() for tag in raw_tags if tag}
    print(f"  Raw Tag Count:      {len(raw_tags)}")
    print(f"  Distinct Tags:      {sorted(distinct_tags)}")


if __name__ == "__main__":
    main()
