import pytest
from src.numero_romano import NumeroRomano


@pytest.fixture
def numero_romano_I():
    return NumeroRomano("I")


@pytest.fixture
def numero_romano_II():
    return NumeroRomano("II")


@pytest.fixture
def numero_romano_i():
    return NumeroRomano("i")


@pytest.fixture
def numero_romano_XI():
    return NumeroRomano("XI")


@pytest.fixture
def numero_romano_IX():
    return NumeroRomano("XI")


def test_I_e_numero_romano(numero_romano_I):
    assert isinstance(numero_romano_I, NumeroRomano)


def test_i_e_numero_romano(numero_romano_i):
    assert isinstance(numero_romano_i, NumeroRomano)


def test_II_e_numero_romano(numero_romano_II):
    assert isinstance(numero_romano_II, NumeroRomano)


def test_1_retorna_erro():
    with pytest.raises(ValueError, match="Número romano inválido"):
        NumeroRomano("1")


def test_i1_retorna_erro():
    with pytest.raises(ValueError, match="Número romano inválido"):
        NumeroRomano("i1")


def test_I_em_inteiro_e_1(numero_romano_I):
    assert numero_romano_I.em_inteiro() == 1


def test_XI_em_inteiro_e_11(numero_romano_XI):
    assert numero_romano_XI.em_inteiro() == 11


def test_varias_convercoes():
    assert NumeroRomano("X").em_inteiro() == 10
    assert NumeroRomano("XL").em_inteiro() == 40
    assert NumeroRomano("C").em_inteiro() == 100
    assert NumeroRomano("XC").em_inteiro() == 90
    assert NumeroRomano("CXXX").em_inteiro() == 130
    assert NumeroRomano("XLIX").em_inteiro() == 49
    assert NumeroRomano("XLIX ").em_inteiro() == 49
    assert NumeroRomano("LXXXIV").em_inteiro() == 84
