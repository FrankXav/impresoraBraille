from Electronica.carril import *

actuador = 18
GPIO.setup(actuador, GPIO.OUT, initial=0)

def impresionCaracter(arregloCaracter):

    print(arregloCaracter)

    for columna in range(2):
        for fila in range(3):

            print("valor: " + str(arregloCaracter[columna][fila]) + " columna: " + str(columna) + " fila: " + str(fila))

            if(arregloCaracter[columna][fila] == 1):
                print("Activar actuador")
                GPIO.output(actuador, GPIO.HIGH)
                time.sleep(1.5)
                GPIO.output(actuador, GPIO.LOW)

            if(columna == 0 and fila !=2):
                print("Mover derecha")
                mover1mmDerecha()

            if(columna == 1 and fila !=2):
                print("Mover Izquierda")
                mover1mmIzquierda()
