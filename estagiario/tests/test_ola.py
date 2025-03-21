from src.ola import ola


def test_ola_vazio():
    context = ""
    received = ola(context)
    assert received == "Olá, Mundo!"


def test_ola_joao():
    context = "João"
    received = ola(context)
    assert received == "Olá, João!"
