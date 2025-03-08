from src.inverter_string import inverter
def test_inverter_abacaxi():
    context = "abacaxi"
    received = inverter(context)
    assert received == "ixacaba"


def test_inverter_celular():
    context = "celular"
    received = inverter(context)
    assert received == "ralulec"

