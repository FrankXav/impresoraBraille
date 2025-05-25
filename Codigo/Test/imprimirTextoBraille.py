import subprocess
import os
import sys

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

subprocess.run(["python3.6", "Braille/imprimirTexto.py", "<<<<<"])
