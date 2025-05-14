from Whisper.ReconocimientoWhisper import *

print("Proyecto Etiquedadora Braille")

#Ejecutamos función de reconocimiento

palabraReconocida = reconocimientodeVoz()

if(palabraReconocida != ""):

    subprocess.run(["python", "Braille/imprimirTexto.py", palabraReconocida])

else:
    print("Ocurrio un error en el reconocimiento")