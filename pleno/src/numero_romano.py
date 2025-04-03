import sys


class NumeroRomano:
    def __init__(self, numero_romano):
        self.roman_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        if not numero_romano.strip():
            raise ValueError("Número romano inválido")

        for char in numero_romano.strip():
            if char.upper() not in self.roman_values.keys():
                raise ValueError("Número romano inválido")

        self._numero_romano = numero_romano.strip().upper()

    def em_inteiro(self):
        resultado = 0
        valor_anterior = 0

        # Percorre da direita pra esquerda porque é mais FÁCIL
        for char in reversed(self._numero_romano):
            valor_atual = self.roman_values[char]

            # Se o valor anterior é maior, subtrai
            # Tipo IV = 5 - 1 = 4
            if valor_atual < valor_anterior:
                resultado -= valor_atual
            else:
                resultado += valor_atual

            valor_anterior = valor_atual

        return resultado

    def imprimir(self):
        print(self.em_inteiro())

    def imprimir2(self):  # pragma: no cover
        print(self.em_inteiro())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        numero_romano = NumeroRomano(arg)
        numero_romano.imprimir()
