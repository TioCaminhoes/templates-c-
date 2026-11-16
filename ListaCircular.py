class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class ListaCircular:
    def __init__(self):
        self.ultimo = None      # a única etiqueta que a lista guarda
        self.tamanho = 0

    def inserir_inicio(self, dado):
        no = No(dado)
        if self.ultimo is None:             # lista vazia
            no.proximo = no                 # aponta para si mesmo
            self.ultimo = no
        else:
            no.proximo = self.ultimo.proximo    # o novo aponta para o antigo primeiro
            self.ultimo.proximo = no            # o último aponta para o novo
        self.tamanho += 1

    def inserir_fim(self, dado):
        self.inserir_inicio(dado)           # insere do mesmo jeito...
        self.ultimo = self.ultimo.proximo   # ...e o novo vira o último

    def imprimir(self):
        if self.ultimo is None:
            print("(vazia)")
            return
        primeiro = self.ultimo.proximo
        atual = primeiro
        while True:
            print(atual.dado)
            atual = atual.proximo
            if atual is primeiro:           # voltou ao começo: para
                break
    def remover_inicio(self):
        if self.ultimo is None:             # lista vazia
            return None
        primeiro = self.ultimo.proximo
        if primeiro is self.ultimo:        # apenas um elemento
            self.ultimo = None
        else:
            self.ultimo.proximo = primeiro.proximo  # o último aponta para o segundo
        self.tamanho -= 1
        return primeiro.dado

    def remover_fim(self):
        if self.ultimo is None:             # lista vazia
            return None
        ultimo = self.ultimo
        if ultimo is self.ultimo.proximo:   # apenas um elemento
            self.ultimo = None
        else:
            atual = self.ultimo.proximo
            while atual.proximo is not self.ultimo:
                atual = atual.proximo
            atual.proximo = self.ultimo.proximo  # o penúltimo aponta para o primeiro
            self.ultimo = atual
        self.tamanho -= 1
        return ultimo.dado

    def imprimir_invertido(self):
        if self.ultimo is None:
            print("(vazia)")
            return
        atual = self.ultimo
        while True:
            print(atual.dado)
            # Encontrar o nó anterior ao atual
            anterior = self.ultimo
            while anterior.proximo is not atual:
                anterior = anterior.proximo
            atual = anterior
            if atual is self.ultimo:  # voltou ao último: para
                break

lista_circular = ListaCircular()
lista_circular.inserir_fim(1)
lista_circular.inserir_fim(2)
lista_circular.inserir_fim(3)
lista_circular.inserir_fim(4)
lista_circular.imprimir()
lista_circular.remover_fim()
lista_circular.imprimir()
lista_circular.imprimir_invertido()