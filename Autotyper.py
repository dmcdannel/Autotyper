from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time

# The key combination to check
COMBINATION = {keyboard.Key.alt, keyboard.Key.ctrl}

# The currently active modifiers
current = set()

def dowork():
        keyboard = Controller()
        text = pyperclip.paste()
        for i in text:
		time.sleep
                keyboard.press(i)

def on_press(key):
	if key in COMBINATION:
		current.add(key)
		if all(k in current for k in COMBINATION):
			print("made it here")
			dowork()
	if key == keyboard.Key.esc:
		listener.stop()


def on_release(key):
	try:
		current.remove(key)
	except KeyError:
		pass


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
