import sys
import os
import time

# typewrite function taken from https://www.youtube.com/watch?v=A_1THfBpCH8&list=LL&index=1 

def typewrite(string):
    """
    Loops through a prints each letter one after the 
    other left to right. 
    """
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)

# restart_program fuction copied from https://www.daniweb.com/programming/software-development/code/260268/restart-your-python-program

def restart_program():
    """
    Restarts the current program.
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)
