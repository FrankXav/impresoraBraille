print("Proyecto Etiquedadora Braille")

from Arranque.IniciarTerminal import *

subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Introduccion.wav", "ENTER"])


from Whisper.reconocimientoWhisper import *

subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "aplay ../../Audios/Preparado.wav", "ENTER"])


while(True):

    palabraReconocida = reconocimientodeVoz()

    if(palabraReconocida != ""):

        #subprocess.run(["python", "Braille/imprimirTexto.py", palabraReconocida])
        print("Se imprimira la palabra: " + str(palabraReconocida))

    else:
        print("Ocurrio un error en el reconocimiento")