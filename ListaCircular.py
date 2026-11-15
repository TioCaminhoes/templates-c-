class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class Lista:
    def __init__(self):
       self.ultimo = None
       self.tamanho = 0

    def insere(self, dado):
        no = No(dado)
        if self.ultimo is None:
            no.proximo = no
            self.ultimo = no
        else:
            no.proximo = self.ultimo.proximo
            self.ultimo.proximo = no
            self.ultimo = no
        self.tamanho += 1

    def obter_tamanho(self):
        return self.tamanho

    def vazia(self):
        return self.tamanho == 0

    def remove(self):
        if not self.vazia():
            self.ultimo.proximo = self.ultimo.proximo.proximo
            self.tamanho -= 1

lista = Lista()
lista.insere(1)
lista.insere(2)
lista.insere(3)
lista.insere(4)
print(f'Tamanho: {lista.obter_tamanho()}')