import string
import itertools
import ctypes


def prepareInput(raw):
    raw = "".join([c.upper() for c in raw if c in string.ascii_letters])
    clean = ""

    if len(raw) < 2:
        return raw

    for i in range(len(raw) - 1):
        clean += raw[i]

        if raw[i] == raw[i + 1]:
            clean += "X"

    clean += raw[-1]

    if len(clean) & 1:
        clean += "X"

    return clean


def createTable(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []

    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)

    return table


def packer(seq, size):
    it = iter(seq)
    while True:
        pack = tuple(itertools.islice(it, size))
        if not pack:
            return
        yield pack


def encrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        else:
            table = createTable(key)
            text = prepareInput(text)
            result = []

            for char1, char2 in packer(text, 2):
                row1, col1 = divmod(table.index(char1), 5)
                row2, col2 = divmod(table.index(char2), 5)

                if row1 == row2:
                    result.append(table[row1 * 5 + (col1 + 1) % 5])
                    result.append(table[row2 * 5 + (col2 + 1) % 5])
                elif col1 == col2:
                    result.append(table[((row1 + 1) % 5) * 5 + col1])
                    result.append(table[((row2 + 1) % 5) * 5 + col2])
                else:
                    result.append(table[row1 * 5 + col2])
                    result.append(table[row2 * 5 + col1])

            return ''.join(result)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        else:
            table = createTable(key)
            result = []

            for char1, char2 in packer(text, 2):
                row1, col1 = divmod(table.index(char1), 5)
                row2, col2 = divmod(table.index(char2), 5)

                if row1 == row2:
                    result.append(table[row1 * 5 + (col1 - 1) % 5])
                    result.append(table[row2 * 5 + (col2 - 1) % 5])
                elif col1 == col2:
                    result.append(table[((row1 - 1) % 5) * 5 + col1])
                    result.append(table[((row2 - 1) % 5) * 5 + col2])
                else:
                    result.append(table[row1 * 5 + col2])
                    result.append(table[row2 * 5 + col1])

            return ''.join(result)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)