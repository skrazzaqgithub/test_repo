import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_numbers(number):
    # This test runs 3 times, with number = 1, 2, and 3
    assert number in [1, 2, 3]