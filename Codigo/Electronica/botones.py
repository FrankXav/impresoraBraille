import Jetson.GPIO as GPIO
import time

import sys
import os

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from Electronica.carril import *
from Electronica.avanceCinta import *

botonImpresion = 26

botonIns = 29

GPIO.setup(botonImpresion, GPIO.IN)

estado_BotImp = GPIO.input(botonImpresion)

GPIO.output(Q1, GPIO.LOW)
GPIO.output(Q2, GPIO.LOW)
GPIO.output(Q3, GPIO.LOW)
GPIO.output(Q4, GPIO.LOW)

GPIO.output(C1, GPIO.LOW)
GPIO.output(C2, GPIO.LOW)
GPIO.output(C3, GPIO.LOW)
GPIO.output(C4, GPIO.LOW)

while(GPIO.input(botonImpresion) == 1):
    estado_BotImp = GPIO.input(botonImpresion)
    #print("No presionado")

