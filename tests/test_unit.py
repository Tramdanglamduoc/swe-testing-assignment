import pytest
from quick_calc.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# -------- Basic operations --------

def test_add_integers(calc):
    assert calc.add(5, 3) == 8


def test_subtract_integers(calc):
    assert calc.subtract(10, 4) == 6


def test_multiply_integers(calc):
    assert calc.multiply(6, 7) == 42


def test_divide_integers(calc):
    assert calc.divide(8, 2) == 4


# -------- Edge cases --------

def test_divide_by_zero_raises_value_error(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


def test_add_negative_numbers(calc):
    assert calc.add(-5, 2) == -3


def test_subtract_negative_result(calc):
    assert calc.subtract(3, 10) == -7


def test_multiply_by_zero(calc):
    assert calc.multiply(123, 0) == 0


def test_divide_decimal_result(calc):
    assert calc.divide(5, 2) == 2.5


def test_add_large_numbers(calc):
    assert calc.add(10**12, 10**12) == 2 * 10**12


def test_add_decimals(calc):
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)


def test_divide_returns_float(calc):
    assert isinstance(calc.divide(10, 2), float)