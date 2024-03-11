from fila1 import *

class deque:

    def __init__(self):
        self.dk = FilaArray(11)
    
    def __len__(self):
        return len(self.dk)
    
    def primeiro(self):
        return self.dk.primeiro_fila()
    
    def ultimo(self):
        return self.dk.ultimo_fila()
    
    def adiciona_comeco(self,valor):
        aux_fila = FilaArray(valor)
        aux_fila.tamanho += 1
        while not self.dk.vazia():
            aux_fila.enfileirar(self.dk.desenfileirar())
        self.dk = aux_fila
    
    def adiciona_ultimo(self,valor):
        self.dk.enfileirar(valor)
    
    def delete_comeco(self):
        return self.dk.desenfileirar()
    
    def delete_ultimo(self):
        aux_fila = FilaArray()
        while not self.dk.vazia():
            if len(self.kd) == 1:
                return self.dk.desenfileirar()
            aux_fila.enfileirar(self.dk.desenfileirar)

    def vazia(self):
        return self.dk.vazia()
