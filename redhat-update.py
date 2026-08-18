import subprocess
import os

def execute_update():
    os.system("sudo dnf upgrade -y")
    
if __name__ == "__main__":
    execute_update()   