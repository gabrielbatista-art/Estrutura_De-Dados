class FilaArray:

    
    def __init__(self, capacidade):
        
        # self.lista = self.capacidade
        self.lista = [None] * capacidade
        self.inicio = 0
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho
    
    def vazia(self):
        return self.tamanho == 0
    
    def enfileirar(self, valor):
        if self.tamanho == len(self.lista):
            self.redimensionar(2 * len(self.lista))
        disponivel = (self.inicio + self.tamanho) % len(self.lista)
        self.lista[disponivel] = valor
        self.tamanho += 1
    
    def desenfileirar(self):
        if self.vazia():
            raise IndexError("Fila Vazia")
        resultado = self.lista[self.inicio]
        self.inicio = (self.inicio + 1) % len(self.lista)
        self.tamanho -= 1
        return resultado
    
    def redimensionar(self, capacidade):
        lista_antiga = self.lista
        self.lista = [None] * capacidade
        for k in range(self.tamanho):
            self.lista[k] = lista_antiga[(self.inicio +k) % len(lista_antiga)]
        self.inicio = 0
    
    def primeiro_fila(self):
        if self.vazia():
            raise IndexError("Fila vazia")
        return self.lista[self.inicio]
    
    def ultimo_fila(self):
        if self.vazia():
            raise IndexError("Fila vazia")
        return self.lista[(self.lista + self.tamanho - 1) % len(self.lista)]