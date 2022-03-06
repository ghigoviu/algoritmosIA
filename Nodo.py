#Clase Nodo que contiene un ID, un dato y una lista de hijos

class Nodo:
    id = ""
    dato = ""
    adyacentes = []

    def __init__(self, i=0, d="empty"):
        self.dato=d
        self.id=i

    def getNodo(self):
        numNodos = len(self.adyacentes)
        print("Quedan", numNodos, "nodo(s) en este arbol sin recorrer")
        if numNodos < 1:
            return self.adyacentes.pop(0)

    def __add__(self, *nodos):
        for nodo in nodos:
            self.adyacentes.append(nodo)
        print(str(len(nodos)) + " nodos agregados")

    def agregarNodo(self, *nodos):
        self.adyacentes.append(nodos)
        print(str(len(nodos)), " nodos agregados")

    def __str__(self):
        return "ID="+str(self.id)+" Dato="+str(self.dato)

