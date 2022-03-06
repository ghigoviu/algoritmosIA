class Node:
    def __init__(self,datos,nivel,fvalores):
        
        self.datos = datos
        self.nivel = nivel
        self.fvalores = fvalores

    def hijo(self):
        
        x,y = self.find(self.datos,'_')
        
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.BuscarResultado(self.datos,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.nivel+1,0)
                children.append(child_node)
        return children
        
    def BuscarResultado(self,puz,x1,y1,x2,y2):
        
        if x2 >= 0 and x2 < len(self.datos) and y2 >= 0 and y2 < len(self.datos):
            temp_puzle = []
            temp_puzle = self.matriz(puz)
            temp = temp_puzle[x2][y2]
            temp_puzle[x2][y2] = temp_puzle[x1][y1]
            temp_puzle[x1][y1] = temp
            return temp_puzle
        else:
            return None
            

    def matriz(self,root):
        
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        
        for i in range(0,len(self.datos)):
            for j in range(0,len(self.datos)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        
        self.n = size
        self.abrir = []
        self.cerrar = []

    def acpt(self):
        
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,iniciar,goal):
        
        return self.h(iniciar.datos,goal)+iniciar.nivel

    def h(self,iniciar,goal): 
        
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if iniciar[i][j] != goal[i][j] and iniciar[i][j] != '_':
                    temp += 1
        return temp
        

    def ingresardat(self):
        cont=0
        print("Instrucciones: para ingresar un espacio en blanco se debera ingresar un _")
        print("Por ejemplo \n 1 2 3 \n 4 _ 6 \n 7 5 8")
        print("\n Ahora escriba su matriz \n")
        iniciar = self.acpt()
        print("Ingrese la matriz en el estado final \n")        
        goal = self.acpt()

        iniciar = Node(iniciar,0,0)
        iniciar.fvalores = self.f(iniciar,goal)

        self.abrir.append(iniciar)
        print("\n\n")
        while True:
            cont = cont + 1
            cur = self.abrir[0]
            print("***********")
            print("iterado",cont)
            print("***********\n")
            for i in cur.datos:
                for j in i:
                    print(j,end=" ")
                print("")
            if(self.h(cur.datos,goal) == 0):
                break
            for i in cur.hijo():
                i.fvalores = self.f(i,goal)
                self.abrir.append(i)
            self.cerrar.append(cur)
            del self.abrir[0]

            self.abrir.sort(key = lambda x:x.fvalores,reverse=False)

tipoBusqueda=0

tipoBusqueda = int(input("Ingrese una opcion \n1.- Solucion puzzle utilizando heuristica de piezas mal colocadas \n2.- Solucion puzzle utilizando heuristica manhattan \n"))
if(tipoBusqueda==1):
    print("Solucion puzzle utilizando heuristica de piezas mal colocadas")
    puz = Puzzle(3)
    puz.ingresardat()
elif(tipoBusqueda==2):
    print("Solucion puzzle utilizando heuristica manhattan")


