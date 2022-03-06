class nario:
    def __init__(self,valor,nivel): 
        self.valor = valor 
        self.hijos = []
        self.nivel = nivel

def iterada(raiz, limite, ladoBusqueda, valorBuscado):
    nodo = []
    pila = [] 
    pila.append(raiz)  
    while(pila): 
        nodo = pila.pop(0)
        if(nodo.nivel<=limite): 
            print("Ruta: ", nodo.valor)
            print("Nivel: ",nodo.nivel)
            if (nodo.valor==valorBuscado): 
                print("Nodo encontrado: ", nodo.valor,"En el nivel: ",nodo.nivel)
                flag=1
                return True 
                break  
            else:
                if(ladoBusqueda == 1):
                    for value in nodo.hijos: 
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in reversed(nodo.hijos): 
                        pila.append (value)
    return False

#Arbol segundo problema
raiz = nario("Arad",0)
#hijos de arad
raiz.hijos.append(nario("Timisura",1))#0
raiz.hijos.append(nario("Sibiu",1))#1
raiz.hijos.append(nario("Zerind",1))#2
#hijos timisura
raiz.hijos[0].hijos.append(nario("Lugoj",2))#0
#hijos de sibiu
raiz.hijos[1].hijos.append(nario("Rimnicu",2))#0
raiz.hijos[1].hijos.append(nario("Fagaras",2))#1
#hijos de zerind
raiz.hijos[2].hijos.append(nario("Oradea",2))#0
#hijos de lugoj
raiz.hijos[0].hijos[0].hijos.append(nario("Mehadia",3))#0
#hijos de rimnicu
raiz.hijos[1].hijos[0].hijos.append(nario("Craiova",3))#0
raiz.hijos[1].hijos[0].hijos.append(nario("Pitesti",3))#1
#hijos de fagaras
raiz.hijos[1].hijos[1].hijos.append(nario("Bucharest",3))#0
#hijos de oradea
raiz.hijos[2].hijos[0].hijos.append(nario("Sibiu",3))#0
#hijos mehadia
raiz.hijos[0].hijos[0].hijos[0].hijos.append(nario("Dobreta",4))#0
#hijos de pitesti
raiz.hijos[1].hijos[0].hijos[1].hijos.append(nario("Bucharest",4))#0
#hijos de sibiu
raiz.hijos[2].hijos[0].hijos[0].hijos.append(nario("Rimnicu",4))#0
raiz.hijos[2].hijos[0].hijos[0].hijos.append(nario("Fagaras",4))#1
#hijos de dobreta
raiz.hijos[0].hijos[0].hijos[0].hijos[0].hijos.append(nario("Craiova",5))#0
tipoBusqueda = 0
ladoBusqueda = 0
flag = 0
limite = -1

pila = [] 
nodo = [] 
valorBuscado = "" 

print("Bienvenido al programa #1")
tipoBusqueda = int(input("¿Qué tipo de busqueda deseas hacer?\n 1 = Profundidad\n 2 = Anchura\n 3 = Anchura limitada\n 4 = Anchura iterativa \n"))
ladoBusqueda = int(input("¿Por qué lado deseas realizarla?\n 1 = Izquierda\n 2 = Derecha \n"))

if(tipoBusqueda == 1):
    valorBuscado = input("¿Qué valor deseas buscar? ")
    pila.append(raiz) 
    while(pila): 
        nodo = pila.pop() 
        print("Ruta: ", nodo.valor) 
        if (nodo.valor==valorBuscado): 
            print("Nodo encontrado: ", nodo.valor)
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
        print("Valor no encontrado :(")
elif(tipoBusqueda == 2):
    valorBuscado = input("¿Qué valor deseas buscar? ")
    pila.append(raiz) 
    while(pila): 
        nodo = pila.pop(0) 
        print("Ruta: ", nodo.valor) 
        if (nodo.valor==valorBuscado): 
            print("Nodo encontrado: ", nodo.valor)
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
        print("Valor no encontrado :(")
elif(tipoBusqueda == 3):
    valorBuscado = input("¿Qué valor deseas buscar? ")
    while((limite > 5) or (limite < 0)):
        limite = int(input("¿Hasta que profundidad? (Max 5) "))
        if((limite > 5) or (limite < 0)):
            print("Ingrese un limite valido")
    pila.append(raiz) 
    while(pila):
        nodo = pila.pop(0)
        if(nodo.nivel<=limite): 
            print("Ruta: ", nodo.valor)
            print("Nivel: ",nodo.nivel)
            if (nodo.valor==valorBuscado): 
                print("Nodo encontrado: ", nodo.valor,"En el nivel: ",nodo.nivel)
                flag=1 
                break  
            else:
                if(ladoBusqueda == 1):
                    for value in nodo.hijos: 
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in reversed(nodo.hijos): 
                        pila.append (value)
    if(flag==0):
        print("Valor no encontrado :(")
elif(tipoBusqueda == 4):
    valorBuscado = input("¿Qué valor deseas buscar? ")
    while((limite > 6) or (limite < 0)):
        limite = int(input("¿Hasta que iteración deseas llegar? (Max 6) "))
        if((limite > 6) or (limite < 0)):
            print("Ingrese una iteración valida")
    
    for itera in range (limite):
        print("Profundidad = ",itera)
        if(iterada(raiz,(itera+1),ladoBusqueda,valorBuscado)):
            break         