import subprocess
import os
import sys

print("os.getcwd() desde imprimirTexto.py" + str(os.getcwd()))

# Ahora ejecutar el script
subprocess.run(["python", "Braille/imprimirTexto.py", "oficina"])
