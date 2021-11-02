import string
import re
import ctypes

field = string.ascii_uppercase


def encrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        else:
            text = text.upper()
            encrypted = []
            for i in text:
                ind = field.find(i)
                if ind != -1:
                    if i in text:
                        index = (field.find(i) + key) % len(field)
                        encrypted.append(field[index])
                else:
                    encrypted.append(i)

            return ''.join(encrypted)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        else:
            text = text.upper()
            decrypted = []
            for i in text:
                ind = field.find(i)
                if ind != -1:
                    if i in text:
                        index = (field.find(i) - key) % len(field)
                        decrypted.append(field[index])
                else:
                    decrypted.append(i)

            return ''.join(decrypted)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
