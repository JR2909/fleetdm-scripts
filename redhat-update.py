#!/usr/bin/env python3
import subprocess
import sys


def execute_update():
    try:
        subprocess.run(["sudo", "dnf", "upgrade", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(1)


if __name__ == "__main__":
    execute_update()