import pytest
from calculator.operations import Calculator

calc = Calculator()

def test_add():
    assert calc.add(7, 9) == 16

def test_subtract():
    assert calc.subtract(9, 3) == 6

def test_multiply():
    assert calc.multiply(5, 8) == 40

def test_divide():
    assert calc.divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)
