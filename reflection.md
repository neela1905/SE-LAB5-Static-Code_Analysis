# Reflection — Static Code Analysis Lab

## 1. Which issues were the easiest to fix, and which were the hardest? Why?
- **Easiest:** The formatting and style-related issues from *Flake8* (like missing blank lines, unused imports, and line length). These were simple to correct by following PEP8 guidelines.
- **Hardest:** The security-related issue flagged by *Bandit* (`eval()` usage) and the mutable default argument warning from *Pylint*. These required changing the logic and understanding why the fix was safer (e.g., replacing `eval()` with safer alternatives and using `None` instead of `[]`).

---

## 2. Did the static analysis tools report any false positives? If so, describe one example.
- *Pylint* raised a warning for using the `global` statement in the `main()` function. Although technically correct, in this small program it was harmless and intentional to share state. Still, the warning encouraged me to refactor and return data explicitly, which improved design clarity.

---

## 3. How would you integrate static analysis tools into your actual software development workflow?
- I would integrate **Pylint**, **Flake8**, and **Bandit** into my **GitHub Actions CI pipeline** so that every push or pull request automatically runs static analysis.
- Locally, I would use **pre-commit hooks** to run these tools before committing code, ensuring style and security compliance early in the process.
- This setup helps maintain consistent code quality and prevents introducing security risks.

---

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- The final version of the code became **more secure** (removed `eval()` and bare `except`).
- It’s **more readable and maintainable** due to clear naming conventions and consistent spacing.
- Resource handling improved by using `with open()` context managers.
- Logging replaced prints, making the program **more professional and easier to debug**.
- Overall, the code quality improved from a Pylint score of **4.8/10** to **10/10**, reflecting real robustness gains.
