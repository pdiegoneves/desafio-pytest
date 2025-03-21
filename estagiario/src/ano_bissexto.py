def e_ano_bissexto(ano: int) -> bool:
    """
    O ano é bissexto quando:
        É divisível por 4
        Se for divisível por 100, também deve ser divisível por 400
    """

    e_divisivel_por_4 = ano % 4 == 0
    nao_e_divisivel_por_100 = ano % 100 != 0
    e_divisivel_por_400 = ano % 400 == 0

    bissexto = (e_divisivel_por_4 and nao_e_divisivel_por_100) or e_divisivel_por_400
    return bissexto
