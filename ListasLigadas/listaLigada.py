from celulaLista import CelulaLista


# Classe Lista Ligada
class ListaLigada:


    def __init__(self):
        # primeira celula da lista
        self.__primeira = None
        # total de elementos da lista
        self.__total_elementos = 0
        # ultima celula da lista
        self.__ultima = None


    # adiciona um elemento no inicio da lista
    def adiciona_comeco(self, elemento):
        nova_celula = CelulaLista(elemento,self.__primeira, None)

        # verificando se a lista já tinha elementos
        if self.__total_elementos >= 1:
            self.__primeira.anterior = nova_celula

        # atualizando a lista dizendo que a nova celula é nosso primeiro elemento
        self.__primeira = nova_celula

        # caso a lista não tivesse elementos então nossa nova celula também será a ultima
        if self.__total_elementos == 0:
            self.__ultima = nova_celula

        # atualizando o total de elementos da lista
        self.__total_elementos += 1


    # metodo adiciona elemento no final da lista
    def adiciona_fim(self, elemento):
        
        # verificando se o novo elemento vai ser o primeiro da lista
        if self.__total_elementos == 0:
            # então será adicionado no começo da lista
            self.adiciona_comeco(elemento)
            
        # caso a lista já possua elementos
        else: 
            # transformar o novo elemento em uma celula
            nova_celula = CelulaLista(elemento,None, self.__ultima)
            # a proxima celula da atual ultima celula será a nova celula
            self.__ultima.proxima = nova_celula
            # a ultima celula da lista agora será a nova celula
            self.__ultima = nova_celula
            # adicionando mais 1 no total de elementos
            self.__total_elementos += 1


    # adicionando elemento em uma determinada posição
    def adiciona_posicao(self, elemento, posicao):
        
        # se a posição que o usuário passou for 0 adicionar no começo da lista
        if posicao == 0: 
            self.adiciona_comeco(elemento)
            
        # se a posição for igual ao total de elementos adicionar no  final
        elif posicao == self.__total_elementos:
            self.adiciona_fim(elemento)
            
        # se não for nenhum dos casos acima
        else:
            # anterior a posição que o usuário passou
            anterior = self.pegar(posicao-1)
            # transformar o novo elemento em uma celula
            nova_celula = CelulaLista(elemento,anterior.proxima, anterior)
            # atualizar o anterior do proximo do anterior para ser a nova celula
            anterior.proxima.anterior = nova_celula
            # atualizar o proximo do anterior para ser a nova celula
            anterior.proxima = nova_celula
            # adicionar mais 1 ao total de elementos
            self.__total_elementos += 1
    
    
    # metodo pegar
    def pegar(self, posicao):
        
        # verificando se a posição é inválida
        if posicao < 0 or posicao >= self.__total_elementos:
            raise Exception('Posição inválida')
        
        # se a posição for válida
        else:
            # a atual celula que será retornada
            atual = self.__primeira
            # rodando da posição 0 até a posição desejada
            for _ in range(0, posicao):
                # atualizando o valor de atual
                atual = atual.proxima
            # retornando a atual celula
            return atual


    # metodo remover começo
    def remover_comeco(self):
        
        # caso a lista só possua 1 elemento
        if self.__total_elementos == 1:
            # a primeira celula da lista agora é none
            self.__primeira = None
            # a ultima celula da lista agora é none
            self.__ultima = None
        
        # caso a lista possua mais de 1 elemento
        else:
            # tirando o anterior da priemria celula da lista
            self.__primeira.proxima.anterior = None
            # a primeira celula agora é a segunda
            self.__primeira = self.__primeira.proxima
            
        # tirando 1 elemento da lista
        self.__total_elementos -= 1


    # metodo que retorna o tamanho da lista
    def tamanho(self):
        return self.__total_elementos


    # metodo que retorna true caso o elemento esteja na lista e falso caso não esteja
    def contem(self, elemento):
        
        atual = self.__primeira
        
        while atual is not None:
            
            if atual.elemento == elemento:
                return True
            
            atual = atual.proxima
            
        return False

    # metodo que remove de acordo com a posição
    def remover_posicao(self, posicao):
        # se a posição for 0 remove o começo
        if posicao == 0:
            self.remover_comeco()
        
        # se a posição for igual ao total -1 remove no final
        elif posicao == self.__total_elementos-1:
            self.remover_fim()
        
        # se não
        else:
            # pegaremos a celula de acordo com a posição
            celula = self.pegar(posicao)
            
            celula.anterior.proxima = celula.proxima
            celula.proxima = celula.anterior
            
            # tirando 1 elemento da lista
            self.__total_elementos -=1
     
            
    def remover_elemento(self, elemento):
        if self.contem(elemento) == False:
            print('esse elemento não está contido na lista') 
        atual = self.__primeira
        if elemento == self.__primeira:
            self.remover_comeco()
        else:
            while atual is not None:
            
                if atual.elemento == elemento:                    
                    if atual.proxima == None:
                        self.remover_fim()
                    else:
                        atual.anterior.proxima = atual.proxima
                        atual.proxima = atual.anterior
                        self.__total_elementos -=1
                    break  
                atual = atual.proxima


    def remover_todos_elementos(self, elemento):
        if self.contem(elemento) == False:
            print('esse elemento não está contido na lista') 
        atual = self.__primeira
        
        while atual is not None:
        
            if atual.elemento == elemento:                    
                if atual.proxima == None:
                    self.remover_fim()
                elif atual.anterior == None:
                    self.remover_comeco()
                else:
                    atual.anterior.proxima = atual.proxima
                    atual.proxima = atual.anterior
                    self.__total_elementos -=1
            atual = atual.proxima


    def remover_fim(self):
        if self.__total_elementos == 1:
            self.remover_comeco() 
        else: 
            self.__ultima = self.__ultima.anterior
            self.__ultima.proxima = None
            self.__total_elementos -= 1


    # retorno padrão da classe
    def __str__(self):
        if self.__total_elementos == 0:
            return '[] '
        string_final = '['
        atual = self.__primeira
        for _ in range(0, self.__total_elementos-1):
            string_final = string_final + atual.elemento + ', '
            atual = atual.proxima
        self.__ultima = atual
        self.__ultima.proxima = None
        string_final = string_final + f'{atual.elemento}]'
        return string_final