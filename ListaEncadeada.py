class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def insere(self, dado):
        no = No(dado) ### Cria o no e coloca meu dado no nó
        no.proximo = self.inicio 
        self.inicio = no
        self.tamanho += 1

    def obter_tamanho(self):
        return self.tamanho

    def vazia(self):
        return self.inicio is None

    def remove(self):
        if not self.vazia():
            self.inicio = self.inicio.proximo
            self.tamanho -= 1

    def imprime(self):
        no = self.inicio
        while no:
            print(no.dado)
            no = no.proximo

lista = Lista()
lista.insere(1)
lista.insere(2)
lista.insere(3)
lista.insere(4)
print(f'Tamanho: {lista.obter_tamanho()}')
lista.imprime()