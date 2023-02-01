# Classe Conjunto
class Conjunto:

    # Método construtor
    def __init__(self):

        # Iniciando a estrutura do conjunto, vale ressaltar que no Conjunto, os valores dentro dele jamais se repetem
        self.__estrutura = set()

    
    # Método para adicionar algum objeto ao conjunto
    def _add(self, objeto):

        self.__estrutura.add(objeto)
    

    # Método para remover algum objeto do conjunto
    def _remove(self, objeto):

        self.__estrutura.remove(objeto)
    

    # Método Dunder para a função print
    def __str__(self):

        # Declaração da variavel que armazenará os itens em formato de String
        itens_conjunto = ""

        # Para cada item dentro da conjunto
        for item in self.__estrutura:

            itens_conjunto += str(item) + "\n"
        
        # Retornar os itens da conjunto em formato de String
        return itens_conjunto