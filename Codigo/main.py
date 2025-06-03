import subprocess
import os

print("Proyecto Etiquedadora Braille")

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

#from Arranque.IniciarTerminal import *

#subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Introduccion.wav", "ENTER"])
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