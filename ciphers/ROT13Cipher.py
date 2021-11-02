import string
import ctypes

field = string.ascii_uppercase


def encrypt(ptext):
    key = 13
    try:
        if ptext == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered!", "Error!", 0)
        else:
            ptext = ptext.upper()
            encrypted = []
            for i in ptext:
                ind = field.find(i)
                if ind != -1:
                    if i in ptext:
                        index = (field.find(i) + key) % len(field)
                        encrypted.append(field[index])
                else:
                    encrypted.append(i)

            return ''.join(encrypted)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(ctext):
    key = 13
    try:
        if ctext == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered!", "Error!", 0)
        else:
            ctext = ctext.upper()
            decrypted = []
            for i in ctext:
                ind = field.find(i)
                if ind != -1:
                    if i in ctext:
                        index = (field.find(i) - key) % len(field)
                        decrypted.append(field[index])
                else:
                    decrypted.append(i)

            return ''.join(decrypted)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
