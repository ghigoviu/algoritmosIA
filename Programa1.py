class arbol:
    def __init__(self,valor,nivel): 
        self.valor = valor 
        self.hijos = []
        self.nivel = nivel

def iterada(raiz, limite, ladoBusqueda, valorBuscado):
    nodo = []
    pila = [] 
    pila.append(raiz)  
    while(pila): 
        nodo = pila.pop()
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
                    for value in reversed(nodo.hijos): 
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in nodo.hijos: 
                        pila.append (value)  
    return False

raiz = arbol("A",0) 
#hijos de A
raiz.hijos.append(arbol("C",1))  #0 
raiz.hijos.append(arbol ("B",1)) #1 
#hijos de C
raiz.hijos[0].hijos.append(arbol("D",2))#0 
raiz.hijos[0].hijos.append (arbol("E",2))#1 
#hijos de E
raiz.hijos[0].hijos[1].hijos.append(arbol("G",3))#0 
raiz.hijos[0].hijos[1].hijos.append(arbol("F",3))#1  
#hijos de G
raiz.hijos[0].hijos[1].hijos[0].hijos.append(arbol("I",4))#0
raiz.hijos[0].hijos[1].hijos[0].hijos.append(arbol("H",4))#1
#hijos de I
raiz.hijos[0].hijos[1].hijos[0].hijos[0].hijos.append(arbol("J",5))

tipoBusqueda = 0
ladoBusqueda = 0
flag = 0
limite = -1

pila = [] 
nodo = [] 
valorBuscado = "" 

print("Bienvenido al programa #1")
tipoBusqueda = int(input("¿Qué tipo de busqueda deseas hacer?\n 1 = Profundidad\n 2 = Anchura\n 3 = Profundida limitada\n 4 = Profundidad iterativa \n"))
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
        nodo = pila.pop()
        if(nodo.nivel<=limite): 
            print("Ruta: ", nodo.valor)
            print("Nivel: ",nodo.nivel)
            if (nodo.valor==valorBuscado): 
                print("Nodo encontrado: ", nodo.valor,"En el nivel: ",nodo.nivel)
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