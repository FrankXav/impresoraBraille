import Jetson.GPIO as GPIO
import time

Q1 = 7
Q2 = 11
Q3 = 13
Q4 = 12

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

timeCiclo = 0.0005

def ejecutarCiclo(CW):
    #print("Ejecutar paso")
    
    for ind in range(4):
        
        if(CW):
            paso = ind
        else:
            paso = 3 - ind
            
        print(secuencia[paso])
        
        #Envio de datos
        GPIO.output(Q1, GPIO.HIGH if secuencia[paso][0] == 1 else GPIO.LOW)
        GPIO.output(Q2, GPIO.HIGH if secuencia[paso][1] == 1 else GPIO.LOW)
        GPIO.output(Q3, GPIO.HIGH if secuencia[paso][2] == 1 else GPIO.LOW)
        GPIO.output(Q4, GPIO.HIGH if secuencia[paso][3] == 1 else GPIO.LOW)
        
        time.sleep(timeCiclo)


def mover1mmDerecha():
    
    for i in range(4):
        ejecutarCiclo(CW = True) 
        #time.sleep(0.1)
        
    
        
    
    
def mover1mmIzquierda():
    
    for i in range(4):
        ejecutarCiclo(CW = False) 
        
    
        
        #time.sleep_ms(1)


        