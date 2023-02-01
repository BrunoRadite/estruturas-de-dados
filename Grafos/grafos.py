class Matriz:
    def __init__(self,quantidade):
        self.quantidade_nos = quantidade
        self.grafo = []
        self.__criaMatriz(self.quantidade_nos)
        
    def __criaMatriz(self, quantidade):
        for _ in range(quantidade):
            linha = []
            for _ in range(quantidade):
                linha.append(0)
            self.grafo.append(linha)
        
            
    def adicionar_aresta(self, linha:int, coluna: int):
        self.grafo[linha - 1][coluna - 1] = 1
        self.grafo[coluna - 1][linha - 1] = 1
    
    
    def tem_ligacao(self,linha:int, coluna: int):
        if self.grafo[linha - 1][coluna - 1] == 1:
            return True
        return False
           
    
    def __str__(self):
        saida = ''
        for linha in self.grafo:
            for coluna in linha:

                saida += f' {coluna} '

            saida += '\n'
        
        return saida
    

m = Matriz(5)
m.adicionar_aresta(1,4)
print(m)