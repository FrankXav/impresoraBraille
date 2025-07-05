# coding: utf-8
import subprocess
import os
import sys
import time
import multiprocessing
import time
import uuid

from Whisper.transcripcion import *

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

duracion = 3  # segundos
archivo_salida = "/home/jetson/Documents/grabaciones/grabacion.wav"

entradaTranscripcion = multiprocessing.Queue()
salidaTranscripcion = multiprocessing.Queue()

proceso = multiprocessing.Process(target=loop_reconocimiento, args=(entradaTranscripcion, salidaTranscripcion))
proceso.start()

bancoPalabras = {
    "oficina": {"agenda":["agenda"],
         "calculadora": ["calculadora"],
         "carpeta": ["carpeta","carpita"],
         "corrector": ["corrector", "correcto"],
         "extintor":["extintor"],
         "impresora": ["impresora"],
         "librero": ["librero","libreero","libraro","librerojo","libreiro","libredom"],
         "organizador": ["organizador"],
         "pluma": ["pluma","bluma","loma","luma","blu"],
         "sobre": ["sobre"],
         "archivero": ["achíverón","archivero","achiveron","artíbero","artibero","activero","alcibero"],
         "cargador": ["cargador"],
         "cinta": ["cinta", "sinta", "finta"],
         "escritorio": ["escritorio","escritorio"],
         "fólder": ["fólder", "folder", "foldit"],
         "marcador": ["marcador"],
         "perforadora": ["perforadora"],
         "regla": ["regla"]
         }
}

palabraReconocida = ""

palabraEncontrada = ""


def validarPalabra(palabraCorrecta,palabraMal,dif):
    
    bandera = False

    for i in range(len(palabraMal) + 1):

        cantError = 10

        indexAnt = i-1 if i-1 >= 0 else 0

        palabraPrueba = palabraMal[0:indexAnt] + palabraMal[i:len(palabraMal)]

        if (palabraCorrecta == palabraPrueba):
            bandera = True
        
        else:
            if(len(palabraPrueba) == len(palabraCorrecta)):
                cantError = 0
                for indP in range(len(palabraCorrecta)):
                    if(palabraCorrecta[indP] != palabraPrueba[indP]):
                        cantError = cantError + 1
            
                if(cantError < 2 ):
                    bandera = True

        if(dif - 1 > 0):
            bandera = validarPalabra(palabraCorrecta,palabraPrueba,dif-1)

    return bandera


def reconocimientodeVoz():

    intentos = 0

    textoReconocido = ""

    #Reproducir audio indicando que comenzará a grabar
    time.sleep(1)

    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/InicioGrabacion.wav"])

    while(intentos < 3):

        palabraReconocida = ""

        palabraEncontrada = ""

        #confirmacion = input("Presione para grabar")

        #time.sleep(30)

        subprocess.run(["arecord", "-D", "plughw:2,0", "-f", "S16_LE", "-r", "48000", "-c", "2","-d", str(duracion),archivo_salida])

        #subprocess.run(["aplay", "-D", "hw:2,0", archivo_salida])

        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/InicioReconocimiento.wav"])

        try:

            timeout_segundos = 40

            uid = str(uuid.uuid4())
            entradaTranscripcion.put({"archivo": archivo_salida, "uid": uid})

            textoReconocido = ""

            start = time.time()
            while time.time() - start < timeout_segundos:
                while not salidaTranscripcion.empty():
                    resultado = salidaTranscripcion.get()
                    if resultado["uid"] == uid:
                        textoReconocido = resultado["texto"]
                time.sleep(0.5)

            print(f"Texto: {textoReconocido}")

            #En caso de que sea una frase, solo obtener la primera palabra para impresion
            palabras = [""]

            if textoReconocido != "":

                palabras = textoReconocido.split()

                palabraReconocida = palabras[0].lower()

                #Caso no se reconocio la palabra
                if(palabraReconocida == "objetos"):
                    intentos = intentos + 1
                    if(intentos < 3):
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])

                else:

                    #Quitar caracteres no alphanumericos
                    palabraReconocida = textoReconocido.lower().replace(" ","")
                    palabraReconocida = palabraReconocida.replace(",","")
                    palabraReconocida = palabraReconocida.replace(".","")
                    palabraReconocida = palabraReconocida.replace("!","")
                    palabraReconocida = palabraReconocida.replace("?","")
                    palabraReconocida = palabraReconocida.replace("_","")
                    palabraReconocida = palabraReconocida.replace("¡","")

                    print("Palabra reconocida: " + str(palabraReconocida))

                    """for key,list in bancoPalabra["oficina"]:
                        if(palabraReconocida == i):
                            palabraEncontrada = i """

                    for key, value in bancoPalabras["oficina"].items():
                        
                        #Coincidencia exacta
                        if(palabraReconocida == key):
                            palabraEncontrada = key
                        
                        #Coincidencia en banco de palabras
                        for i in value:
                            if(palabraReconocida == i):
                                palabraEncontrada = key

                        #Palabra reconocida mas larga 

                        if(len(palabraReconocida) > len(key)):
                            diferencia =  len(palabraReconocida) - len(key)

                            palabraMalPre = palabraReconocida.replace("á","a")
                            palabraMalPre = palabraMalPre.replace("é","e")
                            palabraMalPre = palabraMalPre.replace("í","i")
                            palabraMalPre = palabraMalPre.replace("ó","o")
                            palabraMalPre = palabraMalPre.replace("ú","u")

                            palabraCorrectaPre = key.replace("á","a")
                            palabraCorrectaPre = palabraCorrectaPre.replace("é","e")
                            palabraCorrectaPre = palabraCorrectaPre.replace("í","i")
                            palabraCorrectaPre = palabraCorrectaPre.replace("ó","o")
                            palabraCorrectaPre = palabraCorrectaPre.replace("ú","u")

                            coincidencia = validarPalabra(palabraCorrectaPre,palabraMalPre,diferencia)

                            if(coincidencia):
                                palabraEncontrada = key

                            
                    
                    print("Palabra encontrada: " + palabraEncontrada )
                    if(palabraEncontrada != ""):
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/Lapalabraes.wav"])
                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/palabras/"+palabraEncontrada+".wav"])

                        #Verificacion de la palabra

                        #Audio confirmación

                        subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/VerificacionPalabra.wav"])

                        result = subprocess.run(["python3.6", "Electronica/botonesConf.py"], capture_output=True, text=True)

                        print(result)

                        confirmacion = result.stdout.strip()

                        print("------------------ " + confirmacion)

                        if("afirmativo" in confirmacion):

                            #Audio comenzaremos la impresion
                            subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/ComenzarImpresion.wav"])

                            return(palabraEncontrada)
                    
                        else:
                            palabraEncontrada = ""
                            intentos = intentos + 1
                            if(intentos < 3):
                                subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])
                            

                    else:
                        intentos = intentos + 1
                        if(intentos < 3):
                            subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])


            else:
                intentos = intentos + 1
                if(intentos < 3):
                    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/RepetirReconocimiento.wav"])

            
        
        except:
            subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/ErrorReconocimiento.wav"])

    subprocess.run(["aplay", "-D", "plughw:2,0", "../../Audios/ErrorReconocimiento.wav"])
    

    return(palabraEncontrada)

    



    