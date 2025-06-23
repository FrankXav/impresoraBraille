# coding: utf-8
import subprocess
import os
import sys
import whisper
import time


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

modelo = whisper.load_model("small")

duracion = 3  # segundos
archivo_salida = "/home/jetson/Documents/grabaciones/grabacion.wav"

def reconocimientodeVoz():

    textoReconocido = ""

    #Reproducir audio indicando que comenzará a grabar
    time.sleep(1)

    print("Grabando...")

    confirmacion = input("Presione para grabar")

    #time.sleep(30)

    subprocess.run(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", str(duracion),archivo_salida])

    subprocess.run(["aplay", "-D", "hw:2,0", archivo_salida])

    #Aplicar reconocimiento de voz a audio generado

    try:

        resultado = modelo.transcribe(archivo_salida, language = 'es', initial_prompt ='Objetos en la oficina')

        textoReconocido = resultado['text']

        print(f"Texto: {textoReconocido}")

        #Algoritmo para encontrar la palabra con mayor simulitud a las opciones de reconocimiento

        

        #En caso de que sea una frase, solo obtener la primera palabra para impresion
        palabras = [""]

        if textoReconocido != "":

            palabras = textoReconocido.split()

        #Se pregunta se la palabra reconocida es la que quiere imprimir

        bancoEscritorio = ['Esescritorio', ]

        #Se devuelve la palabra
    
    except:
        print("Error en el reconocimiento")

    return(palabras[0])

    



    