import subprocess
import time

subprocess.run(["tmux", "new-session", "-d", "-s", "impresorabraille"])

print("Inicio de terminal")

subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "python3.8 /home/jetson/Documents/impresoraBraille/Codigo/main.py", "ENTER"])