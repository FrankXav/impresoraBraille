import subprocess
import os
import signal

print("Proyecto Etiquedadora Braille")

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

#from Arranque.IniciarTerminal import *

#subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Introduccion.wav", "ENTER"])

inicioFalso = subprocess.Popen(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", "1", "falso.mp3"])

inicioFalso.send_signal(signal.SIGINT)

inicioFalso.wait()

subprocess.run(["aplay", "../../Audios/Introduccion.wav"])


from Whisper.reconocimientoWhisper import *

#subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Preparado.wav", "ENTER"])
subprocess.run(["aplay", "../../Audios/Preparado.wav"])


while(True):

    palabraReconocida = reconocimientodeVoz()

    if(palabraReconocida != ""):

        #subprocess.run(["python", "Braille/imprimirTexto.py", palabraReconocida])
        print("Se imprimira la palabra: " + str(palabraReconocida))

    else:
        print("Ocurrio un error en el reconocimiento")