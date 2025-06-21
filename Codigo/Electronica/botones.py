import Jetson.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

botonImpresion = 26

botonIns = 29

GPIO.setup(botonImpresion, GPIO.IN)

estado_BotImp = GPIO.input(botonImpresion)

while(GPIO.input(botonImpresion) == 1):
    estado_BotImp = GPIO.input(botonImpresion)
    print("No presionado")

