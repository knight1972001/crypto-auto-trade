import threading
import time
from actionDB import *
from utils import *
import keyboard


def getTime():
    while True:
        get_time()
        time.sleep(1)


space_thread = threading.Thread(target=getTime, daemon=True)
space_thread.start()

# Main thread prints the time
while True:
    # Start the space monitoring thread

    while True:
        if keyboard.is_pressed("space"):
            print("Space pressed")
        if keyboard.is_pressed("s"):
            print("S pressed")
        time.sleep(0.1)
