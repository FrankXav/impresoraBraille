import subprocess
import os
import sys

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

subprocess.run(["python", "Braille/imprimirTexto.py", "oficina"])
