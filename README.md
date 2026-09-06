# Crime Psychology + Data Analytics Portfolio

> Bridging Criminal Psychology with Data Analytics — from behavioral theory to crime pattern analysis, victimology networks, and investigative dashboards.

This repository is my structured learning path for **Data Analytics + Criminal Psychology**. It contains phase-wise code, theory notes, EDA notebooks, and portfolio projects.

---

## 🎯 Goal
- Build strong foundations in Python, SQL, Statistics, and Visualization
- Apply analytics to real crime datasets (Chicago Crimes, NCRB India, Maharashtra data)
- Integrate criminal psychology theories (BSU, victimology, psychopathy, behavioral analysis)
- Create 3 portfolio-ready projects + Streamlit dashboards

## 🛠️ Tech Stack
**Analytics:** Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-Learn, NetworkX, Streamlit, Jupyter  
**Database:** SQL (SQLite, MySQL), SQLAlchemy  
**Psychology Track:** Behavioral Analysis, Criminology Theories, Victimology, Crime Typologies  
**Tools:** Git, Antigravity IDE / VS Code, GitHub

---

## 📁 Repository Structure

```
crime_psych_analytics/
├── .vscode/
│   └── settings.json
├── 01_python_for_data_analysis/
│   ├── 01_intermediate_python/        # Functions, lambda, comprehensions, ETL
│   ├── 02_numpy_basics/
│   ├── 03_pandas_core/
│   └── 04_advanced_pandas/
├── 02_sql_and_databases/
│   ├── 01_sql_foundations/
│   ├── 02_aggregations_and_joins/
│   ├── 03_advanced_sql/
│   └── 04_python_sql_integration/
├── 03_eda_and_visualization/
│   ├── 01_chart_design_principles/    # Crime EDA starter notebooks
│   ├── 02_python_plotting/
│   └── 03_bi_tools_dashboards/
├── 04_statistics_for_analytics/
│   ├── 01_descriptive_statistics/
│   ├── 02_inferential_stats_and_ab_testing/
│   └── 03_correlation_and_regression/
├── 05_portfolio_projects/
│   ├── project_1_eda_python/          # Chicago + NCRB EDA + Behavioral patterns
│   ├── project_2_sql_bi_dashboard/    # SQL analysis + BI dashboard
│   └── project_3_capstone_analytics/  # Capstone: Profiling + Dashboard + Report
├── criminal_psychology_study/         # Theory track
│   ├── 00_curriculum_overview.md
│   ├── 01_history_and_bsu_foundations.md
│   ├── 02_criminological_and_psychological_theories.md
│   ├── 03_psychopathy_and_personality_disorders.md
│   ├── 04_crime_scene_behavioral_analysis.md
│   ├── 05_victimology_and_offender_interviewing.md
│   ├── 06_violent_crime_typologies.md
│   └── 07_modern_behavioral_analysis_and_open_resources.md
├── data/                              # Local only - ignored by git (CSV, DB)
├── notebooks/                         # Optional: symlink or shortcut to EDA notebooks
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 📚 Learning Roadmap

### Phase 1: Python for Data Analysis
- **01_intermediate_python**: Functions, modules, lambda, comprehensions, matrix ops, file I/O, generators, ETL capstone log parser
- **02_numpy_basics**: Vectorization, broadcasting, slicing
- **03_pandas_core**: DataFrame creation, read_csv/excel, filtering, missing values
- **04_advanced_pandas**: groupby, merge, pivot_table, time series

### Phase 2: SQL & Databases
- **01_sql_foundations**: SELECT, WHERE, ORDER BY, LIMIT
- **02_aggregations_and_joins**: COUNT/SUM/AVG, GROUP BY, HAVING, JOINs
- **03_advanced_sql**: Subqueries, CTEs, Window Functions
- **04_python_sql_integration**: sqlite3, SQLAlchemy, pandas.read_sql

### Phase 3: EDA & Visualization
- **01_chart_design_principles**: Chart selection, UX, behavioral heatmaps
- **02_python_plotting**: Matplotlib, Seaborn, Plotly
- **03_bi_tools_dashboards**: Power BI / Tableau, DAX

### Phase 4: Statistics for Analytics
- Descriptive stats, inferential stats, A/B testing, correlation & regression

### Phase 5: Portfolio Projects
- **Project 1**: Python EDA - Chicago Crimes + NCRB (When/Where/What patterns)
- **Project 2**: SQL + BI Dashboard - District-wise trends
- **Project 3**: Capstone - Victim-Offender Network (NetworkX) + Profiling (K-Means) + Streamlit Dashboard

### Criminal Psychology Track
Parallel theory notes in `criminal_psychology_study/` — BSU history, theories, psychopathy, crime scene behavioral analysis, victimology, violent crime typologies.

---

## 🚀 Quick Start

**1. Clone & Setup Environment**
```bash
git clone https://github.com/night-joe/crime-psych-analytics.git
cd crime-psych-analytics

# Create virtual environment
python -m venv .venv

# Activate
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install
pip install --upgrade pip
pip install -r requirements.txt
```

**2. Add Data (Local Only)**
```bash
mkdir data
# Download:
# Chicago Crimes: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2
# Save as data/chicago_crimes.csv
# NCRB India: https://www.kaggle.com/datasets/rajanand/crime-in-india
# Save as data/ncrb.csv
```

**3. Run Notebooks**
```bash
# Select kernel: Python 3 (.venv) in VS Code / Antigravity
jupyter notebook
```

**4. Run Streamlit Dashboard (Phase 5)**
```bash
streamlit run 05_portfolio_projects/project_3_capstone_analytics/app.py
```

---

## ✅ Progress Tracker

- [x] Phase 0: Env setup (.venv, gitignore, GitHub)
- [ ] Phase 1: Python for Data Analysis
- [ ] Phase 2: SQL
- [ ] Phase 3: EDA + Visualization
- [ ] Phase 4: Statistics
- [ ] Phase 5: Portfolio Projects

---

## 📌 Portfolio Links (Update as you complete)

- Project 1 EDA Report: `03_eda_and_visualization/01_chart_design_principles/01_crime_eda_starter.ipynb`
- Project 2 Dashboard: Coming soon
- Project 3 Capstone: Coming soon

---

## 👤 Author
night-joe

> Note: `data/` and `.venv/` are git-ignored. This repo contains code and notes only, not raw datasets.
