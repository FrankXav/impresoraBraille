import subprocess
import time

subprocess.run(["tmux", "new-session", "-d", "-s", "impresorabraille"])

subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "python3.8 main.py", "ENTER"])