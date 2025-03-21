# received = input("Qual o seu nome?")
# def ola(received):

#     if received:
#         return f"Olá, {received}!"

#     return "Olá, Mundo!"


def ola(received):
    received = received if received else "Mundo"

    return f"Olá, {received}!"
