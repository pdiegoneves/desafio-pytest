# def fatorial(num):
#     if num == 0:
#         return 1
#     elif num < 0:
#         return "Não existe fatorial de um número negativo"
#     else:
#         resultado = 1
#         for i in range(1, num+1):
#             resultado *= i

#         return resultado


def fatorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError("Não existe fatorial de um número negativo")
    else:
        return num * fatorial(num - 1)