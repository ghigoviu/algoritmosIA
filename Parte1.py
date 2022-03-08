from Nodo import Nodo

# Algoritmos de busqueda
def busqueda(valor, tipo=1, lado=1, limite=1000):
    pila = []
    pila.append(raiz)
    print("Ruta: ")
    while (pila):
        if tipo == 1:
            nodo = pila.pop()  # Busqueda en profundidad
        else:
            nodo = pila.pop(0)  # Busqueda en anchura
        print(nodo.valor, end=", ")
        if nodo.nivel + 2 > limite:
            print("\nLimite alcanzado")
            flag = 0
            break
        elif nodo.valor == valorBuscado:  # Profundidad limitada
            print("\nNodo encontrado: ", nodo.valor)
            flag = 1
            break
        else:
            if (lado == 1):  # Por la derecha
                for value in reversed(nodo.adyacencias):
                    pila.append(value)
            elif (lado == 2):  # Por la izquierda
                for value in nodo.adyacencias:
                    pila.append(value)
    if (flag == 0):
        print("nodo no encontrado ")


def iterada(raiz, limite, ladoBusqueda, valorBuscado):
    nodo = []
    pila = []
    pila.append(raiz)
    while (pila):
        nodo = pila.pop()
        if (nodo.nivel <= limite):
            print("Nodo:", nodo.valor, end=" ")
            print("Nivel: ", nodo.nivel)
            if (nodo.valor == valorBuscado):
                print("Nodo encontrado: ", nodo.valor, "En el nivel: ", nodo.nivel)
                return True
                break
            else:
                if (ladoBusqueda == 1):
                    for value in reversed(nodo.adyacencias):
                        pila.append(value)
                elif (ladoBusqueda == 2):
                    for value in nodo.adyacencias:
                        pila.append(value)
    return False


raiz = Nodo("A", 0)
raiz.adyacencias.append(Nodo("B", 1))  # 0
raiz.adyacencias.append(Nodo("C", 1))  # 1
# adyacencias de B
raiz.adyacencias[0].adyacencias.append(Nodo("D", 2))  # 0
raiz.adyacencias[0].adyacencias.append(Nodo("E", 2))  # 1
# adyacencias de E
raiz.adyacencias[0].adyacencias[1].adyacencias.append(Nodo("F", 3))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias.append(Nodo("G", 3))  # 1
# adyacencias de F
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("H", 4))  # 0
# adyacencias de G
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias.append(Nodo("I", 4))  # 0
# adyacencias de H
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("J", 5))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("K", 5))  # 1
# adyacencias de J
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("L", 6))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("M", 6))  # 1
# adyacencias de M
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(
    Nodo("N", 7))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(
    Nodo("O", 7))  # 1
# adyacencias en N
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[
    0].adyacencias.append(Nodo("P", 8))  # 0
# adyacencias en O
raiz.adyacencias[0].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[
    1].adyacencias.append(Nodo("P", 8))  # 0
# adyacencias de I
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("J", 5))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias.append(Nodo("K", 5))  # 1
# adyacencias de J
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("L", 6))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias.append(Nodo("M", 6))  # 1
# adyacencias de M
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(
    Nodo("N", 7))  # 0
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias.append(
    Nodo("O", 7))  # 1
# adyacencias en N
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[
    0].adyacencias.append(Nodo("P", 8))  # 0
# adyacencias en O
raiz.adyacencias[0].adyacencias[1].adyacencias[1].adyacencias[0].adyacencias[0].adyacencias[1].adyacencias[
    1].adyacencias.append(Nodo("P", 8))  # 0

tipoBusqueda = 0
ladoBusqueda = 0
flag = 0
limite = -1

pila = []
nodo = []
valorBuscado = ""


if __name__ == '__main__':
    print("Bienvenido al programa #1")
    ans = 1
    while (ans == 1):
        tipoBusqueda = int(input(
            "¿Qué tipo de busqueda desea hacer?\n 1 = Profundidad\n 2 = Anchura\n 3 = Profundida limitada\n 4 = Profundidad iterativa \n"))
        ladoBusqueda = int(input("¿Por qué lado desea realizarla?\n 1 = Izquierda\n 2 = Derecha \n"))
        valorBuscado = input("Ingrese valor a buscar? ")
        if tipoBusqueda < 3:
            busqueda(valorBuscado, tipo=tipoBusqueda, lado=ladoBusqueda)
        elif tipoBusqueda == 4:
            limite = 1000
            while ((limite > 6) or (limite < 0)):
                limite = int(input("Ingrese numero de iteraciones: "))
                if ((limite > 6) or (limite < 0)):
                    print("Ingrese una iteración valida")
            for iteracion in range(limite):
                print("Profundidad= ", iteracion - 1)
                if (iterada(raiz, (iteracion + 1), ladoBusqueda, valorBuscado)):
                    print("Nodo encontrado")
                    break
                else:
                    print("Valor no encontrado")
        elif tipoBusqueda == 3:
            lim = int(input("Ingrese limite"))
            busqueda(valorBuscado, lado=ladoBusqueda, limite=lim)

        ans = int(input("Volver a empezar? 1=SI, 2=No"))
