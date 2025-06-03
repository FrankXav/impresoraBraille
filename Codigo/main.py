from Whisper.reconocimientoWhisper import *
from Arranque.IniciarTerminal import *

print("Proyecto Etiquedadora Braille")

#Ejecutamos función de reconocimiento

Introduccion()

""" while(True):

    palabraReconocida = reconocimientodeVoz()

    if(palabraReconocida != ""):

        subprocess.run(["python", "Braille/imprimirTexto.py", palabraReconocida])

    else:
        print("Ocurrio un error en el reconocimiento") """