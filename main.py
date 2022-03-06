from Nodo import Nodo

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
    listaNodos[12].__add__(listaNodos[14]) #Nodo P a nodo N
    listaNodos[13].__add__(listaNodos[14]) #Nodo P a nodo O
    listaNodos[11].__add__(listaNodos[12], listaNodos[13]) #Nodo N y O a nodo M
    listaNodos[8].__add__(listaNodos[10], listaNodos[11]) #Nodo L y M a nodo J
    listaNodos[6].__add__(listaNodos[8], listaNodos[9]) #Nodo J y K a nodo H
    listaNodos[7].__add__(listaNodos[8], listaNodos[9]) #Nodo J y K a nodo I
    listaNodos[4].__add__(listaNodos[6]) #Nodo H a nodo F
    listaNodos[5].__add__(listaNodos[7]) #Nodo I a nodo G
    listaNodos[3].__add__(listaNodos[4], listaNodos[5]) #Nodo F y G a nodo E
    listaNodos[0].__add__(listaNodos[2], listaNodos[3]) #Nodo D y E a nodo B
    raiz.__add__(listaNodos[0], listaNodos[1]) #Nodo B y C a nodo raiz
    problema2_raiz = Nodo()
    problema3_raiz = Nodo()

print("Imprimiendo lista de nodos")
for nodo in raiz.adyacentes:
    print(nodo)

'''
Algoritmo de profundidad, utiliza una pila
def DFS(graph,start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while len(queue)>0:
        vert = queue.pop () # Esto muestra una pila, el último en entrar es el primero en salir
        nodes = graph[vert]
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
