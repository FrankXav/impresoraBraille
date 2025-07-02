import subprocess
import os
import signal
import time


print("Proyecto Etiquedadora Braille")

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

#from Arranque.IniciarTerminal import *

#subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Introduccion.wav", "ENTER"])

time.sleep(1)

inicioFalso = subprocess.Popen(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", "1", "falso.mp3"])

inicioFalso.send_signal(signal.SIGINT)

inicioFalso.wait()


subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Introduccion.wav"])


from Whisper.reconocimientoWhisper import *

#subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Preparado.wav", "ENTER"])

subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Preparado.wav"])


while(True):

    subprocess.run(["python3.6", "Electronica/botones.py"])

    result = subprocess.run(["python3.6", "Electronica/estadoSensores.py"], capture_output=True, text=True)

    print(result)

    confirmacion = result.stdout.strip()

    print("------------------ " + confirmacion)

    palabraReconocida = ""

    if("correcto" in confirmacion):

        palabraReconocida = reconocimientodeVoz()

    #palabraReconocida = "<<<<<"

    if(palabraReconocida != ""):

        print("Se imprimira la palabra: " + str(palabraReconocida))
        subprocess.run(["python", "Braille/imprimirTexto.py", palabraReconocida])
        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/FinImpresion.wav"])



    else:
        print("Ocurrio un error en el reconocimiento")