class Carro:
    def __init__(self, nome:str, marca:str, cor:str, ano:int):
        self.__nome = nome
        self.__marca = marca
        self.__cor = cor
        self.__ano = ano
    
    
    # Nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,valor):
        self.__nome = valor
    
    
    # Marca
    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self,valor):
        self.__marca = valor
        
        
    # Cor
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self,valor):
        self.__cor = valor
        
        
    # Ano
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,valor):
        self.__ano = valor
        
    def __str__(self):
        return f'{self.__nome}, da marca {self.__marca}, de cor {self.__cor}, do ano {self.__ano}'