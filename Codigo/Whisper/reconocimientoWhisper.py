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

bancoPalabra = {"oficina" : [
                "agenda",
                "calculadora",
                "carpeta",
                "corrector",
                "extintor",
                "impresora",
                "librero",
                "organizador",
                "pluma",
                "sobre",
                "archivero",
                "cargador",
                "cinta",
                "escritorio",
                "fólder",
                "lápiz",
                "marcador",
                "perforadora",
                "regla"
            ]}

palabraReconocida = ""

palabraEncontrada = ""

def reconocimientodeVoz():

    intentos = 0

    textoReconocido = ""

    #Reproducir audio indicando que comenzará a grabar
    time.sleep(1)

    print("Grabando...")

    while(intentos < 3):

        palabraReconocida = ""

        palabraEncontrada = ""

        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/InicioGrabacion.wav"])

        #confirmacion = input("Presione para grabar")

        #time.sleep(30)

        subprocess.run(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", str(duracion),archivo_salida])

        subprocess.run(["aplay", "-D", "hw:2,0", archivo_salida])

        #Aplicar reconocimiento de voz a audio generado

        try:

            resultado = modelo.transcribe(archivo_salida, language = 'es', initial_prompt ='Objetos en la oficina')

            textoReconocido = resultado['text']

            print(f"Texto: {textoReconocido}")

            #En caso de que sea una frase, solo obtener la primera palabra para impresion
            palabras = [""]

            if textoReconocido != "":

                palabras = textoReconocido.split()

                palabraReconocida = palabras[0].lower()

                #Caso no se reconocio la palabra
                if(palabraReconocida == "Objetos"):
                    intentos = intentos + 1
                    if(intentos < 3):
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])

                else:
                    print("Palabra reconocida: " + str(palabraReconocida))
                    for i in bancoPalabra["oficina"]:
                        if(palabraReconocida == i):
                            palabraEncontrada = i
                    
                    print("Palabra encontrada: " + palabraEncontrada )
                    if(palabraEncontrada != ""):
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Lapalabraes.wav"])
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/palabras/"+palabraEncontrada+".wav"])

                        #Verificacion de la palabra
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Verificacion.wav"])

                        subprocess.run(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", str(duracion),archivo_salida])

                        subprocess.run(["aplay", "-D", "hw:2,0", archivo_salida])

                        resultado = modelo.transcribe(archivo_salida, language = 'es', initial_prompt ='Afirmación o Negación')

                        textoReconocido = resultado['text']

                        print("Texto afirmacion: " + textoReconocido)

                        palabras = textoReconocido.split()

                        palabraReconocida = palabras[0].lower()

                        print("palabraReconocida: " + palabraReconocida)

                        if(palabraReconocida == "si" or palabraReconocida == "sí"):
                            return(palabraEncontrada)
                        
                        else:
                            intentos = intentos + 1
                            if(intentos < 3):
                                subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])

                    else:
                        intentos = intentos + 1
                        if(intentos < 3):
                            subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])
                    

                #Algoritmo para encontrar la palabra con mayor simulitud a las opciones de reconocimiento

                #Se pregunta se la palabra reconocida es la que quiere imprimir



                #bancoEscritorio = ['Esescritorio', ]

                #Se devuelve la palabra


            else:
                intentos = intentos + 1
                if(intentos < 3):
                    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])

            
        
        except:
            print("Error en el reconocimiento")

    return(palabraEncontrada)

    



    