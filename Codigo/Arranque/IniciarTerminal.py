import subprocess
import time

subprocess.run(["tmux", "new-session", "-d", "-s", "impresorabraille"])

""" time.sleep(3)

subprocess.run(["tmux", "send-keys", "-t", "impresorabraille", "ls -l", "ENTER"]) """
    