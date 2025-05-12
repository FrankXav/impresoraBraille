import subprocess
import os
import sys

print(f'os.getcwd() desde imprimirTexto.py {os.getcwd()}')

# Ahora ejecutar el script
subprocess.run(["python", "Braille/imprimirTexto.py", "oficina"])
