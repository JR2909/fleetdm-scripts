import subprocess
import os

def execute_update():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade -y")
    
    print("Update complete.")

if __name__ == "__main__":
    execute_update()   