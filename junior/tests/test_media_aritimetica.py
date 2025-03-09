import pytest
from src.media_aritimetica import media_aritimetica

def test_media():
    contexto = [1, 2, 3, 4, 5]
    resultado = media_aritimetica(contexto)
    esperado = 3
    assert esperado == resultado

def test_media_lista_vazia():
    contexto = []
    resultado = media_aritimetica(contexto)
    esperado = 0.0
    assert esperado == resultado

def test_media_num_como_string():
    contexto = ['1', '2', '3', '4', '5']
    resultado = media_aritimetica(contexto)
    esperado = 3
    assert esperado == resultado

def test_media_string_retorna_erro():
    contexto = ['1', 'a', '3', '4', '5']
    with pytest.raises(ValueError):
        resultado = media_aritimetica(contexto)