from src import sample_func


def test_add():
    assert sample_func.add(3, 4) == 7
    assert sample_func.add(-1, 4) == 3
    assert sample_func.add(0, 4) == 4


def subtract():
    assert sample_func.subtract(3, 4) == -1
    assert sample_func.subtract(-1, 4) == -5
    assert sample_func.subtract(0, 4) == -4


def multiply():
    assert sample_func.multiply(3, 4) == 12
    assert sample_func.multiply(3, 4) != 11
    assert sample_func.multiply(-1, 4) == -4
    assert sample_func.multiply(0, 4) == 0


def division():
    assert sample_func.multiply(12, 4) == 3
