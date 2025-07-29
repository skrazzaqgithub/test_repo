# import pytest
#
# @pytest.fixture
# def sample_data():
#     return {"name": "Alice", "age": 30}
#
# def test_user_age(sample_data):
#     assert sample_data["age"] == 30
#     assert sample_data["name"] == "Alice"

import pytest
@pytest.fixture
def user_data():
    return {"name": "Alice", "age": 30, "address": "123 Main St"}
def test_user_role(user_data):
    assert user_data["age"] == 30
def test_user_name(user_data):
    assert user_data["name"] == "Alice"
def test_user_data(user_data):
    assert user_data == {"name": "Alice", "age": 30, "address": "123 Main St"}
def test_user_data_keys(user_data):
    assert "name" in user_data
    assert "age" in user_data
@pytest.fixture(scope="function", autouse=True)
def user_setup_teardown(user_data):
    # Setup code before each test
    user_data["name"] = "Alice"
    yield user_data
def test_user_with_address(user_data):
    user_data["address"] = "123 Main St"
    assert user_data["address"] == "123 Main St"
