# Python Calculator - Unit Testing & Code Coverage Guide

## 📌 Overview
This repository contains a **Python calculator module** with basic arithmetic functions and **unit tests using `pytest`**. The guide provides installation steps, commands for running tests, and best practices followed in the industry.

---

## ⚙️ Installation Guide

1. **Clone the Repository**  
   ```sh
   git clone https://github.com/your-repo/calculator.git
   cd calculator
2. **Install Dependencies**     
    ```
    pip install -r requirements.txt
    
3. **Verify Installation**     
    ```
    python --version
    pytest --version OR python -m pytest --version

# 🛠 Running Tests with Pytest

## ✅ Run All Tests
```sh
python -m pytest 
```

## ✅ Run a Specific Test File
```sh
python -m pytest test_calculator.py
```

## ✅ Run a Specific Test Function
```sh
python -m pytest -k "test_add"
```

## ✅ Run Tests with Detailed Output
```sh
python -m pytest -v
```

## ✅ Run Tests with Code Coverage
```sh
python -m pytest --cov=calculator test_calculator.py
```

## ✅ Generate an HTML Coverage Report
```sh
python -m pytest --cov=calculator --cov-report=html
```
After running this command, open `htmlcov/index.html` in your browser.

---

# 🏆 Best Practices Followed

## 🔹 Code Best Practices
- Follows **PEP 8** coding standards.
- Includes **type hints** for better readability.
- Uses **logging** for debugging and error tracking.

## 🔹 Testing Best Practices
- Uses **pytest** for structured and scalable unit testing.
- Uses **`pytest.mark.parametrize`** to reduce redundancy.
- Covers **all possible edge cases** (zero, negatives, large numbers).
- Includes **exception handling tests** (e.g., division by zero).
