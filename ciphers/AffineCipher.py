import math
import string
import ctypes


def is_coprime(x):
    return math.gcd(x, 26) == 1


field = string.ascii_lowercase


def encrypt(text, key):
    temp = key.replace(',', ' ').split()
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key Entered", "Error!", 0)
        elif ',' not in key or len(key) > 5 or len(temp) != 2:
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key/Not Comma Separated", "Error!", 0)
        elif not is_coprime(int(temp[0])):
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key", "Error!", 0)
        else:
            key = key.replace(',', ' ').split()
            a = int(key[0])
            b = int(key[1])
            enc = []
            for letter in text:
                index = field.find(letter)
                if index != -1:
                    index = (((a * index) + b) % 26)
                    enc.append(field[index])
                else:
                    enc.append(letter)

            return "".join(enc)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(message, key):
    try:
        if message == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key Entered", "Error!", 0)
        elif ',' not in key or len(key) > 5:
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key/Not Comma Separated", "Error!", 0)
        else:
            key = key.replace(',', ' ').split()
            a = int(key[0])
            b = int(key[1])
            # inverse modulo value
            x = 0
            for i in range(26):
                if (a * i) % 26 == 1:
                    x = i

            # affine decrypt formula
            dec = []
            for letter in message:
                index = field.find(letter)
                if index != -1:
                    index = (x * (index - b) % 26)
                    dec.append(field[index])
                else:
                    dec.append(letter)

            return "".join(dec)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
