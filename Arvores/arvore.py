from no import No
class ArvoreBinariaBusca:
    def __init__(self):
        self.__raiz = None
        
    @property
    def raiz(self):
        return self.__raiz
        
    def inserir(self, label):
        no = No(label)
        print(no.label)
        if (self.__raiz is None):
            print('raiz')
            self.__raiz = no
        else:
            atual = self.__raiz
            while True:
                if(no.label < atual.label):
                    print('passei para a esquerda')
                    if(atual.esquerda is None):
                        atual.esquerda = no
                        print('parei')
                        break
                    else:
                        atual = atual.esquerda
                        print('o atual agora é',atual.label)
                        
                else:
                    print('passei para a direita')
                    if(atual.direita is None):
                        print('parei')
                        atual.direita = no
                        break
                    else:
                        atual = atual.direita
                        print('o atual agora é',atual.label)
        print('\n')
        
    def imprimir_pre(self,arvore):
        print(arvore.label)
        
        if arvore.esquerda is not None:
            self.imprimir_pre(arvore.esquerda)
              
        if arvore.direita is not None:
            self.imprimir_pre(arvore.direita)       
    
    
    def imprimir_ordem(self,arvore):
        if arvore.esquerda is not None:
            self.imprimir_ordem(arvore.esquerda)    
             
        print(arvore.label) 
         
        if arvore.direita is not None:
            # print(arvore.direita.label) 
            self.imprimir_ordem(arvore.direita)        
         
            
    def imprimir_pos(self,arvore):
        if arvore.esquerda is not None:
            self.imprimir_pos(arvore.esquerda)  

        if arvore.direita is not None:
            self.imprimir_pos(arvore.direita) 
        
        print(arvore.label)
           
    
    
                    
                        
                    
            
            