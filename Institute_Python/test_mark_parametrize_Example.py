import pytest

def func(x):
    return x + 2

@pytest.mark.parametrize("input,expected", [
    (3, 5),
    (0, 2),
    (-1, 1),
])
def test_func(input, expected):
    assert func(input) == expected
