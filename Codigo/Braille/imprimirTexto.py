import sys
import os
import subprocess

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Braille.tansBraille import *
from Electronica.iniciarCarrail import *
from Electronica.impresionCaracter import *

texto = sys.argv[1]

IRCinta = 31 

GPIO.setup(IRCinta, GPIO.IN)

estado_IR = GPIO.input(IRCinta)

print("Estado estado_IR: " + str(estado_IR))

IRCarril = 32 

GPIO.setup(IRCarril, GPIO.IN)

estado_IRCarril = GPIO.input(IRCarril)

print("Estado IRCaril: " + str(estado_IRCarril))

if(estado_IR == 0 and estado_IRCarril == 0):

    print("Palabra a imprimir: " + str(texto))

    arregloPalabra = transcripcionBraille(texto)

    iniciarCarril()

    print("Posicion Inicial")

    print("Comenzar impresion!!!")

    for caracter in arregloPalabra:
        impresionCaracter(caracter)

    for i in range(30):
        #print("Mover Avance")
        mover1mmDerechaAvance()

    GPIO.output(C1, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(C3, GPIO.LOW)
    GPIO.output(C4, GPIO.LOW)

    GPIO.output(Q1, GPIO.LOW)
    GPIO.output(Q2, GPIO.LOW)
    GPIO.output(Q3, GPIO.LOW)
    GPIO.output(Q4, GPIO.LOW)

else: 
    print("No hay cinta")

    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/FinalEtiqueta.wav"])
