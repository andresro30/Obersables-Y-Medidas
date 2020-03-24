from sys import stdin
import math
import unittest


""" Números complejos """

def suma(a,b):
    v1 = a[0]+b[0]
    v2 = a[1]+b[1]
    return (v1,v2)
    
def resta(a,b):
    v1 = a[0]-b[0]
    v2 = a[1]-b[1]
    return (v1,v2)

def multiplicacion(a,b):
    ent = []
    ima = []
    for i in range(len(a)):
        for j in range(len(b)):    
            if(i==0 and j==0):
                ent.append(a[i]*b[j])
            elif(i==0 and j==1):
                ima.append(a[i]*b[j])
            elif(i==1 and j==0):
                ima.append(a[i]*b[j])
            else:
                ent.append(-1*(a[i]*b[j]))
                
    v1 = ent[0]+ent[1]
    v2 = ima[0]+ima[1]
    return (v1,v2)

def division(a,b):
    z1 = a[0]*b[0] + a[1]*b[1]
    z2 = a[1]*b[0] - a[0]*b[1]
    z3 = b[0]**2 + b[1]**2

    v1 = z1/z3
    v2 = z2/z3
    return (v1,v2)

def modulo(a):
    temp = a[0]**2 + a[1]**2
    v1 = temp**(1/2)
    return (v1,"")

def conjugado(a):
    v1 = a[1]*-1    
    return (a[0],v1)

def polarCartesiano(a):
    #Los angulos estan en grados
    r = a[0]
    ang = radGrados(a[1])
    v1 = r*(math.cos(ang))
    v2 = r*(math.sin(ang))
    return (v1,v2)

def cartesianoPolar(a):
    v1 = (a[0]**2 + a[1]**2)**(1/2)
    v2 = gradRadi(math.atan2(a[1],abs(a[0])))
    return(v1,v2)

def fase(a):
    v1 = math.atan2(a[1],a[0])
    return (v1,"")

def norma(a):
    ans = a[0]**2 + a[1]**2
    return ans


""" Funciones de apoyo para operaciones con Vectores y matrices """


def verificarTipo(a,b):
    if(type(a)==tuple):
        return (a,b)
    else:
        return (b,a)

def diferenciaVectMatriz(a,b):
    if(type(a[0])==tuple):
        return (a,b)
    else:
        return (b,a)

def filtrar(a,b):
    if(type(a[0])==list and type(b[0])==list):
        return (a,b)
    elif(type(a[0])!=list and type(b[0])==list):
        return ([a],b)
    elif(type(a[0])==list and type(b[0])!=list):
        return (a,[b])


""" Operaciones con Vectores y Matrices complejas"""

def sumaVectores(a,b):
    ans = [0]*len(a)
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            ans[i] = suma(a[i],b[i])
        return ans

def restaVectores(a,b):
    ans = [0]*len(a)
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            ans[i] = resta(a[i],b[i])
        return ans

def inversaVector(a):
    ans = [0]*len(a)
    for i in range(len(a)):
        ans[i] = (-1*(a[i][0]),-1*(a[i][1]))
    return ans

def multiplicacionVectores(a,b):
    c = verificarTipo(a,b)[0]
    v = verificarTipo(a,b)[1]
    ans = [0]*len(v)
    for i in range(len(v)):
        ans[i] = multiplicacion(c,v[i])
    return ans

def sumaMatrices(a,b):
    ans = [0]*len(a)
    if(len(a)!=len(b)):
        return "Las dimensiones de los vectores no son iguales"
    else:
        for i in range(len(a)):
            if(len(a[i])!=len(b[i])):
               return "Las dimensiones de los vectores no son iguales"
            else:
                ans[i] = sumaVectores(a[i],b[i])
        return ans

def inversaMatriz(a):
    ans = [0]*len(a)
    for i in range(len(a)):
        ans[i] = inversaVector(a[i])
    return ans

def multiplicacionEscalarMatrices(a,b):
    c = verificarTipo(a,b)[0]
    m = verificarTipo(a,b)[1]
    ans = [0]*len(a)    
    for i in range(len(m)):
        ans[i] = multiplicacionVectores(c,m[i])
    return ans

def traspuesta(a):
    ans = []
    for i in range(len(a[0])):
        ans.append([])
        for j in range(len(a)):
            ans[i].append(a[j][i])
    return ans


def conjugadoVector(a):
    ans = [0]*len(a)
    for i in range(len(a)):
        ans[i] = conjugado(a[i])
    return ans 

def conjugadoMatriz(a):
    ans = []
    for i in range(len(a)):
        ans.append(conjugadoVector(a[i]))
    return ans
    

def matrizAdjunta(a):
    ans = traspuesta(a)
    ans = conjugadoMatriz(ans)
    return ans

""" Función que multiplica dos vectores y suma sus componentes,
    apoya la funcion de productoVectorMatriz"""

def multiVectores(a,b):
    ans = (0,0) 
    for i in range(len(a)):
        ans = suma(ans,multiplicacion(a[i],b[i]))
    return ans

def multiVectoresReales(a,b):
    ans = 0
    for i in range(len(a)):
        ans+=a[i]*b[i]
    return ans  


""" Funcion que multiplica dos matrices """
def productoMatrices(a,b):
    if(len(a[0])!=len(b)):
        return "Las dimensiones de las matrices no son correctas"
    else:
        ans = []
        for i in range(len(a)):
           fila = []
           for j in range(len(b[0])):
               temp = (0,0)
               for k in range(len(b)):
                   mult = multiplicacion(a[i][k],b[k][j])
                   temp = suma(mult,temp)
               fila.append(temp)
           ans.append(fila)
        return ans


def productoMatricesReales(a,b):
    if(len(a[0])!=len(b)):
        return "Las dimensiones de las matrices no son correctas"
    else:
        ans = []
        for i in range(len(a)):
           fila = []
           for j in range(len(b[0])):
               temp = 0
               for k in range(len(b)):
                   mult = a[i][k]*b[k][j]
                   temp+=mult
               fila.append(temp)
           ans.append(fila)
        return ans

def productoVectorMatriz(a,b):
    vec = diferenciaVectMatriz(a,b)[0]
    ma = diferenciaVectMatriz(a,b)[1]
    if(len(ma[0])!=len(vec)):
        return "Las dimension de la matriz o del vector es incorrecta"
    else:
        ans = []
        for i in range(len(ma)):
            ans.append(multiVectores(vec,ma[i]))
        return ans

def productoVectorMatrizReal(a,b):
    vec = a
    ma = b
    if(len(ma[0])!=len(vec)):
        return "Las dimension de la matriz o del vector es incorrecta"
    else:
        ans = []
        for i in range(len(ma)):
            ans.append(multiVectoresReales(vec,ma[i]))
        return ans


def productoInternoVectores(a,b):
    v1 = conjugadoVector(a)
    return multiVectores(v1,b)


def normaVector(a):
    norma = productoInternoVectores(a,a)
    return math.sqrt(norma[0])
    


def distanciaVectores(a,b):
    resta = restaVectores(a,b)
    return normaVector(resta)


def esUnitaria(a):
    adjunta = matrizAdjunta(a)
    ans = productoMatrices(a,adjunta)
    for i in range(len(a)):
        for j in range(len(a[0])):
            num = ans[i][j]
            if(i==j and (num[0]!=1 or num[1]!=0)):
                return False
            elif(i!=j and (num[0]!=0 or num[1]!=0)):
                 return False
    return True
                
    


def esHermitiana(a):
    adjunta = matrizAdjunta(a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]!=adjunta[i][j]):
                return False
    return True


def productoTensorVectores(a,b):
    ans = []
    for i in range(len(a)):
        for j in range(len(b)):
            ans.append(multiplicacion(a[i],b[j]))
    return ans 
    
   
def productoTensorMatrices(a,b):
    a = filtrar(a,b)[0]
    b = filtrar(a,b)[1]
    ans = []
    for i in range(len(a)):
        for j in range(len(b)):
            ans.append(productoTensorVectores(a[i],b[j]))
    return ans


def prettyPrinting(c):
    if(c[1]==""):
        print(round(c[0],2))
    else:
        if(c[0]!=0):
            print(round(c[0],2),end="")
            if(c[1]>=0):
                print(" +",str(round(c[1],2))+"i")
            else:
                print("",str(round(c[1],2))+"i")
        else:
            if(c[1]==1):
                print("i")
            else:
                print(str(round(c[1],2))+"i")

def radGrados(num):
    return (num/180)*math.pi

def gradRadi(num):
    return (num*180)/math.pi

""" Sistema Cuantico de una partícula"""

def probabilidad(pos,vector):
    a = norma(vector[pos])
    b = 0
    for i in range(len(vector)):
        b+= norma(vector[i])
    prob = (a/b)*100
    return prob

def amplitudTransicion(matriz,vector):
    a = productoVectorMatriz(vector,matriz)
    conjugado = conjugadoVector(a)
    ans = multiVectores(conjugado,vector)
    return ans 
    

"""
def main():
main()
"""

