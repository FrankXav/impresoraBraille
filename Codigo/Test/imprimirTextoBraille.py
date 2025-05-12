import subprocess
import os
import sys

print(os.getcwd())

# Agregar el directorio raíz al path de Python
sys.path.insert(0, os.getcwd())

# Ahora ejecutar el script
subprocess.run(["python", "Braille/imprimirTexto.py", "oficina"])
