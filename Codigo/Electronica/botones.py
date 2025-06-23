import Jetson.GPIO as GPIO
import time

import sys
import os
import subprocess

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from Electronica.carril import *
from Electronica.avanceCinta import *

botonImpresion = 26
botonIns = 29

GPIO.setup(botonImpresion, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botonIns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

presionado = False

GPIO.output(Q1, GPIO.LOW)
GPIO.output(Q2, GPIO.LOW)
GPIO.output(Q3, GPIO.LOW)   
GPIO.output(Q4, GPIO.LOW)

GPIO.output(C1, GPIO.LOW)
GPIO.output(C2, GPIO.LOW)
GPIO.output(C3, GPIO.LOW)
GPIO.output(C4, GPIO.LOW)

""" while(GPIO.input(botonImpresion) == 1):
    estado_BotImp = GPIO.input(botonImpresion)
    #print("No presionado") """

def IniciarImpresion():
    presionado = True

def DecirInstructivo():
    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Seccion1.wav"])
    time.sleep(1)
    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/listapalabras.wav"])
    time.sleep(1)
    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Seccion2.wav"])
    time.sleep(1)
    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/FinalInst.wav"])

GPIO.add_event_detect(botonImpresion, GPIO.RISING, callback=IniciarImpresion, bouncetime=300)
GPIO.add_event_detect(botonIns, GPIO.RISING, callback=DecirInstructivo, bouncetime=300)


while (not presionado):
    time.sleep(1)


