import pytest
from calculator import Calculator

def test_division():
    calc = Calculator()
    assert calc.division(10, 2) == 5
    assert calc.division(-10, -2) == 5
    assert calc.division(0, 10) == 0
    with pytest.raises(ValueError):
        calc.division(10, 0)