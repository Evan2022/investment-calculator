import math
import sys
import os
import time
from colorama import Fore, Back, Style

def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)