# swe-testing-assignment

## Running the Core Calculator (Logic Only)
At this stage, the project includes only the core calculation logic (`calculator.py`) without a graphical interface.

### 1. Start Python from the project root directory
Open a terminal inside the project folder and run:
```python
from quick_calc.calculator import Calculator
calc = Calculator()
```

Example:
- `print(calc.add(5, 3))        # 8`
- `print(calc.divide(10, 2))    # 5.0`

**Division by zero handling `calc.divide(5, 0)`**
This raises: `ValueError`: Cannot divide by zero