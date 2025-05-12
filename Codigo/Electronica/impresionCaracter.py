from Electronica.carril import *

def impresionCaracter(arregloCaracter):

    print(arregloCaracter)

    for columna in range(2):
        for fila in range(3):

            print("valor: " + str(arregloCaracter[columna][fila]) + " columna: " + str(columna) + " fila: " + str(fila))

            if(columna == 0 and fila !=2):
                print("Mover derecha")

            if(columna == 2 and fila !=2):
                print("Mover Izquierda")
