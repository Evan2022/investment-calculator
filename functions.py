import math
import sys
import time
from colorama import Fore, Back, Style

def typewrite(string):
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

