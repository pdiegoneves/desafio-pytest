def media_aritimetica(lista:list) -> float:
    try:
        lista = [int(item) for item in lista] 
        media = sum(lista) / len(lista)
    except ZeroDivisionError:
        media = 0.0
    except ValueError:
        raise ValueError("Os itens da lista devem ser numéricos")
        
    return media