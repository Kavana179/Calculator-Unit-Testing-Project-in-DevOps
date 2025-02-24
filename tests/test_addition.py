import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.addition(2, 3) == 5
    assert calc.addition(-2, 3) == 1
    assert calc.addition(0, 0) == 0
