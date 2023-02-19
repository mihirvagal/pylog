# PyLog

This is a simple keylogger written in Python that captures and logs every keystroke typed on the keyboard. The program runs in the background and saves the logged data in a text file. It can be used for educational purposes or as a tool for monitoring computer usage.

## Requirements

- Python 3.x
    - pynput

## Getting started

1. Clone the repository to your system
```sh
git clone https://github.com/mihirvagal/pylog.git
```

2. Install the requirements
```sh
pip install -r requirements.txt
```

3. Run the program
```sh
python3 src/keylogger.py  # for Linux/macOS

py src/keylogger.py       # for Windows
```

## Usage

The keylogger will start running as soon as you run the program. It will capture and log every keystroke typed on the keyboard, including special keys such as function keys and arrow keys.

To stop the keylogger, press the `Esc` key. The logged data will be saved in a text file named `log_[date].txt`.

# Licence

This project is licensed under the MIT License—see the `LICENSE.md` file for details.

# Disclaimer

This keylogger is intended for educational or monitoring purposes only. Do not use it for malicious purposes. The author is not responsible for any misuse of this program.