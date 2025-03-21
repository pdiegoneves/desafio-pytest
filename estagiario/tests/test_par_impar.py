from src.par_impar import par_ou_impar


def test_um_e_impar():
    context = 1
    received = par_ou_impar(context)
    assert received == "impar"


def test_dois_e_par():
    context = 2
    received = par_ou_impar(context)
    assert received == "par"
