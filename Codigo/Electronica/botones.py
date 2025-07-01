import Jetson.GPIO as GPIO
import time

import sys
import os
import subprocess

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from Electronica.carril import *
from Electronica.avanceCinta import *
from Electronica.inicializarPines import * 

botonImpresion = 29
botonIns = 26

GPIO.setup(botonImpresion, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(botonIns, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

presionado = False

ejeInstrucciones = False

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

def IniciarImpresion(channel):
    global presionado
    presionado = True
    return

def DecirInstructivo(channel):
    global ejeInstrucciones
    

    if( not ejeInstrucciones):
        ejeInstrucciones = True

        GPIO.remove_event_detect(botonIns)
        GPIO.remove_event_detect(botonImpresion)

        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/IntroduccionManual.wav"])
        time.sleep(1)
        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion1.wav"])
        contador = 0
        while(contador < 50):
            estado_BotImp = GPIO.input(botonIns)
            if(estado_BotImp == 0):
                subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion1Texto.wav"])
                contador = 500
            else:
                time.sleep(0.1)
                contador = contador + 1
        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion2.wav"])
        contador = 0
        while(contador < 50):
            estado_BotImp = GPIO.input(botonIns)
            if(estado_BotImp == 0):
                subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion2Texto.wav"])
                contador = 500
            else:
                time.sleep(0.1)
                contador = contador + 1

        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion3.wav"])
        contador = 0
        while(contador < 50):
            estado_BotImp = GPIO.input(botonIns)
            if(estado_BotImp == 0):
                subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion3Texto.wav"])
                contador = 500
            else:
                time.sleep(0.1)
                contador = contador + 1

        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion4.wav"])
        contador = 0
        while(contador < 50):
            estado_BotImp = GPIO.input(botonIns)
            if(estado_BotImp == 0):
                subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/Seccion4Texto.wav"])
                contador = 500
            else:
                time.sleep(0.1)
                contador = contador + 1

        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Manual/FinalManual.wav"])
        time.sleep(1)
        Restaurarpines()
        GPIO.add_event_detect(botonIns, GPIO.FALLING, callback=DecirInstructivo, bouncetime=500)
        GPIO.add_event_detect(botonImpresion, GPIO.FALLING, callback=IniciarImpresion, bouncetime=500)
        ejeInstrucciones = False
        


GPIO.add_event_detect(botonImpresion, GPIO.FALLING, callback=IniciarImpresion, bouncetime=500)
GPIO.add_event_detect(botonIns, GPIO.FALLING, callback=DecirInstructivo, bouncetime=500)


try:

    while (not presionado):
        time.sleep(0.5)
finally:

    print("Limpiando GPIO...")
    GPIO.cleanup()
    Restaurarpines()

