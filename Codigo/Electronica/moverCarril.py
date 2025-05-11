from carril import *

""" for i in range(200):
    mover1mmDerecha()


for i in range(200):
    mover1mmIzquierda()


for i in range(200):
    ejecutarCiclo(CW = True) 
    #time.sleep(0.1)
        
GPIO.output(Q1, GPIO.LOW)
GPIO.output(Q2, GPIO.LOW)
GPIO.output(Q3, GPIO.LOW)
GPIO.output(Q4, GPIO.LOW) """


while(True):

    print("Mover derecha!")
    for i in range(50):
        mover1mmDerecha()

    GPIO.output(Q1, GPIO.LOW)
    GPIO.output(Q2, GPIO.LOW)
    GPIO.output(Q3, GPIO.LOW)
    GPIO.output(Q4, GPIO.LOW)

    time.sleep(2)

    print("Mover izquierda!")

    for i in range(50):
        mover1mmIzquierda()

    GPIO.output(Q1, GPIO.LOW)
    GPIO.output(Q2, GPIO.LOW)
    GPIO.output(Q3, GPIO.LOW)
    GPIO.output(Q4, GPIO.LOW)

    time.sleep(2)