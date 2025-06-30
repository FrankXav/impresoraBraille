import Jetson.GPIO as GPIO
import time

def Restaurarpines():

    print("Restaturando pines")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    #Carril

    Q1 = 7
    Q2 = 11
    Q3 = 13
    Q4 = 12

    GPIO.setup(Q1, GPIO.OUT, initial=0)
    GPIO.setup(Q2, GPIO.OUT, initial=0)
    GPIO.setup(Q3, GPIO.OUT, initial=0)
    GPIO.setup(Q4, GPIO.OUT, initial=0)

    GPIO.output(Q1, GPIO.LOW)
    GPIO.output(Q2, GPIO.LOW)
    GPIO.output(Q3, GPIO.LOW)
    GPIO.output(Q4, GPIO.LOW)

    #Avance

    C1 = 19
    C2 = 21
    C3 = 22
    C4 = 23

    GPIO.setup(C1, GPIO.OUT, initial=0)
    GPIO.setup(C2, GPIO.OUT, initial=0)
    GPIO.setup(C3, GPIO.OUT, initial=0)
    GPIO.setup(C4, GPIO.OUT, initial=0)

    GPIO.output(C1, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(C3, GPIO.LOW)
    GPIO.output(C4, GPIO.LOW)

    #actuador

    actuador = 18
    GPIO.setup(actuador, GPIO.OUT, initial=1)
    GPIO.output(actuador, GPIO.HIGH)