from associacao import Associacao


class MapaEspalhamento:
    def __init__(self):
        self.__tabela_hash = []
        
        for _ in range(0,30):
            self.__tabela_hash.append([])
        
        self.__tamanho = 0
        
    
    def calcula_indice_tabela(self,placa):
        codigo_espalhamento = self.funcao_hash(placa)
        codigo_espalhamento = abs(codigo_espalhamento)
        return codigo_espalhamento % len(self.__tabela_hash)


    def funcao_hash(self,placa):
        codigo = 1
        for i in range(0, len(placa)):
            codigo = 7 * codigo + ord(placa[i])
        return codigo
    

    def contem_chave(self, placa):
        indice = self.calcula_indice_tabela(placa)
        lista = self.__tabela_hash[indice]
        for associacao in lista:
            if placa == associacao.placa:
                return True
        return False
    
    def adiciona(self, placa, carro):
        if self.contem_chave(placa):
            self.remove(placa)
        
        indice = self.calcula_indice_tabela(placa)
        lista:list = self.__tabela_hash[indice]
        
        associacao = Associacao(carro, placa)
        lista.append(associacao)
        self.__tamanho += 1
    
    
    def remove(self, placa):
        indice = self.calcula_indice_tabela(placa)
        self.__tabela_hash[indice] = [associacao for associacao in self.__tabela_hash[indice] if associacao.placa != placa]
        self.__tamanho -= 1
    
    def tamanho(self):
        return self.tamanho
    
    def pega(self, placa):
        indice = self.calcula_indice_tabela(placa)
        for associacao in self.__tabela_hash[indice]:
            if (associacao.placa == placa):
                return associacao.carro
        
        return 'carro não encontrado'
    
    def __str__(self):
        return f'{self.__tabela_hash}'
            