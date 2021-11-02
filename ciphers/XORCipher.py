import ctypes


def xor(text, key):
    try:
        if text == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered", "Error!", 0)
        elif not key.isdigit() or int(key) > 127 or int(key) < 0:
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key", "Error!", 0)
        else:
            enc = []
            for i in text:
                enc.append(chr(ord(i) ^ int(key)))

            return ''.join(enc)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)

