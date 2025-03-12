class BubbleList():
    def __init__(self, *args):
        self._list = list(args)

    def sort(self, reverse=False):
        
        resultado = self._list.copy()
        tamanho = len(resultado)
        
        for i in range(tamanho):
            sorteado = True
            
            # Compara elementos adjacentes
            for j in range(0, tamanho - i - 1):
                
                if reverse:     
                    if resultado[j] < resultado[j + 1]:
                        resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                        sorteado = False
                else:
                    if resultado[j] > resultado[j + 1]:
                        resultado[j], resultado[j + 1] = resultado[j + 1], resultado[j]
                        sorteado = False
            
            # Se não teve troca, já tá ordenado
            if sorteado:
                break
                
        return resultado