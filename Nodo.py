#Clase Nodo que contiene un ID, un dato y una lista de hijos

class Nodo:
    def __init__(self,valor,nivel):
        self.valor = valor
        self.adyacencias = []
        self.nivel = nivel