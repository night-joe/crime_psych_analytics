# Chapter 1: Intermediate Python for Data Analytics

This chapter bridges basic Python programming with data-centric engineering principles. It equips you with the foundational skills needed for large-scale data manipulation before moving on to **NumPy** and **Pandas**.

---

## 📚 Curriculum & Learning Sequence

| Module | File | Core Analytics Focus |
| :--- | :--- | :--- |
| **01** | [`01_functions_and_modules.py`](01_functions_and_modules.py) | Reusable functions, type hints, default arguments, dynamic aggregators with `*args`, dataset metadata configs with `**kwargs`, and modular execution (`__name__ == "__main__"`). |
| **02** | [`02_lambda_and_functional_tools.py`](02_lambda_and_functional_tools.py) | Functional programming in data workflows: `lambda`, `map()`, `filter()`, `zip()`, `enumerate()`, multi-key sorting with `sorted()`, and cumulative reduction with `reduce()`. |
| **03** | [`03_comprehensions_and_matrix.py`](03_comprehensions_and_matrix.py) | Expressive data manipulation: list comprehensions for cleaning, conditional assignments, 2D matrix flattening, lookup maps via dictionary comprehensions, and set deduplication. |
| **04** | [`04_error_and_exception_handling.py`](04_error_and_exception_handling.py) | Defensive programming for dirty data: `try`/`except`/`else`/`finally`, handling `ValueError` on bad numbers, missing keys (`KeyError`), zero division in KPI ratios, custom `DataValidationError`, and quarantined audit logs. |
| **05** | [`05_file_io_csv_and_json.py`](05_file_io_csv_and_json.py) | Native file handling: modern `pathlib.Path`, context managers (`with open`), tabular data with `csv.DictReader`/`csv.DictWriter`, and semi-structured payloads with `json.load`/`json.dump`. |
| **06** | [`06_generators_and_streaming_data.py`](06_generators_and_streaming_data.py) | Scalable analytics: RAM profiling (`sys.getsizeof`), lazy evaluation, generator functions with `yield`, generator expressions `(...)`, and multi-stage streaming ETL pipelines. |
| **07** | [`07_collections_and_itertools.py`](07_collections_and_itertools.py) | Analytics power tools: `collections.Counter` (pure-Python value counts), `collections.defaultdict` (group-by aggregations), `namedtuple` schemas, and `itertools` (`islice`, `chain`, `accumulate`). |
| **08** | [`08_capstone_log_parser_etl.py`](08_capstone_log_parser_etl.py) | **Capstone Mini-Project**: End-to-end streaming ingestion of raw server access logs, regex parsing, defensive exception handling, metric calculations, and JSON summary dashboard export. |

---

## 🚀 How to Run the Lessons

Execute any lesson script directly with Python:

```bash
python 01_functions_and_modules.py
python 02_lambda_and_functional_tools.py
python 03_comprehensions_and_matrix.py
python 04_error_and_exception_handling.py
python 05_file_io_csv_and_json.py
python 06_generators_and_streaming_data.py
python 07_collections_and_itertools.py
python 08_capstone_log_parser_etl.py
```

---

## 🎯 Next Chapter
Once you master pure Python data transformations and memory management, proceed to **Chapter 02: NumPy Basics** for vectorized numerical computing and array operations.
