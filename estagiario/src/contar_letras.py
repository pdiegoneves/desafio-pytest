def contar_letras(texto, letra):
    texto = texto.lower()
    letra = letra.lower()
    quantitade_letras = texto.count(letra)
    return quantitade_letras

def contar_vogais(texto):
    texto = texto.lower()
    vogais = "aeiou"

    quantitade_vogais = 0
    for vogal in vogais:
        quantitade_vogais += texto.count(vogal)

    # quantitade_vogais = sum([texto.count(vogal) for vogal in vogais])
    
    return quantitade_vogais
