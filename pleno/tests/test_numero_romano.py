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


def test_I_e_numero_romano(numero_romano_I):
    assert isinstance(numero_romano_I, NumeroRomano)


def test_i_e_numero_romano(numero_romano_i):
    assert isinstance(numero_romano_i, NumeroRomano)


def test_II_e_numero_romano(numero_romano_II):
    assert isinstance(numero_romano_II, NumeroRomano)


@pytest.mark.parametrize(
    "entrada", ["I", "i", "II", "XI", "IX", "XC", "C", "CXXX", "XLIX", "LXXXIV"]
)
def test_varias_convercoes_2(entrada):
    assert NumeroRomano(entrada).em_inteiro()


@pytest.mark.parametrize(
    "entrada, mensagem_erro",
    [
        ("1", "Número romano inválido"),
        ("i1", "Número romano inválido"),
        ("ABC", "Número romano inválido"),
        ("", "Número romano inválido"),
        ("#", "Número romano inválido"),
    ],
)
def test_criar_numero_romano_invalido(entrada, mensagem_erro):
    with pytest.raises(ValueError, match=mensagem_erro):
        NumeroRomano(entrada)


@pytest.mark.parametrize(
    "romano, inteiro",
    [
        ("I", 1),
        ("XI", 11),
        ("X", 10),
        ("XL", 40),
        ("C", 100),
        ("XC", 90),
        ("CXXX", 130),
        ("XLIX", 49),
        ("XLIX ", 49),  # Testa com espaço
        ("LXXXIV", 84),
        ("IV", 4),
        ("IX", 9),
        ("XCIX", 99),
        ("CDXLIV", 444),
        ("MCMXCIX", 1999),
    ],
)
def test_varias_convercoes_3(romano, inteiro):
    assert NumeroRomano(romano).em_inteiro() == inteiro
