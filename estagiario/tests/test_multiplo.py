import pytest
from src.multiplo import e_multiplo


def test_5_e_multiplo_de_35():
    context = (5, 35)
    received = e_multiplo(context)
    assert received is True

def test_35_e_multiplo_de_5():
    context = (35, 5)
    received = e_multiplo(context)
    assert received is True

def test_3_nao_e_multiplo_de_35():
    context = (3, 35)
    received = e_multiplo(context)
    assert received is False
   
def test_35_nao_e_multiplo_de_3():
    context = (3, 35)
    received = e_multiplo(context)
    assert received is False
   