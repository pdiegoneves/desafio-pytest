import pytest
from src.lista_de_numeros import obter_maior


def test_o_maior_numero_e_5():
    context = [1, 2, 3, 4, 5]
    maior = obter_maior(context)
    assert maior == 5


def test_o_maior_numero_string():
    context = ["1", "2", 3, "4", "5"]
    maior = obter_maior(context)
    assert maior == 5


def test_o_maior_numero_string_que_nao_converte_retona_erro():
    context = ["1", "2", "a", "4", "5"]

    # maior = obter_maior(context)
    # assert maior == 5

    # assert pytest.raises(ValueError)

    with pytest.raises(ValueError):
        obter_maior(context)
