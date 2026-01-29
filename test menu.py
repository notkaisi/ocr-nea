#menu1
import subprocess
import sys
import os

def start():
    print('game started')
    game_path = os.path.join(os.path.dirname(__file__), "openworld3.py")
    subprocess.Popen([sys.executable, game_path])
start()

