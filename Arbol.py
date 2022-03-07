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

    def recorridoAnchura(self, start):
        print("Iniciando recorrido en anchura")
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


