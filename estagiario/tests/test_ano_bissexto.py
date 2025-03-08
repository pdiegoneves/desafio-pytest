from src.ano_bissexto import e_ano_bissexto

def test_ano_2000_e_bissexto():
    context = 2000
    received = e_ano_bissexto(context)
    assert received is True

def test_ano_2001_noa_e_bissexto():
    context = 2001
    received = e_ano_bissexto(context)
    assert received is False