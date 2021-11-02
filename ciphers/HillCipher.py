import string
import numpy as np
import ctypes

field = string.ascii_lowercase


def decrypt(text, k1, k2, k3, k4):
    try:
        if text == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered", "Error!", 0)
        elif not k1.isdigit() or not k2.isdigit() or not k3.isdigit() or not k4.isdigit():
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key", "Error!", 0)
        else:
            cipher = text.lower()
            key = [[int(k1), int(k2)], [int(k3), int(k4)]]

            frow = []
            srow = []

            for c in range(len(cipher)):
                if c % 2 == 0:
                    frow.append(field.find(cipher[c]))
                else:
                    srow.append(field.find(cipher[c]))

            matrix = [frow, srow]

            det = np.linalg.det(key)
            det = int(det)

            if det <= 0:
                return False
            else:
                # inverse modulo
                x = 0
                for i in range(26):
                    if (det * i) % 26 == 1:
                        x = i

                if x <= 0:
                    return False
                else:
                    ikey = [[key[1][1], key[0][1] * -1], [key[1][0] * -1, key[0][0]]]

                    a = np.dot(x, ikey)

                    b = np.dot(a, matrix)

                    pl = []
                    for k in b:
                        for l in k:
                            pl.append(field[l % 26])

                    cols = len(b[0])

                    decipher = "".join(pl)

                    col = 0
                    p = [''] * cols
                    for char in decipher:
                        p[col] += char
                        col += 1
                        if col == cols:
                            col = 0

                    plain = "".join(p)
                    plain = plain.replace("x", "")

                    return plain

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


# for checking if the given keys are valid with the affine formula in encryption/decryption
def keyCheck(text, k1, k2, k3, k4):
    if decrypt(text, k1, k2, k3, k4):
        return False
    else:
        return True


def encrypt(text, k1, k2, k3, k4):
    try:
        if text == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered", "Error!", 0)
        elif not k1.isdigit() or not k2.isdigit() or not k3.isdigit() or not k4.isdigit():
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key", "Error!", 0)
        else:
            key = [[int(k1), int(k2)], [int(k3), int(k4)]]
            plain = []
            if len(text) % 2 == 1:
                text += "x"

            for ch in text:
                plain.append(field.find(ch))

            frow = []
            srow = []

            for c in range(len(plain)):
                if c % 2 == 0:
                    frow.append(plain[c])
                else:
                    srow.append(plain[c])

            matrix = [frow, srow]

            multiply = np.dot(key, matrix)
            result = []

            for i in multiply:
                for j in i:
                    result.append(field[j % 26])

            cols = len(multiply[0])

            encipher = "".join(result)

            col = 0
            ciphertext = [''] * cols
            for char in encipher:
                ciphertext[col] += char
                col += 1
                if col == cols:
                    col = 0

            res = ''.join(ciphertext)
            if keyCheck(res, k1, k2, k3, k4):
                ctypes.windll.user32.MessageBoxW(None, "Bad keys used!", "Error!", 0)
            else:
                return res

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)

