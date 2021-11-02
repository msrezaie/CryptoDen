import string
import ctypes

field = string.printable


def encrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "Both Message and Key must be Entered!", "Error!", 0)
        else:
            cipher1 = []
            cipher2 = []
            res = []
            for i in range(len(text)):
                k_ind = i % len(key)
                for a, b in enumerate(field):
                    if text[i] == b:
                        cipher1.append(a)
                    if key[k_ind] == b:
                        cipher2.append(a)
                res.append(field[(cipher1[i] + cipher2[i]) % len(field)])
            return ''.join(res)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Both Message and Key must be Entered!", "Error!", 0)


def decrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "Both Message and Key must be Entered!", "Error!", 0)
        else:
            decipher1 = []
            decipher2 = []
            res = []
            for i in range(len(text)):
                k_ind = i % len(key)
                for a, b in enumerate(field):
                    if text[i] == b:
                        decipher1.append(a)
                    if key[k_ind] == b:
                        decipher2.append(a)
                res.append(field[(decipher1[i] - decipher2[i]) % len(field)])
            return ''.join(res)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Both Message and Key must be Entered!", "Error!", 0)
