import sys
import os

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

# Añadir el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Braille.tansBraille import *

texto = sys.argv[1]

print(texto)