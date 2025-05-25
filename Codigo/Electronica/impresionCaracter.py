import Jetson.GPIO as GPIO
import time

from Electronica.carril import *

actuador = 18
GPIO.setup(actuador, GPIO.OUT, initial=1)

def impresionCaracter(arregloCaracter):

    print(arregloCaracter)

    for columna in range(2):
        for fila in range(3):

            print("valor: " + str(arregloCaracter[columna][fila]) + " columna: " + str(columna) + " fila: " + str(fila))

            if(arregloCaracter[columna][fila] == 1):
                #print("Activar actuador")
                """ GPIO.output(actuador, GPIO.LOW)
                GPIO.output(Q1, GPIO.LOW)
                GPIO.output(Q2, GPIO.LOW)
                GPIO.output(Q3, GPIO.LOW)
                GPIO.output(Q4, GPIO.LOW)
                time.sleep(0.3)
                GPIO.output(actuador, GPIO.HIGH) """

            if(columna == 0 and fila !=2):
                #print("Mover Izquierda")
                mover1mmIzquierda()
                mover1mmIzquierda()
                mover1mmIzquierda()
                time.sleep(2)

            if(columna == 1 and fila !=2):
                #print("Mover derecha")
                mover1mmDerecha()
                mover1mmDerecha()
                mover1mmDerecha()
                time.sleep(2)
                
