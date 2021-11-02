import ctypes

alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")


def charIndex(let, mat):
    r, c = 0, 0
    for row in mat:
        for char in row:
            if char == let:
                return r, c
            c += 1
        r += 1
        c = 0


def encrypt(text, key1, key2):
    try:
        if text == "" or key1 == "" or key2 == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        elif not text.replace(' ', '').isalpha():
            ctypes.windll.user32.MessageBoxW(None, "Special characters are not supported", "Error!", 0)
        else:
            key1 = key1.replace(" ", "").upper()
            key2 = key2.replace(" ", "").upper()
            mat1Val = []
            for c in key1:
                if c in alphabet and c not in mat1Val:
                    mat1Val.append(c)
            for c in alphabet:
                if c not in mat1Val:
                    mat1Val.append(c)

            mat1 = []
            index = 0
            for rows in range(5):
                row = []
                for columns in range(5):
                    row.append(mat1Val[index])
                    index += 1
                mat1.append(row)

            mat2Val = []
            for char in key2:
                if char in alphabet and char not in mat2Val:
                    mat2Val.append(char)
            for char in alphabet:
                if char not in mat2Val:
                    mat2Val.append(char)

            mat2 = []
            index = 0
            for rows in range(5):
                row = []
                for columns in range(5):
                    row.append(mat2Val[index])
                    index += 1
                mat2.append(row)

            plainText = text.replace(" ", "").upper().replace("J", "I")
            for var in range(0, len(plainText) + 1, 2):
                if var < len(plainText) - 1:
                    if plainText[var] == plainText[var + 1]:
                        plainText = plainText[:var + 1] + 'X' + plainText[var + 1:]
            if len(plainText) % 2 != 0:
                plainText = plainText[:] + ' x '
            plainText = " ".join(plainText[i:i + 2] for i in range(0, len(plainText), 2)).split(
                " ")  # Splits the string into pairVals with a space between them
            cipher = ""

            for pairVals in plainText:
                index1 = charIndex(pairVals[0], mat1)
                index2 = charIndex(pairVals[1], mat2)
                var1 = mat1[index2[0]][index1[1]]
                var2 = mat2[index1[0]][index2[1]]
                cipher += var1 + var2 + ""

            return cipher

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(text, key1, key2):
    try:
        if text == "" or key1 == "" or key2 == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        elif not text.replace(' ', '').isalpha():
            ctypes.windll.user32.MessageBoxW(None, "Special characters are not supported", "Error!", 0)
        else:
            key1 = key1.replace(" ", "").upper()
            key2 = key2.replace(" ", "").upper()
            mat1Val = []
            for c in key1:
                if c in alphabet and c not in mat1Val:
                    mat1Val.append(c)
            for c in alphabet:
                if c not in mat1Val:
                    mat1Val.append(c)

            matrix1 = []
            index = 0
            for rows in range(5):
                row = []
                for column in range(5):
                    row.append(mat1Val[index])
                    index += 1
                matrix1.append(row)

            mat2Val = []
            for c in key2:
                if c in alphabet and c not in mat2Val:
                    mat2Val.append(c)
            for c in alphabet:
                if c not in mat2Val:
                    mat2Val.append(c)

            matrix2 = []
            index = 0
            for rows in range(5):
                row = []
                for column in range(5):
                    row.append(mat2Val[index])
                    index += 1
                matrix2.append(row)

            plainText = text.replace(" ", "").upper().replace("J", "I")
            for s in range(0, len(plainText) + 1, 2):
                if s < len(plainText) - 1:
                    if plainText[s] == plainText[s + 1]:
                        plainText = plainText[:s + 1] + 'X' + plainText[s + 1:]
            if len(plainText) % 2 != 0:
                plainText = plainText[:] + 'X'
            plainText = " ".join(plainText[i:i + 2]
                                 for i in range(0, len(plainText), 2)).split(" ")
            result = ""

            for pairVals in plainText:
                index1 = charIndex(pairVals[0], matrix1)
                index2 = charIndex(pairVals[1], matrix2)
                var1 = matrix1[index2[0]][index1[1]]
                var2 = matrix2[index1[0]][index2[1]]
                result += var1 + var2 + ""

            return result

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
