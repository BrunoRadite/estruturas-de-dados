# Classe Armazenamento Sequencial
class ArmazenamentoSequencial:

    # Método construtor
    def __init__(self):

        self.__estrutura = []

    
    # Método para adicionar algum objeto a armazenamnto_sequencial
    def _add(self, objeto):

        self.__estrutura.append(objeto)
    

    # Método para remover algum objeto a armazenamnto_sequencial
    def _pop(self, index):
        
        try:

            del self.__estrutura[index]
        
        except IndexError:

            print("Index não existente")
    

    # Método Dunder para a função print
    def __str__(self):

        # Declaração da variavel que armazenará os itens em formato de String
        itens_armazenamnto_sequencial = ""

        # Para cada item dentro da armazenamnto_sequencial
        for item in self.__estrutura:

            itens_armazenamnto_sequencial += str(item) + "\n"
        
        # Retornar os itens da armazenamnto_sequencial em formato de String
        return itens_armazenamnto_sequencial