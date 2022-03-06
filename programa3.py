class arbol:
    def __init__(self,valor,nivel): 
        self.valor = valor 
        self.hijos = []
        self.nivel = nivel

def iterada(raiz, limite, ladoBusqueda, valorB):
    nodo = []
    pila = [] 
    pila.append(raiz)  
    while(pila): 
        nodo = pila.pop()
        if(nodo.nivel<=limite): 
            print("Ruta: \n", imprimir(nodo.valor))
            print("Nivel: ",nodo.nivel)
            if (nodo.valor==valorB): 
                print("Tablero (nodo) encontrado: \n", imprimir(nodo.valor),"En el nivel: ",nodo.nivel)
                flag=1
                return True 
                break  
            else:
                if(ladoBusqueda == 1):
                    for value in reversed(nodo.hijos): 
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in nodo.hijos: 
                        pila.append (value)  
    return False

def imprimir(valor):
    s = [[str(e) for e in row] for row in valor]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    return '\n'.join(table)

raiz=arbol([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]],0)
###limite 1
#hijos de 1
raiz.hijos.append(arbol([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0,0, 0, 0]], 1))
raiz.hijos.append(arbol([[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0,0, 0, 0]], 1))
raiz.hijos.append(arbol([[0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [0,0, 0, 0]], 1))
raiz.hijos.append(arbol([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1,0, 0, 0]], 1))
##limite 2
#hijos de 2
raiz.hijos[0].hijos.append(arbol([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0,0], [0, 0, 0, 0]], 2))
raiz.hijos[0].hijos.append(arbol([[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0,0], [0, 0, 0, 0]], 2))
#hijos de 3
raiz.hijos[1].hijos.append(arbol([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0,0], [0, 0, 0, 0]], 2))
raiz.hijos[1].hijos.append(arbol([[0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0,0], [0, 0, 0, 0]], 2))
#hijos de 4
raiz.hijos[2].hijos.append(arbol([[0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 0,0], [0, 0, 0, 0]], 2))
raiz.hijos[2].hijos.append(arbol([[0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 0,0], [0, 0, 0, 0]], 2))
#hijos de 5
raiz.hijos[3].hijos.append(arbol([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0,0], [1, 0, 0, 0]], 2))
raiz.hijos[3].hijos.append(arbol([[0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0,0], [1, 0, 0, 0]], 2))
##limite 3
#hijos de 6
raiz.hijos[0].hijos[0].hijos.append(arbol([[1, 0, 0, 0], [0, 1, 0, 0],[0, 0, 1, 0], [0, 0, 0, 0]], 3))
raiz.hijos[0].hijos[0].hijos.append(arbol([[1, 0, 0, 0], [0, 1, 0, 0],[0, 0, 0, 1], [0, 0, 0, 0]], 3))
#hijos de 7
raiz.hijos[0].hijos[1].hijos.append(arbol([[1, 0, 0, 0], [0, 0, 1, 0],[0, 0, 0, 1], [0, 0, 0, 0]], 3))
raiz.hijos[0].hijos[1].hijos.append(arbol([[1, 0, 0, 0], [0, 0, 1, 0],[0, 0, 0, 0], [0, 0, 0, 1]], 3))
#hijos de 8
raiz.hijos[1].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [1, 0, 0, 0],[0, 1, 0, 0], [0, 0, 0, 0]], 3))
raiz.hijos[1].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [1, 0, 0, 0],[0, 0, 1, 0], [0, 0, 0, 0]], 3))
#hijos de 9
raiz.hijos[1].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [1, 0, 0, 0],[0, 0, 1, 0], [0, 0, 0, 0]], 3))
raiz.hijos[1].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [1, 0, 0, 0],[0, 0, 0, 1], [0, 0, 0, 0]], 3))
#hijos de 10
raiz.hijos[2].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [0, 0, 1, 0],[1, 0, 0, 0], [0, 0, 0, 0]], 3))
raiz.hijos[2].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [0, 0, 0, 1],[1, 0, 0, 0], [0, 0, 0, 0]], 3))
#hijos de 11
raiz.hijos[2].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [0, 0, 1, 0],[1, 0, 0, 0], [0, 0, 0, 0]], 3))
raiz.hijos[2].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [0, 0, 0, 1],[1, 0, 0, 0], [0, 0, 0, 0]], 3))
#hijos de 12
raiz.hijos[3].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [0, 0, 0, 0],[0, 0, 1, 0], [1, 0, 0, 0]], 3))
raiz.hijos[3].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [0, 0, 0, 0],[0, 0, 0, 1], [1, 0, 0, 0]], 3))
#hijos de 13
raiz.hijos[3].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [0, 0, 0, 0],[1, 0, 0, 0], [1, 0, 0, 0]], 3))
raiz.hijos[3].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [0, 0, 0, 0],[0, 1, 0, 0], [1, 0, 0, 0]], 3))
##limite 4
#hijos de 14
raiz.hijos[0].hijos[0].hijos[0].hijos.append(arbol([[1, 0, 0, 0], [0,1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]], 4))
#hijos de 15
raiz.hijos[0].hijos[0].hijos[1].hijos.append(arbol([[1, 0, 0, 0], [0,1, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]], 4))
#hijos de 16
raiz.hijos[0].hijos[1].hijos[0].hijos.append(arbol([[1, 0, 0, 0], [0,0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]], 4))
#hijos de 17
raiz.hijos[0].hijos[1].hijos[1].hijos.append(arbol([[1, 0, 0, 0], [0,0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]], 4))
#hijos de 18
raiz.hijos[1].hijos[0].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [1,0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]], 4))
#hijos de 19
raiz.hijos[1].hijos[0].hijos[1].hijos.append(arbol([[0, 1, 0, 0], [1,0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4))
#hijos de 20
raiz.hijos[1].hijos[1].hijos[0].hijos.append(arbol([[0, 0, 1, 0], [1,0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0]], 4))
#hijos de 21
raiz.hijos[1].hijos[1].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [1,0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0]], 4))
#hijos de 22
raiz.hijos[2].hijos[0].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [0,0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 4))
#hijos de 23
raiz.hijos[2].hijos[0].hijos[1].hijos.append(arbol([[0, 1, 0, 0], [0,0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]], 4))#
#hijos de 24
raiz.hijos[2].hijos[1].hijos[0].hijos.append(arbol([[0, 0, 1, 0], [0,0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]], 4))
#hijos de 25
raiz.hijos[2].hijos[1].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [0,0, 0, 1], [1, 0, 0, 0],[0, 1, 0, 0]],4))
#hijos de 26
raiz.hijos[3].hijos[0].hijos[0].hijos.append(arbol([[0, 1, 0, 0], [0,0, 1, 0], [0, 0, 1, 0],[1, 0, 0, 0]],4))
#hijos de 27
raiz.hijos[3].hijos[0].hijos[1].hijos.append(arbol([[0, 1, 0, 0], [0,0, 1, 0], [0, 0, 0, 1],[1, 0, 0, 0]],4))
#hijos de 28
raiz.hijos[3].hijos[1].hijos[0].hijos.append(arbol([[0, 0, 1, 0], [0,1, 0, 0], [1, 0, 0, 0],[1, 0, 0, 0]],4))
#hijos de 29
raiz.hijos[3].hijos[1].hijos[1].hijos.append(arbol([[0, 0, 1, 0], [0,0, 0, 1], [0, 1, 0, 0],[1, 0, 0, 0]],4))

tipoBusqueda = 0
ladoBusqueda = 0
flag = 0
limite = -1

pila = [] 
nodo = [] 
valorBuscado = ""
ruta = ""
valorB = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],[0, 0, 0, 0]]

print("Bienvenido al programa de las 4 reinas")
tipoBusqueda = int(input("¿Qué tipo de busqueda deseas hacer?\n 1 = Profundidad\n 2 = Anchura\n 3 = Profundida limitada\n 4 = Profundidad iterativa \n"))
ladoBusqueda = int(input("¿Por qué lado deseas realizarla?\n 1 = Izquierda\n 2 = Derecha \n"))

if(tipoBusqueda == 1):
    for i in range(4):
        for j in range(4):
            valorB[i][j] = int(input("Ingresa las posiciones en el tablero: "))
    pila.append(raiz) 
    while(pila): 
        nodo = pila.pop() 
        print("Ruta: \n", imprimir(nodo.valor))
        if (nodo.valor==valorB): 
            print("Tablero (nodo) encontrado: \n", imprimir(nodo.valor))
            flag=1 
            break 
        else:
            if(ladoBusqueda == 1):
                for value in reversed(nodo.hijos): 
                    pila.append (value) 
            elif (ladoBusqueda == 2):
                for value in nodo.hijos: 
                    pila.append (value)
    if(flag==0):
        print("Tablero (nodo) encontrado :(")
elif(tipoBusqueda == 2):
    for i in range(4):
        for j in range(4):
            valorB[i][j] = int(input("Ingresa las posiciones en el tablero: "))
    pila.append(raiz) 
    while(pila): 
        nodo = pila.pop(0) 
        print("Ruta: \n", imprimir(nodo.valor)) 
        if (nodo.valor==valorB): 
            print("Tablero (nodo) encontrado: \n", imprimir(nodo.valor))
            flag = 1 
            break 
        else:
            if(ladoBusqueda == 1):
                for value in nodo.hijos: 
                    pila.append (value)
            elif (ladoBusqueda == 2):
                for value in reversed(nodo.hijos): 
                    pila.append (value)
    if(flag==0):
        print("Tablero (nodo) encontrado :(")
elif(tipoBusqueda == 3):
    for i in range(4):
        for j in range(4):
            valorB[i][j] = int(input("Ingresa las posiciones en el tablero: "))
    while((limite > 4) or (limite < 0)):
        limite = int(input("¿Hasta que profundidad? (Max 4) "))
        if((limite > 4) or (limite < 0)):
            print("Ingrese un limite valido")
    pila.append(raiz) 
    while(pila):
        nodo = pila.pop()
        if(nodo.nivel<=limite): 
            print("Ruta: \n", imprimir(nodo.valor))
            print("Nivel: ",nodo.nivel)
            if (nodo.valor==valorB): 
                print("Tablero (nodo) encontrado: \n", imprimir(nodo.valor))
                flag=1 
                break  
            else:
                if(ladoBusqueda == 1):
                    for value in reversed(nodo.hijos): 
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in nodo.hijos: 
                        pila.append (value)
    if(flag==0):
        print("Tablero (nodo) encontrado :(")
elif(tipoBusqueda == 4):
    for i in range(4):
        for j in range(4):
            valorB[i][j] = int(input("Ingresa las posiciones en el tablero: "))
    while((limite > 4) or (limite < 0)):
        limite = int(input("¿Hasta que iteración deseas llegar? (Max 4) "))
        if((limite > 4) or (limite < 0)):
            print("Ingrese una iteración valida")
    
    for itera in range (limite):
        print("Profundidad = ",itera)
        if(iterada(raiz,(itera+1),ladoBusqueda,valorB)):
            break