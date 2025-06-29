

dif = 0

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


def ejecucion():

    dif = 0

    palabraMal = "ezcriptorios"

    palabraCorrecta = "escritorio"

    #Prepara palabra

    palabraMalPre = palabraMal.replace("á","a")
    palabraMalPre = palabraMalPre.replace("é","e")
    palabraMalPre = palabraMalPre.replace("í","i")
    palabraMalPre = palabraMalPre.replace("ó","o")
    palabraMalPre = palabraMalPre.replace("ú","u")

    palabraCorrectaPre = palabraCorrecta.replace("á","a")
    palabraCorrectaPre = palabraCorrectaPre.replace("é","e")
    palabraCorrectaPre = palabraCorrectaPre.replace("í","i")
    palabraCorrectaPre = palabraCorrectaPre.replace("ó","o")
    palabraCorrectaPre = palabraCorrectaPre.replace("ú","u")

    dif = len(palabraMal) - len(palabraCorrecta)

    coincidencia = validarPalabra(palabraCorrectaPre,palabraMalPre,dif)

    if(coincidencia):
        print("Coincidencia!")

    else:
        print("No encontrada")

ejecucion()