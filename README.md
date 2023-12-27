# Simple Python Keylogger

This is a basic Python keylogger that uses the `pynput` library to monitor and record key presses. It's a simple script designed for educational purposes.

## Features

- Records all keypresses in a text file (`log.txt`).
- Handles special keys like `space` for better readability in the log.
- Stops recording when the `esc` key is pressed.

## Requirements

This script requires Python and the `pynput` library. Ensure you have Python installed on your machine. You can install `pynput` using pip:

    ```bash
        pip install pynput

##Usage

To start the keylogger, simply run the script:

    ```bash
        python keylogger.py

The script will start recording all keypresses. Each set of 10 keypresses will be written to log.txt. Press the esc key to stop the script.

##Disclaimer

This script is for educational purposes only. Unauthorized keylogging is a violation of privacy and is illegal in many jurisdictions. Use this script responsibly.

License

This project is open source and available under the [MIT License](LICENSE).
