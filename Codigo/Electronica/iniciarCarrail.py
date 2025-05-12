import sys
import os

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

#sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Electronica.carril import *

IR = 16 

GPIO.setup(16, GPIO.IN)

estado_IR = GPIO.input(IR)

def iniciarCarril():

    print("Iniciamos la posicion del carril")

    if(estado_IR == 1):

        while(GPIO.input(IR) == 1):

            mover1mmDerecha()

        for i in range(5):
            mover1mmDerecha()

        while(GPIO.input(IR) == 0):

            mover1mmIzquierda()

    else:

        while(GPIO.input(IR) == 0):

            mover1mmIzquierda()

    GPIO.output(Q1, GPIO.LOW)
    GPIO.output(Q2, GPIO.LOW)
    GPIO.output(Q3, GPIO.LOW)
    GPIO.output(Q4, GPIO.LOW)