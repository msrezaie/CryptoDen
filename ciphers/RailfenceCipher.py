import ctypes


def encrypt(plaintext, key):
    try:
        if plaintext == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        elif not key.isdigit():
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key", "Error!", 0)
        else:
            key = int(key)
            Rfence = [['\n' for i in range(len(plaintext))] for j in range(key)]

            dirc = False
            row, col = 0, 0

            for i in range(len(plaintext)):
                if (row == 0) or (row == key - 1):
                    dirc = not dirc
                Rfence[row][col] = plaintext[i]
                col += 1

                if dirc:
                    row += 1
                else:
                    row -= 1

            enc = []
            for i in range(key):
                for j in range(len(plaintext)):
                    if Rfence[i][j] != '\n':
                        enc.append(Rfence[i][j])
            return "".join(enc)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(cipher, key):
    try:
        if cipher == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered", "Error!", 0)
        elif not key.isdigit():
            ctypes.windll.user32.MessageBoxW(None, "Invalid Key", "Error!", 0)
        else:
            key = int(key)
            Rfence = [['\n' for i in range(len(cipher))] for j in range(key)]

            dirc = None
            row, col = 0, 0

            for i in range(len(cipher)):
                if row == 0:
                    dirc = True
                if row == key - 1:
                    dirc = False
                Rfence[row][col] = '*'
                col += 1

                if dirc:
                    row += 1
                else:
                    row -= 1

            index = 0
            for i in range(key):
                for j in range(len(cipher)):
                    if (Rfence[i][j] == '*') and (index < len(cipher)):
                        Rfence[i][j] = cipher[index]
                        index += 1

            dec = []
            row, col = 0, 0
            for i in range(len(cipher)):
                if row == 0:
                    dirc = True
                if row == key - 1:
                    dirc = False

                if Rfence[row][col] != '*':
                    dec.append(Rfence[row][col])
                    col += 1

                if dirc:
                    row += 1
                else:
                    row -= 1
            return "".join(dec)

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
