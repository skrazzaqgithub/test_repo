# import pytest
from calc.math import addition, substraction, multiplication
# print("Testing add function:", addition(2,7))  # Expected output: 5
# print("Testing subtract function:", substraction(7,2))  # Expected output: 2
# print("Testing multiply function:", multiplication(9,2))  # Expected output: 6
@pytest.fixture()
def test_addition():
    assert addition(33,44) == 77
#
# # @pytest.fixture()
# def test_subtract():
#     assert substraction(44,33) == 11

# import pytest
#
# @pytest.mark.parametrize("x,y,result", [
#     (3, 5, 8),
#     (0, 2, 2),
#     (-1, 1, 0),
# ])
# def test_func(x,y, result):
#     assert test_func(x,y) == result
