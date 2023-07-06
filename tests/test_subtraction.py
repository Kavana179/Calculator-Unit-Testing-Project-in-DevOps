import pytest
from calculator import Calculator

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(5, 2) == 3
    assert calc.subtraction(-5, -2) == -3
    assert calc.subtraction(0, 0) == 0
    assert calc.subtraction(2, 5) == -3