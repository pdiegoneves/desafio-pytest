from src.verificar_num import verificar_num


def test_e_negativo():
    context = -1
    received = verificar_num(context)
    assert received == "negativo"


def test_e_positivo():
    context = 1
    received = verificar_num(context)
    assert received == "positivo"


def test_e_zero():
    context = 0
    received = verificar_num(context)
    assert received == "zero"
