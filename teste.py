class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None
        
class Lista:
    def __init__(self):
        self.inicio = None
        
    def inserir(self, dado):
        no = No(dado)
        no.proximo = self.inicio
        self.inicio = no
        
    def imprimir(self):
        comeco = self.inicio
        while comeco:
            print(comeco.dado)
            comeco = comeco.proximo
            
    def remover(self):
        primeiro = self.inicio
        self.inicio = primeiro.proximo
        
    def remover_dado(self, removido):
        atual = self.inicio
        anterior = None

        while atual:
            if atual.dado == removido:
                # Se for o primeiro elemento da lista
                if anterior is None:
                    self.inicio = atual.proximo
                # Se estiver no meio ou no fim
                else:
                    anterior.proximo = atual.proximo
                return True  # Encerra após remover a primeira ocorrência
            
            anterior = atual
            atual = atual.proximo
            
        return False  # Retorna False se o dado não existir na lista
            
lista = Lista()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
lista.imprimir()
lista.remover()
lista.remover_dado(2)
lista.imprimir()

class ListaCircular:
    def __init__(self):
        self.ultimo = None
        
    def inserir(self, dado):
        no = No(dado)
        if self.ultimo is None:
            no.proximo = no
            self.ultimo = no
        else:
            no.proximo = self.ultimo.proximo
            self.ultimo.proximo = no
            
    def remover_inicio(self):
        primeiro = self.ultimo.proximo
        self.ultimo.proximo = primeiro.proximo
        
        
    def imprimir(self):
        referencia = self.ultimo.proximo
        while referencia:
            print(referencia.dado)
            referencia = referencia.proximo
            if referencia == self.ultimo.proximo:
                break
            
lista = ListaCircular()
lista.inserir(1)
lista.inserir(2)
lista.inserir(3)
lista.inserir(4)
lista.imprimir()
lista.remover_inicio()
lista.imprimir()