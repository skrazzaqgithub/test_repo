import pytest
@pytest.fixture
def sample_list():
    print("Setting up sample list")
    data = [1, 2, 3, 4, 5]
    yield data
    print("Tearing down sample list")
def test_sample_list_sum(sample_list):
    # assert len(sample_list) == 5
    assert sum(sample_list) == 15
@pytest.fixture(scope="function", autouse=True)
def simple_list2():
    print("Setting up simple list")
    data1= [1, 2, 3, 4, 5]
    yield data1
    print("Tearing down simple list")

def test_simple_list_length(simple_list2):
    assert len(simple_list2) == 5
    # assert sum(simple_list2) == 15