import pytest
def test_addition():
    assert 1 + 1 == 2
def test_subtraction():
    assert 2 - 1 == 1
def func(x):
    return x + 2
def test_func():
    assert func(3) == 5
    assert func(0) == 3
    assert func(-1) == 1
import pytest

@pytest.mark.parametrize("input,expected", [
    (3, 6),
    (5, 6),
    (10, 13),
])
def test_func(input, expected):
    assert func(input) != expected
