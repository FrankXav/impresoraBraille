import sys
import os

#print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Braille.tansBraille import *
from Electronica.iniciarCarrail import *

texto = sys.argv[1]

print("Palabra a imprimir " + str(texto))

iniciarCarril()