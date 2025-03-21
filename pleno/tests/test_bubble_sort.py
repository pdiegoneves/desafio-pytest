import pytest
from src.bubble_sort import BubbleList


@pytest.fixture
def bubble_list():
    return BubbleList(3, 4, 2, 1, 5)


def test_ordenar_crescente(bubble_list):
    assert bubble_list.sort() == [1, 2, 3, 4, 5]


def test_ordenar_decrescente(bubble_list):
    assert bubble_list.sort(reverse=True) == [5, 4, 3, 2, 1]


def test_ordenar_lista_vazia():
    bubble_list = BubbleList()
    assert bubble_list.sort() == []


def test_ordenar_lista_com_um_elemento():
    bubble_list = BubbleList(5)
    assert bubble_list.sort() == [5]


def test_bubble_sort_reverse_sorted_list():
    bubble_list = BubbleList(5, 4, 3, 2, 1)
    assert bubble_list.sort() == [1, 2, 3, 4, 5]


@pytest.mark.parametrize(
    "entradas, saidas",
    [
        ([3, 4, 2, 1, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([2, 1], [1, 2]),
        ([], []),
    ],
)
def test_ordenar_varias_listas_com_parametrize_crescente(entradas, saidas):
    bubble_list = BubbleList(*entradas)
    assert bubble_list.sort() == saidas


@pytest.mark.parametrize(
    "entradas, saidas",
    [
        ([3, 4, 2, 1, 5], [5, 4, 3, 2, 1]),
        ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
    ],
)
def test_ordenar_varias_listas_com_parametrize_decrecente(entradas, saidas):
    bubble_list = BubbleList(*entradas)
    assert bubble_list.sort(reverse=True) == saidas
