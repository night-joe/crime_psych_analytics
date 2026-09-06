# Chapter 3: Pandas Core Data Manipulation

## 📌 Key Topics & Subtopics
- [ ] **Data Structures**
  - pd.Series and pd.DataFrame creation and inspection
  - .head(), .tail(), .info(), .describe(), .shape
- [ ] **Data Ingestion & Export**
  - Reading CSV, Excel, Parquet, and JSON files (pd.read_csv, etc.)
  - Writing data to disk (df.to_csv(), df.to_excel())
- [ ] **Indexing, Selection & Filtering**
  - Selection via .loc[] (label-based) vs .iloc[] (position-based)
  - Multi-condition filtering ((df['col1'] > 10) & (df['col2'] == 'A'))
- [ ] **Data Cleaning Workflows**
  - Handling missing data (isna(), illna(), dropna())
  - Finding and removing duplicates (duplicated(), drop_duplicates())
  - Renaming columns, changing data types (stype()), string accessor methods (df['col'].str...)

---
## 💡 Practice Exercise Idea
Import a messy customer dataset, clean null values, convert date strings to datetime objects, fix column names, and filter active users.
