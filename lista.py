from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque()

    def insere(self, dado):
        self.fila.append(dado)

    def remove(self):
        
        if not self.vazia():
            return self.fila.popleft()
        return None

    def vazia(self):
        return len(self.fila) == 0

class Deque:
    def __init__(self):
        self.deque = deque()

    def insere_inicio(self, dado):
        self.deque.appendleft(dado)

    def insere_final(self, dado):
        self.deque.append(dado)

    def remove_inicio(self):
        if not self.vazia():
            return self.deque.popleft()
        return None

    def remove_final(self):
        if not self.vazia():
            return self.deque.pop()
        return None

    def vazia(self):
        return len(self.deque) == 0

class Pilha:
    def __init__(self):
        self.pilha = []

    def insere(self, dado):
        self.pilha.append(dado)

    def remove(self):
        if not self.vazia():
            return self.pilha.pop()
        return None

    def vazia(self):
        return len(self.pilha) == 0