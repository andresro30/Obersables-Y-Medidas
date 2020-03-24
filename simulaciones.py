from calculadora import *



""" Punto 4.4.2 """
def canicasBooleanas(estado,canicas,clicks):
    for i in range(clicks):
        estado = productoVectorMatrizReal(estado,canicas)
    return estado

"""
def main():
main()
"""
