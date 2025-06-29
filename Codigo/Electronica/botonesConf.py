import Jetson.GPIO as GPIO
import time

import sys
import os
import subprocess

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from Electronica.botones import *

botonImpresion = 29
botonIns = 26

GPIO.setup(botonImpresion, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botonIns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

""" while(GPIO.input(botonImpresion) == 1):
    estado_BotImp = GPIO.input(botonImpresion)
    #print("No presionado") """

def Confirmacion(channel):
    global presionado

    print("si")

    presionado = True
    return

def Negacion(channel):
    global presionado

    print("no")

    presionado = True
    return


GPIO.add_event_detect(botonImpresion, GPIO.FALLING, callback=Confirmacion, bouncetime=500)
GPIO.add_event_detect(botonIns, GPIO.FALLING, callback=Negacion, bouncetime=500)


while (not presionado):
    time.sleep(1)

