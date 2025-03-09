import pytest
import string
from src.gerar_de_senha import GeradorDeSenha

@pytest.fixture
def senha_padrao():
    return GeradorDeSenha().gerar_senha()

@pytest.fixture
def senha_dez():
    return GeradorDeSenha(tamanho=10).gerar_senha()

def test_gerar_sennha_padrao_8_caracteres(senha_padrao):
    assert len(senha_padrao) == 8

def test_senha_padrao_forte(senha_padrao):
    tem_maiusculo = any(char.isupper() for char in senha_padrao)
    tem_minusculo = any(char.islower() for char in senha_padrao)
    tem_numero = any(char.isdigit() for char in senha_padrao)
    tem_especial = any(char in string.punctuation for char in senha_padrao)
    assert tem_maiusculo and tem_minusculo and tem_numero and tem_especial

def test_senha_10_digitos(senha_dez):
    assert len(senha_dez) == 10