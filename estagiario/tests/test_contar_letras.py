from src.contar_letras import contar_letras, contar_vogais
def test_em_banana_tem_tres_a():
    context = "banana"
    received = contar_letras(context, "a")
    assert received == 3

def test_em_banana_tem_dois_n():
    context = "banana"
    received = contar_letras(context, "n")
    assert received == 2

def test_em_BANANA_tem_dois_n():
    '''
    Ignorar case sensitive
    '''
    context = "BANANA"
    received = contar_letras(context, "n")
    assert received == 2

def test_em_banana_tem_tres_vogais():
    context = "banana"
    received = contar_vogais(context)
    assert received == 3

def test_em_abacaxi_tem_quatro_vogais():
    context = "abacaxi"
    received = contar_vogais(context)
    assert received == 4