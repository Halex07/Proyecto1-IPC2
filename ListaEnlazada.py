class Nodo:
    def __init__(self, info=None, siguiente=None, id=None, anterior = None):
        self.id = id
        self.info = info
        self.siguiente = siguiente
        self.anterior = anterior


class ListaE:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.id = 0

    def insertar(self, info):
        if self.primero is None:
            self.primero = Nodo(info=info, id=self.id)
            self.ultimo = self.primero
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        self.id += 1
        actual.siguiente = Nodo(info=info, id=self.id)
        actual.siguiente.anterior = actual
        self.ultimo = actual.siguiente



class NodoInical:
    def __init__(self, id=None):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.inicio = None