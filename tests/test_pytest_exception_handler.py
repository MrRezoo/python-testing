import pytest
from src.sample_func import add, subtract, multiply, division


def test_add():
    assert add(3, 4) == 7
    assert add(-1, 4) == 3
    assert add(0, 4) == 4


def test_subtract():
    assert subtract(3, 4) == -1
    assert subtract(-1, 4) == -5
    assert subtract(0, 4) == -4


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(3, 4) != 11
    assert multiply(-1, 4) == -4
    assert multiply(0, 4) == 0


def test_division():
    assert division(12, 4) == 3
    with pytest.raises(ZeroDivisionError):
        division(2, 0)
