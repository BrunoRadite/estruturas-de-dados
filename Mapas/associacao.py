from carros import Carro
class Associacao:
    def __init__(self, carro: Carro, placa: str):
        self.__carro = carro
        self.__placa = placa
        
    @property
    def carro(self):
        return self.__carro
    
    @carro.setter
    def carro(self, carro):
        self.__carro = carro
        
    
    @property
    def placa(self):
        return self.__placa
    
    @placa.setter
    def placa(self, placa):
        self.__placa = placa
        
    def __str__(self):
        return f'{self.__carro.nome}, da marca {self.__carro.marca}, de cor {self.__carro.cor}, do ano {self.__carro.ano}, associado à placa {self.__placa}'
    