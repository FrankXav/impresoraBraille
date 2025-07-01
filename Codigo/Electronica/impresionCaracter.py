import Jetson.GPIO as GPIO
import time

from Electronica.carril import *
from Electronica.avanceCinta import *

actuador = 18
GPIO.setup(actuador, GPIO.OUT, initial=1)

def impresionCaracter(arregloCaracter):

    print(arregloCaracter)

    for columna in range(2):
        for fila in range(3):

            #Invertir simpresion segunda columna
            if(columna == 0):
                posFila = 2 - fila
            else: 
                posFila = fila

            print("valor: " + str(arregloCaracter[columna][posFila]) + " columna: " + str(columna) + " fila: " + str(posFila) + " valor: " + str(arregloCaracter[columna][posFila]))

            if(arregloCaracter[columna][posFila] == 1):
                #print("Activar actuador")
                GPIO.output(actuador, GPIO.LOW)
                GPIO.output(Q1, GPIO.LOW)
                GPIO.output(Q2, GPIO.LOW)
                GPIO.output(Q3, GPIO.LOW)
                GPIO.output(Q4, GPIO.LOW)
                time.sleep(0.1)
                GPIO.output(actuador, GPIO.HIGH)
                time.sleep(0.2)

            if(columna == 0 and posFila != 0):
                print("Mover Izquierda")
                mover1mmIzquierda()
                mover1mmIzquierda()
                mover1mmIzquierda()
                mover1mmIzquierda()
                mover1mmIzquierda()
                mover1mmIzquierda()
                

            if(columna == 1 and posFila != 2):
                print("Mover derecha")
                mover1mmDerecha()
                mover1mmDerecha()
                mover1mmDerecha()
                mover1mmDerecha()
                mover1mmDerecha()
                mover1mmDerecha()
            
            GPIO.output(Q1, GPIO.LOW)
            GPIO.output(Q2, GPIO.LOW)
            GPIO.output(Q3, GPIO.LOW)
            GPIO.output(Q4, GPIO.LOW)

            time.sleep(0.2)

        mover1mmDerechaAvance()
    
        GPIO.output(C1, GPIO.LOW)
        GPIO.output(C2, GPIO.LOW)
        GPIO.output(C3, GPIO.LOW)
        GPIO.output(C4, GPIO.LOW)
        
        time.sleep(0.2)

    mover1mmDerechaAvance()

    GPIO.output(C1, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(C3, GPIO.LOW)
    GPIO.output(C4, GPIO.LOW)

    time.sleep(0.2)
                
                
