# swe-testing-assignment

## Running the Core Calculator (Logic Only)

At this stage, the project includes only the core calculation logic (`calculator.py`) without a graphical interface.

### Start Python from the project root directory

Open a terminal inside the project folder and run:
```python
from quick_calc.calculator import Calculator
calc = Calculator()
```

Example:
- `print(calc.add(5, 3))        # 8`
- `print(calc.divide(10, 2))    # 5.0`

#### Division by zero handling `calc.divide(5, 0)`
This raises: `ValueError`: Cannot divide by zero

---

## Project Execution

### Running Unit Tests & Integration Tests
This project uses **pytest** as the testing framework.

If pytest is not installed, install it first: `pip install pytest`

To run all unit tests and all integration tests, execute the following command from the project root directory: `pytest`
- All tests will be automatically discovered inside the `tests/` folder.
    - Unit tests for calculator logic
    - Integration tests verifying GUI with calculation logic interaction
    

### Running the Graphical Interface (GUI)

The calculator also includes a Tkinter-based graphical interface.

To run the GUI correctly, execute it as a Python module from the project root directory: `python -m quick_calc.gui`

#### Important:
Do NOT run `gui.py` directly (e.g., python quick_calc/gui.py), as this will cause a `ModuleNotFoundError`. The project uses a package structure, so it must be executed as a module.