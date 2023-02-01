from associacao import Associacao
from carros import Carro

class Mapa:
    def __init__(self):
        self.__associacoes = []
        self.__tamanho = 0
        
        
    def adiciona(self, placa:str, carro:Carro):
        if not self.contem_placa(placa):
            associacao = Associacao(carro, placa)
            self.__associacoes.append(associacao)
            self.__tamanho += 1

    def pega(self, placa):
        for associacao in self.__associacoes:
            if (associacao.placa == placa):
                return associacao.carro
        
        return 'carro não encontrado'
    
    def remove(self, placa):
        self.__associacoes = [associacao for associacao in self.__associacoes if associacao.placa != placa]
        self.__tamanho -= 1
        
        
    def contem_placa(self, placa):
        for associacao in self.__associacoes:
            if (associacao.placa == placa):
                return True
                        
        return False
    
    
    @property
    def tamanho(self):
        return self.__tamanho
    

    def __str__(self):
        string = '{'
        for associacao in self.__associacoes:
            string = string + f'\n\t{associacao.placa} : ({associacao.carro}),\n'
        string = string + '}'
        return string
        
        
    