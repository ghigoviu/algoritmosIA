import Arbol
from Nodo import Nodo
from Arbol import Arbol

if __name__ == '__main__':
    print("Bienvenido")
    listaNodos = []
    i = 2
    BaP = "BCDEFGHIJKLMNOP"
    for letra in BaP:
        listaNodos.append(Nodo(i, letra))
        i+=1
    for nodo in listaNodos:
        print(nodo)
    #Problema 1
    raiz = Nodo(1,'A')
    #Agregando nodos
    copiaNodos = listaNodos[:]
    listaNodos[12].__add__(listaNodos[14]) #Nodo P a nodo N
    listaNodos[13].__add__(copiaNodos[14]) #Nodo P a nodo O
    listaNodos[11].__add__(listaNodos[12], listaNodos[13]) #Nodo N y O a nodo M
    listaNodos[8].__add__(listaNodos[10], listaNodos[11]) #Nodo L y M a nodo J
    listaNodos[6].__add__(listaNodos[8], listaNodos[9]) #Nodo J y K a nodo H
    #Ahora debemos copiar todos los datos del nodo J y K al nodo H
    copiaNodoJ, copiaNodoK = listaNodos[8:10]
    listaNodos[7].__add__(copiaNodoJ, copiaNodoK)

    #listaNodos[7].__add__(listaNodos[8], listaNodos[9]) #Nodo J y K a nodo I
    listaNodos[4].__add__(listaNodos[6]) #Nodo H a nodo F
    listaNodos[5].__add__(listaNodos[7]) #Nodo I a nodo G
    listaNodos[3].__add__(listaNodos[4], listaNodos[5]) #Nodo F y G a nodo E
    listaNodos[0].__add__(listaNodos[2], listaNodos[3]) #Nodo D y E a nodo B
    raiz.__add__(listaNodos[0], listaNodos[1]) #Nodo B y C a nodo raiz
    problema2_raiz = Nodo()
    problema3_raiz = Nodo()


    ##Creando nodos de nuevo
    raiz = Nodo(1, "A")
    nodoB = Nodo(2, "B")
    nodoC = Nodo(3, "C")
    nodoD = Nodo(4, "D")
    nodoE = Nodo(5, "E")
    nodoF = Nodo(6, "F")
    nodoG = Nodo(7, "G")
    nodoH = Nodo(8, "H")
    nodoI = Nodo(9, "I")
    nodoJ = Nodo(10, "J")
    nodoK = Nodo(11, "K")
    nodoL = Nodo(12, "L")
    nodoM = Nodo(13, "M")
    nodoN = Nodo(14, "N")
    nodoO = Nodo(15, "O")
    nodoP = Nodo(15, "P")

    raiz.__add__(nodoB, nodoC)
    nodoB.__add__(nodoD, nodoE)
    nodoE.__add__(nodoF, nodoG)
    nodoF.__add__(nodoH)
    nodoG.__add__(nodoI)


    print("Imprimiendo lista de nodos")
    for nodo in raiz.adyacentes:
        print(nodo)

    arbol1 = Arbol(raiz)
    recorrido = arbol1.recorridoProfundidadD(raiz)
    print()
    for i in recorrido:
        print(i)

    recorrido = arbol1.recorridoProfundidadI(raiz)
    print()
    for i in recorrido:
        print(i)

    recorrido = arbol1.recorridoAnchuraD(raiz)
    print()
    for i in recorrido:
        print(i)

'''
Algoritmo de profundidad, utiliza una pila
def DFS(self, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while len(queue)>0:
        vert = queue.pop () # Esto muestra una pila, el último en entrar es el primero en salir
        nodes = vert.adyacencia
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)

        print(vert)
DFS(graph,'A')

*** --- *** --- *** --- *** --- *** --- ***

Algoritmo en anchura, requiere una cola
def BFS(graph,start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while len(queue)>0:
                 vert = queue.pop (0) # Esto muestra una cola, primero en entrar primero en salir
        nodes = graph[vert]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)

        print(vert)


BFS(graph,'D')

'''
