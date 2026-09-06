# Chapter 4: Advanced Pandas Workflows

## 📌 Key Topics & Subtopics
- [ ] **Groupby & Aggregations**
  - Single & multi-column grouping (df.groupby(['region', 'category']))
  - Applying multiple aggregations (.agg({'sales': ['sum', 'mean'], 'order_id': 'count'}))
  - Transform and Filter methods (.transform(), .filter())
- [ ] **Merging, Joining & Concatenating**
  - Database-style joins (pd.merge(df1, df2, on='id', how='left/inner/outer'))
  - Stacking and concatenating DataFrames (pd.concat([df1, df2]))
- [ ] **Reshaping & Pivot Tables**
  - pd.pivot_table(), .pivot(), .melt(), .stack(), .unstack()
- [ ] **Time Series Analysis**
  - Datetime indexing (pd.to_datetime())
  - Extracting year, month, day, day of week
  - Resampling time series data (.resample('M').sum()), rolling window metrics (.rolling(window=7).mean())

---
## 💡 Practice Exercise Idea
Take transactional sales data, perform a monthly rolling 30-day sum per product category, pivot the results into a wide format table, and analyze seasonal spikes.
