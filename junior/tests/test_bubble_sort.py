import pytest
from src.bubble_sort import BlubleList

@pytest.fixture
def lista1():
    lista = BlubleList(3,4,2,1,5)



def test_34215_retonra12345():
    assert bubble_sort([4, 3, 2, 1, 5]) == [1, 2, 3, 4, 5]