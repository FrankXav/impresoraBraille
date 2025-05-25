import sys
import os

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Braille.tansBraille import *
from Electronica.iniciarCarrail import *
from Electronica.impresionCaracter import *

texto = sys.argv[1]

print("Palabra a imprimir: " + str(texto))

arregloPalabra = transcripcionBraille(texto)

iniciarCarril()

print("Posicion Inicial")
time.sleep(5)

print("Comenzar impresion!!!")

for caracter in arregloPalabra:
    impresionCaracter(caracter)

GPIO.output(Q1, GPIO.LOW)
GPIO.output(Q2, GPIO.LOW)
GPIO.output(Q3, GPIO.LOW)
GPIO.output(Q4, GPIO.LOW)

