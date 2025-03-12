import pytest
from src.bubble_sort import BubbleList

@pytest.fixture
def lista1():
    return BubbleList(3, 4, 2, 1, 5)


def test_34215_retonra12345(lista1):
    assert lista1.sort() == [1, 2, 3, 4, 5]

def test_34215_reverse_retonra54321(lista1):
    assert lista1.sort(reverse=True) == [5, 4, 3, 2, 1]