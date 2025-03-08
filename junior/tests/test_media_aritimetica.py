from src.media_aritimetica import media_aritimetica

def test_media():
    contexto = [1, 2, 3, 4, 5]
    resultado = media_aritimetica(contexto)
    esperado = 3
    assert esperado == resultado

def test_media_lista_vazia():
    contexto = []
    resultado = media_aritimetica(contexto)
    esperado = 0
    assert esperado == resultado