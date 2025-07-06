import sys
import os
import subprocess
import Jetson.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

IRCinta = 31 

GPIO.setup(IRCinta, GPIO.IN)

estado_IR = GPIO.input(IRCinta)

IRCarril = 32 

GPIO.setup(IRCarril, GPIO.IN)

estado_IRCarril = GPIO.input(IRCarril)


if(estado_IR == 1):
    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/SinCinta.wav"])
    print("negativo")

if(estado_IRCarril == 1):
    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/SinPosicion.wav"])
    print("negativo")

if(estado_IR == 0 and estado_IRCarril == 0):
    print("correcto")



