import sys
import os

from Electronica.avanceCinta import *

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

while(True):

    print("Mover derecha!")
    for i in range(10):
        mover1mmDerechaAvance()

    GPIO.output(C1, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(C3, GPIO.LOW)
    GPIO.output(C4, GPIO.LOW)

    time.sleep(2)

    print("Mover izquierda!")

    for i in range(10):
        mover1mmIzquierdaAvance()

    GPIO.output(C1, GPIO.LOW)
    GPIO.output(C2, GPIO.LOW)
    GPIO.output(C3, GPIO.LOW)
    GPIO.output(C4, GPIO.LOW)

    time.sleep(2)