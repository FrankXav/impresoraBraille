from Electronica.carril import *

C1 = 19
C2 = 21
C3 = 22
C4 = 23

GPIO.setup(C1, GPIO.OUT, initial=0)
GPIO.setup(C2, GPIO.OUT, initial=0)
GPIO.setup(C3, GPIO.OUT, initial=0)
GPIO.setup(C4, GPIO.OUT, initial=0)

def ejecutarCicloAvance(CW):
    #print("Ejecutar paso")
    
    for ind in range(4):
        
        if(CW):
            paso = ind
        else:
            paso = 3 - ind
            
        #print(secuencia[paso])
        
        #Envio de datos
        GPIO.output(C1, GPIO.HIGH if secuencia[paso][0] == 1 else GPIO.LOW)
        GPIO.output(C2, GPIO.HIGH if secuencia[paso][1] == 1 else GPIO.LOW)
        GPIO.output(C3, GPIO.HIGH if secuencia[paso][2] == 1 else GPIO.LOW)
        GPIO.output(C4, GPIO.HIGH if secuencia[paso][3] == 1 else GPIO.LOW)
        
        time.sleep(timeCiclo)


def mover1mmDerechaAvance():
    
    for i in range(1):
        ejecutarCicloAvance(CW = True) 
        #time.sleep(0.1)
        
    
def mover1mmIzquierdaAvance():
    
    for i in range(1):
        ejecutarCicloAvance(CW = False) 