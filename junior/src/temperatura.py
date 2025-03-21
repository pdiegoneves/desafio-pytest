class Temperatura:
    def __init__(self, temperatura, unidade="Celsius"):
        self._temperatura = temperatura
        self._unidade = unidade

    def em_fahrenheit(self):
        temp = self._temperatura
        if self._unidade == "Celsius":
            temp = (self._temperatura * 9 / 5) + 32

        return round(temp, 1)

    def em_celsius(self):
        temp = self._temperatura
        if self._unidade == "Fahrenheit":
            temp = (self._temperatura - 32) * 5 / 9

        return round(temp, 1)
