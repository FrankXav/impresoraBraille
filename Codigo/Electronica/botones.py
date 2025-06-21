import Jetson.GPIO as GPIO
import time


botonImpresion = 26

GPIO.setup(botonImpresion, GPIO.IN)

estado_BotImp = GPIO.input(botonImpresion)

while(GPIO.input(botonImpresion) == 1):
    estado_BotImp = GPIO.input(botonImpresion)
    print("No presionado")

