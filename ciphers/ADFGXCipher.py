import ctypes
import math

alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")


def charIndex(let, mat):
    r, c = 0, 0
    for row in mat:
        for char in row:
            if char == let:
                return r, c
            c = c + 1
        r = r + 1
        c = 0


def encrypt(text, key1, key2):
    try:
        if text == "" or key1 == "" or key2 == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        elif not text.replace(' ', '').isalpha():
            ctypes.windll.user32.MessageBoxW(None, "Special characters are not supported", "Error!", 0)
        else:
            polyBiousKey = key1.upper().replace(" ", "")
            # Defining the dictionary to hold ADFGX keywords.
            ADFGVX = {0: "A", 1: "D", 2: "F", 3: "G", 4: "X"}
            cipherText = ""
            # Getting input
            Text = text.upper().replace(" ", "").replace("J", "I")
            mat1Val = []
            for c in polyBiousKey:
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
                    index = index + 1
                mat1.append(row)

            for c in Text:
                r = charIndex(c, mat1)[0]
                c = charIndex(c, mat1)[1]
                cipherText += ADFGVX[r] + ADFGVX[c]

            columnarKey = key2.upper().replace(" ", "")  # Capitalizing and Removing the Spaces

            sequenceOrd = []  # To find out the order of sequence for Columnar.
            for index, let in enumerate(columnarKey):  # Removing any duplicate letter entries.
                currentVal = 1
                backLet = columnarKey[:index]
                for backPos, backChar in enumerate(backLet):
                    if backChar > let:
                        sequenceOrd[backPos] += 1
                    else:
                        currentVal += 1
                sequenceOrd.append(currentVal)
            keySeq = sequenceOrd

            columns = []
            for i in range(len(columnarKey)):  # Arranging Columns
                columns.append(cipherText[i::len(columnarKey)])
            cipherText = [columns[keySeq.index(i + 1)]
                          for i in range(len(columnarKey))]
            cipherText = "".join(cipherText)

            return cipherText

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(text, key1, key2):
    try:
        if text == "" or key1 == "" or key2 == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        elif not text.replace(' ', '').isalpha():
            ctypes.windll.user32.MessageBoxW(None, "Special characters are not supported", "Error!", 0)
        else:
            mat = []
            total = 0
            cipherText = text.replace(" ", "").upper().replace("J", "I")
            columnarKey = key2.upper().replace(" ", "")
            # Attributes of our Columnar Key
            col = len(columnarKey)
            row = int(math.ceil(len(cipherText) / col))

            for i in range(row):
                mat.append([])
                for c in range(col):
                    if total < len(cipherText):
                        mat[i].append('')
                        total += 1

            sequenceOrd = []  # finding order of the columinar key word
            for indx, letter in enumerate(
                    columnarKey):  # to avoid getting the same number in repeated letters like in word hello
                current_num = 1
                previousLetters = columnarKey[:indx]
                for previousPos, previous_char in enumerate(previousLetters):
                    if previous_char > letter:
                        sequenceOrd[previousPos] += 1
                    else:
                        current_num += 1
                sequenceOrd.append(current_num)
            keySeq = sequenceOrd

            pos = 0
            for val in range(len(keySeq)):
                column = keySeq.index(val + 1)

                i = 0
                while (i < len(mat)) and (len(mat[i]) > column):
                    mat[i][column] = cipherText[pos]
                    i = i + 1
                    pos = pos + 1

            cipherText = "".join(sum(mat, []))

            polyBiousKey = key1.upper().replace(" ", "")

            matVal = []
            for c in polyBiousKey:
                if c in alphabet and c not in matVal:
                    matVal.append(c)
            for c in alphabet:
                if c not in matVal:
                    matVal.append(c)

            mat1 = []
            index = 0
            for rows in range(5):
                row = []
                for columns in range(5):
                    row.append(matVal[index])
                    index = index + 1
                mat1.append(row)
            ADFGX = {"A": "0", "D": "1", "F": "2", "G": "3", "X": "4"}
            cipherText = "".join([ADFGX[i] for i in cipherText])
            cipherText = [cipherText[i:2 + i] for i in range(0, len(cipherText), 2)]
            plainText = ""
            for pairVals in cipherText:
                plainText += mat1[int(pairVals[0])][int(pairVals[1])]

            return plainText

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
