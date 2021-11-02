import math
import ctypes


def encrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        else:
            if key.isdigit():
                key = int(key)
            else:
                key = len(key)
            readied = ''.join(text.split())
            cipher = [''] * key
            for col in range(key):
                index = col
                while index < len(readied):
                    cipher[col] += readied[index]
                    index += key
            return ''.join(cipher)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "No text entered", "Error!", 0)


def decrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        else:
            if key.isdigit():
                key = int(key)
            else:
                key = len(key)
            cols = math.ceil(len(text) / key)
            rows = key
            extra = (cols * rows) - len(text)
            col = 0
            row = 0
            decipher = [''] * cols
            for char in text:
                decipher[col] += char
                col += 1
                if (col == cols) or (col == cols - 1 and row >= rows - extra):
                    col = 0
                    row += 1

            return ''.join(decipher)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "No text entered", "Error!", 0)
