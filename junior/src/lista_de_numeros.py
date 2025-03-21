import pytest


def obter_maior(lista: list) -> int:
    try:
        nums = [int(item) for item in lista]
        return max(nums)
    except:
        raise ValueError("Os itens da lista devem ser numéricos")

    # nums = []
    # for item in lista:
    #     try:
    #         nums.append(int(item))
    #     except ValueError:
    #         continue
    # return max(nums)
