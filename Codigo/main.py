print("Proyecto Etiquedadora Braille")

from Arranque.IniciarTerminal import *

subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Introduccion.wav", "ENTER"])


from Whisper.reconocimientoWhisper import *




#Ejecutamos función de reconocimiento



""" while(True):

    palabraReconocida = reconocimientodeVoz()

    if(palabraReconocida != ""):

        subprocess.run(["python", "Braille/imprimirTexto.py", palabraReconocida])

    else:
        print("Ocurrio un error en el reconocimiento") """