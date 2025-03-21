import pytest
from src.fatorial import fatorial


def test_fatorial_de_0():
    assert fatorial(0) == 1


def test_fatorial_de_1():
    assert fatorial(1) == 1


def test_fatorial_de_negativo():
    # assert fatorial(-1) == "Não existe fatorial de um número negativo"
    # assert pytest.raises(ValueError)
    with pytest.raises(ValueError):
        fatorial(-1)


def test_fatorial_de_5():
    assert fatorial(5) == 120


def test_fatorial_de_3():
    assert fatorial(3) == 6
