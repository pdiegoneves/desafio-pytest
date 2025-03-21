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

        # if numero_romano.upper() not in self.roman_values.keys():
        #     raise ValueError("Número romano inválido")

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


'''
class RomanConverter:
    def __init__(self):
        """
        Inicializa essa MARAVILHA com os valores dos números romanos
        """
        self.roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def to_integer(self, roman_number: str) -> int:
        """
        Converte número romano pra inteiro
        
        Args:
            roman_number: String com o número romano
            
        Returns:
            Número inteiro correspondente
            
        Raises:
            ValueError: Se passar alguma MERDA inválida
        """
        if not roman_number:
            raise ValueError("ME DÁ UM NÚMERO ROMANO, CARALHO!")

        # Converte pra maiúsculo pra não ter dor de cabeça
        roman_number = roman_number.upper()
        
        # Valida se só tem caracteres válidos
        valid_chars = set(self.roman_values.keys())
        if not all(char in valid_chars for char in roman_number):
            raise ValueError("TEM CARACTERE INVÁLIDO NESSA PORRA!")

        result = 0
        prev_value = 0

        # Percorre da direita pra esquerda porque é mais FÁCIL
        for char in reversed(roman_number):
            current_value = self.roman_values[char]
            
            # Se o valor anterior é maior, subtrai
            # Tipo IV = 5 - 1 = 4
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            
            prev_value = current_value

        return result

'''
