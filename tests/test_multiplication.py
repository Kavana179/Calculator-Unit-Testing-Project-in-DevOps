import pytest
from calculator import Calculator

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(2, 3) == 6
    assert calc.multiplication(-2, 3) == -6
    assert calc.multiplication(0, 5) == 0
    assert calc.multiplication(2.5, 2) == 5