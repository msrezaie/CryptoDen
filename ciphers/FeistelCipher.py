import random
import ctypes


# Function to translate binary to char
def translate(text):
    result = []
    for i in range(0, len(text), 8):
        result.append(chr(int(text[i:i + 8], 2)))

    return ''.join(result)


# Function for doing XOR of binary
def bin_xor(x, y):
    temp = ""
    for i in range(len(x)):
        if x[i] == y[i]:
            temp += "0"
        else:
            temp += "1"
    return temp


# Function for doing OR of binary
def bin_or(x, y):
    temp = ""
    for i in range(len(x)):
        if x[i] == "0" and y[i] == "1" or x[i] == "1" and y[i] == "0" or x[i] == "1" and y[i] == "1":
            temp += "1"
        else:
            temp += "0"
    return temp


# Function converting the plaintext to binary
def t2b(textB):
    tempL = []
    for i in textB:
        res = bin(ord(i)).replace('b', '')
        if len(res) < 8:
            tempL.append("0" + res)
        else:
            tempL.append(res)

    return ''.join(tempL)


# Function for a evening the key's length to the plaintext's
def fixLength(a, b):
    if len(b) != len(a):
        c = b.split()
        for i in range(0, len(a) - len(b)):
            c.append("0")
            # c.insert(i, "0")
        return ''.join(c)
    else:
        return b


# Function for performing two rounds of feistel cipher
def rounds(leftT, rightT, key0, key1):
    # round 1
    left0 = bin_or(rightT, key0)
    left0 = bin_xor(leftT, left0)
    right0 = rightT

    # round 2
    left1 = bin_or(key1, left0)
    left1 = bin_xor(right0, left1)
    right1 = left0

    return left1 + right1


# Encryption process
def e_process(textB, keyB):
    # Left and Right parts of Plaintext
    L0 = textB[:len(textB) // 2]
    R0 = textB[len(textB) // 2:]

    # Left and Right parts of Key
    K0 = keyB[:len(keyB) // 2]
    K1 = keyB[len(keyB) // 2:]

    # Encryption
    enc = rounds(L0, R0, K0, K1)

    return enc


# Decryption process
def d_process(cipherB, keyB):
    # Left and Right parts of ciphertext
    D0 = cipherB[:len(cipherB) // 2]
    D1 = cipherB[len(cipherB) // 2:]

    # Left and Right parts of Key
    K0 = keyB[:len(keyB) // 2]
    K1 = keyB[len(keyB) // 2:]

    dec = rounds(D0, D1, K1, K0)

    return dec


# Main encryption function
def encrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        elif len(key) > len(text):
            ctypes.windll.user32.MessageBoxW(None, "Key length must be less than text length", "Error!", 0)
        else:
            tInB = t2b(text)
            kInB = fixLength(tInB, t2b(key))

            return translate(e_process(tInB, kInB))
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


# Main decryption function
def decrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        elif len(key) > len(text):
            ctypes.windll.user32.MessageBoxW(None, "Key length must be less than text length", "Error!", 0)
        else:
            tInB = ''.join(format(ord(i), '08b') for i in text)
            kInB = fixLength(tInB, t2b(key))

            return translate(d_process(tInB, kInB))
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
