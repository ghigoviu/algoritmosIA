from Nodo import Nodo

#Algoritmos de busqueda
def busqueda(valor, tipo=1, lado=1, limite=1000):
    pila = []
    pila.append(raiz)
    print("Ruta: ")
    while(pila):
        if tipo == 1:
            nodo = pila.pop() #Busqueda en profundidad
        else:
            nodo = pila.pop(0) #Busqueda en anchura
        print(nodo.valor, end=", ")
        if nodo.nivel+2 > limite : # Busqueda limitada
            print("\nLimite alcanzado")
            flag=0
            break
        elif nodo.valor==valorBuscado: #Profundidad limitada
            print("\nNodo encontrado: ", nodo.valor)
            flag=1
            break
        else:
            if(ladoBusqueda == 1): #Por la derecha
                for value in reversed(nodo.adyacencias):
                    pila.append (value)
            elif (ladoBusqueda == 2): # Por la izquierda
                for value in nodo.adyacencias:
                    pila.append (value)
    if(flag==0):
        print("nodo no encontrado ")


def iterada(raiz, limite, ladoBusqueda, valorBuscado):
    nodo = []
    pila = []
    pila.append(raiz)
    while(pila):
        nodo = pila.pop(0)
        if(nodo.nivel<=limite):
            print("Nodo:", nodo.valor, end=" ")
            print("Nivel: ",nodo.nivel)
            if (nodo.valor==valorBuscado):
                print("Nodo encontrado: ", nodo.valor,"En el nivel: ",nodo.nivel)
                return True
                break
            else:
                if(ladoBusqueda == 1):
                    for value in reversed(nodo.adyacencias):
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in nodo.adyacencias:
                        pila.append (value)
    return False


raiz = Nodo("Arad",0)
raiz.adyacencias.append(Nodo("Timisura",1))  #0
raiz.adyacencias.append(Nodo("Sibiu",1)) #1
raiz.adyacencias.append(Nodo("Zerind",1)) #2
#adyacencias de Timisura
raiz.adyacencias[0].adyacencias.append(Nodo("Lugoj",2))#0
#adyacencias de Sibiu
raiz.adyacencias[1].adyacencias.append(Nodo("Rimnicu",2))#0
raiz.adyacencias[1].adyacencias.append(Nodo("Fagaras",2))#1
#adyacencias de Zerind
raiz.adyacencias[2].adyacencias.append(Nodo("Oradea",2))#0
#adyacencias de Lugoj
raiz.adyacencias[0].adyacencias[0].adyacencias.append(Nodo("Mehadia", 3)) #0
#adyacencias de Rimnicu
raiz.adyacencias[1].adyacencias[0].adyacencias.append(Nodo("Craiova", 3)) #0
raiz.adyacencias[1].adyacencias[0].adyacencias.append(Nodo("Pitesti", 3)) #1
#adyacencias de Fagaras
raiz.adyacencias[1].adyacencias[1].adyacencias.append(Nodo("Bucharest",3)) #1
#adyacencias de Oradea
raiz.adyacencias[2].adyacencias[0].adyacencias.append(Nodo("Sibiu", 3)) #0
#adyacencias de Mehadia
raiz.adyacencias[0].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("Dobreta", 4)) #0
#adyacencias de Pitesti
raiz.adyacencias[1].adyacencias[0].adyacencias[1].adyacencias.append(Nodo("Bucharest", 4)) #0
#adyacencias de Sibiu
raiz.adyacencias[2].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("Rimnicu", 4)) #0
raiz.adyacencias[2].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("Fagaras", 4)) #1
#adyacencias de Dobreta
raiz.adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("Craiova", 5)) #0


tipoBusqueda = 0
ladoBusqueda = 0
flag = 0
limite = -1

pila = []
nodo = []
valorBuscado = ""

print("Bienvenido al programa #2")
ans = 1
while(ans==1):
    tipoBusqueda = int(input("¿Qué tipo de busqueda desea hacer?\n 1 = Profundidad\n 2 = Anchura\n 3 = Anchura limitada\n 4 = Anchura iterativa \n"))
    ladoBusqueda = int(input("¿Por qué lado desea realizarla?\n 1 = Izquierda\n 2 = Derecha \n"))
    valorBuscado = input("Ingrese valor a buscar? ")
    if tipoBusqueda < 3:
        busqueda(valorBuscado, tipo=tipoBusqueda, lado=ladoBusqueda)
    elif tipoBusqueda == 4:
        limite = 1000
        while((limite > 6) or (limite < 0)):
            limite = int(input("Ingrese numero de iteraciones: "))
            if((limite > 6) or (limite < 0)):
                print("Ingrese una iteración valida")
        for iteracion in range(limite):
            print("Profundidad= ", iteracion-1)
            if(iterada(raiz,(iteracion+1),ladoBusqueda,valorBuscado)):
                print("Nodo encontrado")
                break
            else:
                print("Valor no encontrado")
    elif tipoBusqueda == 3:
        lim = int(input("Ingrese limite"))
        busqueda(valorBuscado, tipo=2, lado=ladoBusqueda, limite=lim)

    ans=int(input("Volver a empezar? 1=SI, 2=No"))
