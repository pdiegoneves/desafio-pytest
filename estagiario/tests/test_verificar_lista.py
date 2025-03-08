from src.verifcar_lista import verificar_lista

lista = ["maça", "uva", "banana", "abacaxi"]
def test_tem_banana():
    item = "banana"
    received = verificar_lista(lista, item)
    assert received is True

def test_nao_tem_laranja():
    item = "laranja"
    received = verificar_lista(lista, item)
    assert received is False

