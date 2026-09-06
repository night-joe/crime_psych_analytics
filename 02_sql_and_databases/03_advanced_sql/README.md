# Chapter 7: Advanced SQL Analytics

## 📌 Key Topics & Subtopics
- [ ] **Subqueries & CTEs**
  - Scalar subqueries, multi-row subqueries, correlated subqueries
  - Common Table Expressions (WITH cte_name AS (...) SELECT ...)
- [ ] **Window Functions**
  - Ranking functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE()
  - Value functions: LAG(), LEAD(), FIRST_VALUE(), LAST_VALUE()
  - Aggregate Windowing: SUM(sales) OVER(PARTITION BY category ORDER BY date)
- [ ] **Conditional Logic**
  - CASE WHEN condition THEN result ELSE fallback END
- [ ] **Set Operators**
  - UNION, UNION ALL, INTERSECT, EXCEPT

---
## 💡 Practice Exercise Idea
Use a CTE and Window Functions (LAG and ROW_NUMBER) to calculate month-over-month growth rate and rank products by revenue within each product department.
