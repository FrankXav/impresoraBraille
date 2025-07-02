import sys
import os
import subprocess
import Jetson.GPIO as GPIO
import time

IRCinta = 31 

GPIO.setup(IRCinta, GPIO.IN)

estado_IR = GPIO.input(IRCinta)

IRCarril = 32 

GPIO.setup(IRCarril, GPIO.IN)

estado_IRCarril = GPIO.input(IRCarril)


if(estado_IR == 1):
    #TODO  No hay cita en el porta cinta
    print("negativo")

if(estado_IRCarril == 1):
    #TODO Audio no hay cinta en el carril o no esta acomodada
    print("negativo")

if(estado_IR == 0 and estado_IRCarril == 0):
    print("correcto")



