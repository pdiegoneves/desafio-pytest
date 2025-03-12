import string
import random

class GeradorDeSenha():
    def __init__(self, tamanho=8):
        self._tamanho = tamanho
        self._minusculo = string.ascii_lowercase
        self._maiusculo = string.ascii_uppercase
        self._numeros = string.digits
        self._especiais = string.punctuation
        self._todos_caracteres = self._minusculo + self._maiusculo + self._numeros + self._especiais


    def gerar_senha(self):
        senha = [
            random.choice(self._minusculo),
            random.choice(self._maiusculo),
            random.choice(self._numeros),
            random.choice(self._especiais)
        ]

        for _ in range(self._tamanho - len(senha)):
            senha.append(random.choice(self._todos_caracteres))

        random.shuffle(senha)
        return "".join(senha)

