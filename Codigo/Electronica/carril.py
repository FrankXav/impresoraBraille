import Jetson.GPIO as GPIO
import time

Q1 = 3
Q2 = 5
Q3 = 7
Q4 = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(Q1, GPIO.OUT, initial=0)
GPIO.setup(Q2, GPIO.OUT, initial=0)
GPIO.setup(Q3, GPIO.OUT, initial=0)
GPIO.setup(Q4, GPIO.OUT, initial=0)

secuencia = [[1,0,0,1],
             [1,0,1,0],
             [0,1,1,0],
             [0,1,0,1]]

def ejecutarCiclo(CW):
    #print("Ejecutar paso")
    
    for ind in range(4):
        
        if(CW):
            paso = ind
        else:
            paso = 3 - ind
            
        #print(secuencia[paso])
        
        #Envio de datos
        GPIO.output(Q1, GPIO.HIGH if secuencia[paso][0] == 1 else GPIO.LOW)
        GPIO.output(Q1, GPIO.HIGH if secuencia[paso][2] == 1 else GPIO.LOW)
        GPIO.output(Q1, GPIO.HIGH if secuencia[paso][3] == 1 else GPIO.LOW)
        GPIO.output(Q1, GPIO.HIGH if secuencia[paso][4] == 1 else GPIO.LOW)
        
        time.sleep_ms(1)

def mover1mmDerecha():
    
    for i in range(6):
        ejecutarCiclo(CW = True) 
        
        GPIO.output(Q1, GPIO.LOW)
        GPIO.output(Q2, GPIO.LOW)
        GPIO.output(Q3, GPIO.LOW)
        GPIO.output(Q4, GPIO.LOW)
        
        #time.sleep_ms(1)
    
def mover1mmIzquierda():
    
    for i in range(6):
        ejecutarCiclo(CW = False) 
        
        GPIO.output(Q1, GPIO.LOW)
        GPIO.output(Q2, GPIO.LOW)
        GPIO.output(Q3, GPIO.LOW)
        GPIO.output(Q4, GPIO.LOW)
        
        #time.sleep_ms(1)