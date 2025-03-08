def media_aritimetica(lista:list) -> float:
    try: 
        media = sum(lista) / len(lista)
    except ZeroDivisionError:
        media = 0
        
    return media