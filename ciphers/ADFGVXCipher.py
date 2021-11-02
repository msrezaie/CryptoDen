import ctypes
import math
import re


def check_splcharacter(test):
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if string_check.search(test) is None:
        return True
    else:
        return False


alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


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
        elif not check_splcharacter(text):
            ctypes.windll.user32.MessageBoxW(None, "Special characters are not supported", "Error!", 0)
        else:
            mat1 = []
            index = 0
            polybiousKey = key1.upper().replace(" ", "")
            plainText = text.upper().replace(" ", "")
            mat1Val = []
            for char in polybiousKey:
                if char in alphabet and char not in mat1Val:
                    mat1Val.append(char)
            for char in alphabet:
                if char not in mat1Val:
                    mat1Val.append(char)
            for rows in range(6):
                row = []
                for columns in range(6):
                    row.append(mat1Val[index])
                    index += 1
                mat1.append(row)

            ADFGXV = {0: "A", 1: "D", 2: "F", 3: "G", 4: "V", 5: "X"}
            cipherText = ""
            for char in plainText:
                r = charIndex(char, mat1)[0]
                c = charIndex(char, mat1)[1]
                cipherText += ADFGXV[r] + ADFGXV[c]

            columinarKey = key2.upper().replace(" ", "")
            sequence = []
            for indx, letter in enumerate(
                    columinarKey):  # to avoid getting the same number in repeated letters like in word hello
                currentVal = 1
                previousLetters = columinarKey[:indx]
                for previousPos, previous_char in enumerate(previousLetters):
                    if previous_char > letter:
                        sequence[previousPos] += 1
                    else:
                        currentVal += 1
                sequence.append(currentVal)
            key_order = sequence

            columns = []
            for i in range(len(columinarKey)):
                columns.append(cipherText[i::len(columinarKey)])
            cipherText = [columns[key_order.index(i + 1)] for i in
                          range(len(columinarKey))]
            cipherText = "".join(cipherText)

            return cipherText

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(text, key1, key2):
    try:
        if text == "" or key1 == "" or key2 == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        elif not check_splcharacter(text):
            ctypes.windll.user32.MessageBoxW(None, "Special characters are not supported", "Error!", 0)
        else:
            mat = []
            total = 0
            cipherText = text.replace(" ", "").upper()
            columnarKey = key2.upper().replace(" ", "")

            column = len(columnarKey)
            row = int(math.ceil(len(cipherText) / column))

            for r in range(row):
                mat.append([])
                for c in range(column):
                    if total < len(cipherText):
                        mat[r].append('')
                        total += 1

            sequenceOrd = []
            for index, let in enumerate(
                    columnarKey):  # Omitting repeated letters.
                currentVal = 1
                backLet = columnarKey[:index]
                for backPos, backChar in enumerate(backLet):
                    if backChar > let:
                        sequenceOrd[backPos] += 1
                    else:
                        currentVal += 1
                sequenceOrd.append(currentVal)
            keySeq = sequenceOrd

            pos = 0
            for num in range(len(keySeq)):
                column = keySeq.index(num + 1)

                r = 0
                while (r < len(mat)) and (len(mat[r]) > column):
                    mat[r][column] = cipherText[pos]
                    r += 1
                    pos += 1

            cipherText = "".join(sum(mat, []))

            polybiousKey = key1.upper().replace(" ", "")

            mat1Val = []
            for char in polybiousKey:
                if char in alphabet and char not in mat1Val:
                    mat1Val.append(char)
            for char in alphabet:
                if char not in mat1Val:
                    mat1Val.append(char)

            mat1 = []
            index = 0
            for rows in range(6):
                row = []
                for columns in range(6):
                    row.append(mat1Val[index])
                    index += 1
                mat1.append(row)

            ADFGXV = {"A": "0", "D": "1", "F": "2", "G": "3", "V": "4", "X": "5"}
            cipherText = "".join([ADFGXV[i] for i in cipherText])
            cipherText = [cipherText[i:2 + i] for i in range(0, len(cipherText), 2)]
            plainText = ""
            for pairs in cipherText:
                plainText += mat1[int(pairs[0])][int(pairs[1])]

            return plainText

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
