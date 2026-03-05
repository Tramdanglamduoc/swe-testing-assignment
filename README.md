# swe-testing-assignment


## Project Description

Quick-Calc is a simple desktop calculator application built with Python. It follows a layered architecture separating the calculation logic from the graphical user interface (GUI). The application supports four fundamental arithmetic operations: addition, subtraction, multiplication, and division.

The project was developed with a strong focus on software testing principles, including unit testing and integration testing, ensuring that both the core logic and the interaction between the GUI and logic layer function correctly.

## Project Structure
```
swe-testing-assignment/
│
├── quick_calc/
│   ├── __init__.py
│   ├── calculator.py      # Core calculation logic
│   └── gui.py             # Tkinter GUI layer
│
├── tests/
│   ├── test_unit.py       # Unit tests for calculator logic
│   └── test_integration.py # Integration tests (GUI ↔ logic)
│
├── README.md
├── TESTING.md
└── requirements.txt (if applicable)
```


## Setup Instructions

### 1. Clone the repository

```python
git clone https://github.com/Tramdanglamduoc/swe-testing-assignment
cd swe-testing-assignment
```

### 2. Install dependencies

This project requires Python 3.10+. - recommends Python 3.13 

Install pytest:
```python
pip install pytest
```

### 3.1. Run the Graphical Interface (GUI)

The calculator includes a Tkinter-based graphical interface.

To run the GUI correctly, execute it as a Python module from the project root directory: 
```python
python -m quick_calc.gui
```

#### Important:
Do NOT run `gui.py` directly (e.g., python quick_calc/gui.py), as this will cause a `ModuleNotFoundError`. The project uses a package structure, so it must be executed as a module.

### 3.2. Running the Core Calculator (Logic Only)

The project with the core calculation logic (`calculator.py`) only.

#### Start Python from the project root directory

Open a terminal inside the project folder and run:
```python
from quick_calc.calculator import Calculator
calc = Calculator()
```

Example:
- `print(calc.add(5, 3))        # 8`
- `print(calc.divide(10, 2))    # 5.0`

##### Division by zero handling `calc.divide(5, 0)`
This raises: `ValueError`: Cannot divide by zero

## How to Run Tests

### Running Unit Tests & Integration Tests
This project uses **pytest** as the testing framework.

If pytest is not installed, install it first: `pip install pytest`

To run all unit tests and all integration tests, execute the following command from the project root directory: `pytest`
- All tests will be automatically discovered inside the `tests/` folder.
    - Unit tests for calculator logic
    - Integration tests verifying GUI with calculation logic interaction

All tests should pass successfully.


## Testing Framework Research: Pytest vs Unittest

Python provides multiple testing frameworks, with `unittest` and `pytest` being widely used.

The built-in `unittest` framework is part of Python’s standard library and follows an object-oriented approach inspired by `Java’s JUnit`.  By subclassing `unittest`, developers can specify test cases with `unittest`. Assertions and expected behavior are written/ confirmed using `TestCase` and specific methods such as `self.assertEqual()` or `self.assertRaises()`. While `unittest` is stable, structured, and does not require external dependencies, it can become verbose and less flexible for larger test suites.

In contrast, `pytest` is a third-party framework designed to simplify testing. It allows writing tests simply in a more concise and readable syntax compared to Python's built-in `unittest` framework, making it easier for developers to write tests effectively. `Pytest` supports various test types, including unit tests, functional tests, and integration tests. `Pytest` provides powerful features such as fixtures, parameterized tests, and detailed failure output, which improve maintainability and debugging efficiency. However, `pytest` is not part of the Python standard library and must be installed separately. Certain sophisticated capabilities, such as advanced fixtures, plugins, and parameterization extensions, etc. may rely on external libraries. While these extensions significantly enhance flexibility and power, they also introduce additional dependencies that must be managed carefully.

For this project, **`pytest` was chosen** because of its simplicity, readability, and superior support for fixtures. The integration tests for the Tkinter GUI benefit from pytest’s fixture system  (for setting up test environments), which cleanly manages setup and teardown of the Tkinter root window. Overall, pytest reduces boilerplate code and improves clarity, making it a better choice for this simple application - software testing project.


## Test Coverage Overview

- Unit tests cover all four arithmetic operations.
- Edge cases include division by zero, negative numbers, decimal operations, and large numbers.
- Integration tests simulate realistic user interactions in the GUI (e.g., 5 + 3 = 8, clearing display after calculation).

---

## Author

- Full Name: Ngoc Bao Tram Tran
- University: Riga Technical University
- Email: ngoc-bao-tram.tran@edu.rtu.lv
- Course: Applied System Software (DIP392)