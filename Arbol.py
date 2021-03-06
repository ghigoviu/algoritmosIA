#Clase Arbol, que tien un NOdo Raiz, nombre y funciones de recorrido en anchura y profundidad
class Arbol:
    name = ""

    def __init__(self, root, n="Arbol1"):
        self.raiz=root
        self.name=n

    def recorridoAnchura(self, buscado=0):
        if(buscado==0):
            print("Imrprimir todo el árbol")
        else:
            print("Impirminedo hasta encontrar elemento buscado")

    def recorridoProfundidadD(self, start):
        print("Iniciando recorrido en profundidad por la derecha")
        queue = []
        queue.append(start)
        seen = set()
        seen.add(start)
        while len(queue)>0:
            vert = queue.pop() # Esto muestra una pila, el último en entrar es el primero en salir
            nodes = vert.adyacentes
            for w in nodes:
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
            print(vert)
        return seen

    def recorridoProfundidadI(self, start):
        print("Iniciando recorrido en profundidad por la izquierda")
        queue = []
        queue.append(start)
        seen = set()
        seen.add(start)
        while len(queue)>0:
            vert = queue.pop() # Esto muestra una pila, el último en entrar es el primero en salir
            nodes = vert.adyacentes
            for w in reversed(nodes):
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
            print(vert)
        return seen

    def recorridoAnchuraD(self, start):
        print("Iniciando recorrido en anchura por la izquierda")
        queue = []
        queue.append(start)
        seen = set()
        seen.add(start)
        while len(queue)>0:
            vert = queue.pop(0) # Esto muestra una pila, el último en entrar es el primero en salir
            nodes = vert.adyacentes
            for w in nodes:
                if w not in seen:
                    queue.append(w)
                    seen.add(w)
            print(vert)
        return seen


