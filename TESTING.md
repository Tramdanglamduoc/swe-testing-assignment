# Testing Strategy for Quick-Calc

## 1. Testing Strategy

The testing strategy for the Quick-Calc project focuses on verifying the correctness of the calculator logic and ensuring that the graphical user interface interacts properly with the calculation layer.

Two main categories of tests were implemented:

**Unit Tests - 12 tests**
Unit tests focus on testing the core calculation logic implemented in `calculator.py`. Each arithmetic operation (addition, subtraction, multiplication, and division) is tested independently to verify that the methods return the correct results. Edge cases such as division by zero are also tested to ensure the program handles errors correctly.

**Integration Tests - 4 tests**
Integration tests verify that the user interface interacts correctly with the calculation logic. These tests simulate user actions such as pressing calculator buttons and confirm that the display shows the correct results. For example, entering `5 + 3 =` should display `8`, and pressing `C` after a calculation should reset the display to `0`.

The test suite is designed to be executable with a single command (`pytest`) so it can be run repeatedly during development to detect regressions early.

The graphical layout itself was not tested because UI appearance is not critical to the core functionality and would require more complex GUI testing tools.


## Overall Approach

Testing is organized into two layers: unit tests for the `Calculator` logic and integration tests for the Tkinter GUI flow. Unit tests form the majority to validate arithmetic correctness and edge cases, while integration tests simulate real button-press sequences to confirm that the GUI correctly calls the logic layer and updates the display. All tests run with a single command: `pytest`.

---

## 2. Lecture Concepts

### Testing Pyramid

The test suite follows the **Testing Pyramid principle**, where the majority of tests are unit tests (12 tests) and a smaller number are integration tests (4 tests). Unit tests are faster, simpler, and isolate the calculation logic, while integration tests verify that different components of the system work together correctly. This structure ensures efficient testing while maintaining good coverage.

The base of pyramid should consists of mostly unit tests, followed by integration tests.

### Black-box vs White-box Testing

Both **white-box** and **black-box** testing approaches were used.

Unit tests represent **white-box testing** because they directly test internal methods of the `Calculator` class and are written with knowledge of the implementation.

Integration tests represent **black-box testing** because they simulate user interactions without relying on internal implementation details. The tests interact with the application through button presses and verify the displayed results.

### Functional vs Non-Functional Testing

The implemented tests focus on **functional testing**, verifying that the calculator performs the correct arithmetic operations and handles invalid inputs such as division by zero.

Non-functional aspects such as performance, usability, and graphical design were not tested because they are outside the scope of this assignment.

### Regression Testing

The test suite also supports **regression testing**. Whenever new features or changes are introduced, running the full test suite with `pytest` ensures that previously working functionality has not been broken. If any test fails, it indicates that a regression has occurred.

---

## 3. Test Results Summary

| Test Name | Type | Status |
|-----------|------|--------|
| test_add_integers | Unit | Pass |
| test_subtract_integers | Unit | Pass |
| test_multiply_integers | Unit | Pass |
| test_divide_integers | Unit | Pass |
| test_divide_by_zero_raises_value_error | Unit | Pass |
| test_add_negative_numbers | Unit | Pass |
| test_subtract_negative_result | Unit | Pass |
| test_multiply_by_zero | Unit | Pass |
| test_divide_decimal_result | Unit | Pass |
| test_add_large_numbers | Unit | Pass |
| test_add_decimals | Unit | Pass |
| test_divide_returns_float | Unit | Pass |
| test_user_flow_addition | Integration | Pass |
| test_clear_after_calculation_resets_to_zero | Integration | Pass |
| test_divide_by_zero_shows_error | Integration | Pass |
| test_operator_replacement | Integration | Pass |

All tests were executed using `pytest` and completed successfully.