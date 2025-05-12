import sys
import os

from Braille.tansBraille import *

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

texto = sys.argv[1]

print(texto)