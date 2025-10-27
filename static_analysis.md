 Static Code Analysis Results (Before Fixes)

| Tool | Issue ID / Code | File:Line | Description | Severity | Suggestion |
|------|------------------|------------|--------------|-----------|-------------|
| **Bandit** | **B110** | inventory_system.py:19 | `try / except / pass` detected — hides potential errors | Low | Replace bare `except` with specific exception handling |
| **Bandit** | **B307** | inventory_system.py:59 | Use of `eval()` — possible code injection | Medium | Replace `eval()` with safer `ast.literal_eval()` or remove |
| **Flake8** | **F401** | inventory_system.py:2 | `'logging'` imported but unused | Low | Use `logging` or remove import |
| **Flake8** | **E302** | multiple lines | Missing 2 blank lines before function definitions | Low | Add blank lines per PEP8 |
| **Flake8** | **E722** | inventory_system.py:19 | Do not use bare `except` | Medium | Catch specific exceptions like `KeyError`, `TypeError` |
| **Pylint** | **W0102** | inventory_system.py:8 | Dangerous default value `[]` as argument | Medium | Use `logs=None` and initialize inside function |
| **Pylint** | **W0702** | inventory_system.py:19 | Bare `except` used | Medium | Catch specific exceptions instead |
| **Pylint** | **W0611** | inventory_system.py:2 | Unused import: `logging` | Low | Remove or use logging |
| **Pylint** | **W0123** | inventory_system.py:59 | Use of `eval()` detected | Medium | Replace `eval()` with safe alternative |
| **Pylint** | **C0103** | multiple | Function names not in `snake_case` | Low | Rename to `add_item`, `remove_item`, etc. |

## Summary of Key Findings
- **High priority (security):** `eval()` and `bare except` blocks.  
- **Medium priority:** Mutable default argument (`logs=[]`), missing encoding in `open()`, improper file handling.  
- **Low priority:** Style issues (naming, blank lines, unused imports).  
