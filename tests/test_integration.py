import tkinter as tk
import pytest
from quick_calc.gui import QuickCalcApp


@pytest.fixture
def app():
    root = tk.Tk()
    root.withdraw()  # run without showing the window
    application = QuickCalcApp(root)
    yield application
    root.destroy()


def test_user_flow_addition(app):
    # 5 + 3 =
    app.press("5")
    app.press("+")
    app.press("3")
    app.press("=")
    assert app.get_display() == "8"


def test_clear_after_calculation_resets_to_zero(app):
    # 9 * 2 = 18, then C => 0
    app.press("9")
    app.press("*")
    app.press("2")
    app.press("=")
    assert app.get_display() == "18"

    app.press("C")
    assert app.get_display() == "0"


def test_divide_by_zero_shows_error(app):
    # 5 / 0 = => Error (because Calculator raises ValueError, GUI shows "Error")
    app.press("5")
    app.press("/")
    app.press("0")
    app.press("=")
    assert app.get_display() == "Error"


def test_operator_replacement(app):
    # If user presses ++, second operator replaces the first
    # 7 + * 2 = => 14 (because + replaced by *)
    app.press("7")
    app.press("+")
    app.press("*")
    app.press("2")
    app.press("=")
    assert app.get_display() == "14"