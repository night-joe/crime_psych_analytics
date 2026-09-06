# Chapter 8: Interfacing Python with SQL

## 📌 Key Topics & Subtopics
- [ ] **Database Connectors**
  - SQLite native driver (sqlite3)
  - PostgreSQL / MySQL drivers (psycopg2, pymysql)
  - SQLAlchemy engine configuration
- [ ] **Pandas SQL Integration**
  - pd.read_sql_query(query, connection)
  - pd.read_sql_table(table_name, engine)
  - Exporting DataFrames to SQL tables (df.to_sql())
- [ ] **Parametrized Queries**
  - Preventing SQL injection using parameterized query arguments

---
## 💡 Practice Exercise Idea
Create a local SQLite database using Python, insert synthetic sales records, query summary statistics into a Pandas DataFrame, and output the transformed summary back into a new SQL database table.
