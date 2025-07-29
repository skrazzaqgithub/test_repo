import pytest
@pytest.fixture()
def multiplication(x):
    for i in range(1, 11):
        print(f"{x} * {i} = {x * i}")
if __name__ == "__main__":
    num = int(input("Enter a number to multiply: "))
    multiplication(num)

import pytest

# @pytest.fixture
# def sample_data():
#     return {"name": "Alice", "age": 30}
#
# def test_user_age(sample_data):
#     assert sample_data["age"] == 30
#     assert sample_data["name"] == "Alice"