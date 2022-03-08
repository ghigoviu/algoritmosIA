class Nodo:
    def __init__(self,valor,nivel): 
        self.valor = valor 
        self.adyacencias = []
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

#Algoritmos de busqueda
def busqueda(valor, tipo=1, lado=1, limite=1000):
    pila.append(raiz) 
    print("Ruta: ")
    while(pila): 
        nodo = pila.pop() 
        print(nodo.valor, end=", ") 
        if nodo.nivel+2 > limite :
            print("/nLimite alcanzado")
            flag=0
            break
        elif nodo.valor==valorBuscado: 
            print("/nNodo encontrado: ", nodo.valor)
            flag=1 
            break 
        else:
            if(ladoBusqueda == 1):
                for value in reversed(nodo.adyacencias): 
                    pila.append (value) 
            elif (ladoBusqueda == 2):
                for value in nodo.adyacencias: 
                    pila.append (value)
    if(flag==0):
        print("nodo no encontrado ")


raiz = Nodo("A",0) 
raiz.adyacencias.append(Nodo("B",1))  #0 
raiz.adyacencias.append(Nodo ("C",1)) #1 
#adyacencias de B
raiz.adyacencias[0].adyacencias.append(Nodo("D",2))#0 
raiz.adyacencias[0].adyacencias.append (Nodo("E",2))#1 
#adyacencias de E
raiz.adyacencias[0].adyacencias[1].adyacencias.append(Nodo("F",3))#0 
raiz.adyacencias[0].adyacencias[1].adyacencias.append(Nodo("G",3))#1  
#adyacencias de F
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("H",4))#0
#adyacencias de G
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias.append(Nodo("I",4))#0
#adyacencias de H
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("J",5)) #0
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("K",5)) #1
#adyacencias de J
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("L", 6)) #0
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("M", 6)) #1
#adyacencias de M
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(Nodo("N", 7)) #0
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(Nodo("O", 7)) #1
#adyacencias en N
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("P", 8)) #0
#adyacencias en O
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[1].adyacencias.append(Nodo("P", 8)) #0
#adyacencias de I
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("J",5)) #0
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("K",5)) #1
#adyacencias de J
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("L", 6)) #0
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("M", 6)) #1
#adyacencias de M
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(Nodo("N", 7)) #0
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(Nodo("O", 7)) #1
#adyacencias en N
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("P", 8)) #0
#adyacencias en O
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[1].adyacencias.append(Nodo("P", 8)) #0

tipoBusqueda = 0
ladoBusqueda = 0
flag = 0
limite = -1

pila = []
nodo = []
valorBuscado = "" 

print("Bienvenido al programa #1")
ans = 1
while(ans==1):
    tipoBusqueda = int(input("¿Qué tipo de busqueda deseas hacer?\n 1 = Profundidad\n 2 = Anchura\n 3 = Profundida limitada\n 4 = Profundidad iterativa \n"))
    ladoBusqueda = int(input("¿Por qué lado deseas realizarla?\n 1 = Izquierda\n 2 = Derecha \n"))
    valorBuscado = input("¿Qué valor deseas buscar? ")
    if tipoBusqueda != 3:
        busqueda(valorBuscado, tipo=tipoBusqueda, lado=ladoBusqueda)
    elif tipoBusqueda == 4:
        print("Busqueda iterativa")
        while((limite > 6) or (limite < 0)):
            limite = int(input("¿Hasta que iteración deseas llegar? (Max 6) "))
            if((limite > 6) or (limite < 0)):
                print("Ingrese una iteración valida")
        
        for itera in range (limite):
            print("Profundidad = ",itera)
            if(iterada(raiz,(itera+1),ladoBusqueda,valorBuscado)):
                break    
    else:
        lim = int(input("¿Hasta que profundidad? (Max 7)"))
        busqueda(valorBuscado, lado=ladoBusqueda, limite=lim)
        
    ans=int(input("Volver a empezar? 1=SI, 2=No"))

    

'''
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
                for value in reversed(nodo.adyacencias): 
                    pila.append (value) 
            elif (ladoBusqueda == 2):
                for value in nodo.adyacencias: 
                    pila.append (value)
    if(flag==0):
        print("nodo no encontrado  ")
        
        
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
                for value in nodo.adyacencias: 
                    pila.append (value)
            elif (ladoBusqueda == 2):
                for value in reversed(nodo.adyacencias): 
                    pila.append (value)
    if(flag==0):
        print("nodo no encontrado  ")
        
        
        
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
                    for value in reversed(nodo.adyacencias): 
                        pila.append (value)
                elif (ladoBusqueda == 2):
                    for value in nodo.adyacencias: 
                        pila.append (value)
    if(flag==0):
        print("nodo no encontrado  ")
        
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
        
        '''
        