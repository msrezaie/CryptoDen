import ctypes

field = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")


def fixInp(inp):
    r = ""
    for i in inp:
        if i.isalpha():
            r += i.upper()
    return r


def encrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        else:
            pt = fixInp(text)
            keyVal = fixInp(key)
            matrixVals = []
            for c in keyVal:
                if c in field and c not in matrixVals:
                    matrixVals.append(c)
            for c in field:
                if c not in matrixVals:
                    matrixVals.append(c)
            matrix = []
            index = 0
            for rows in range(5):
                row = []
                for cols in range(5):
                    row.append(matrixVals[index])
                    index += 1
                matrix.append(row)
            rows = []
            col = []
            for letter in pt:
                bin = [(ix + 1, iy + 1) for ix, row in enumerate(matrix) for iy, i in enumerate(row) if i == letter]
                rows.append(bin[0][0])
                col.append(bin[0][1])

            final = rows + col
            final = "".join([str(i) for i in final])
            final = list((final[i:i + 2] for i in range(0, len(final), 2)))
            cipherText = ""
            for pairs in final:
                cipherText += matrix[int(pairs[0]) - 1][int(pairs[1]) - 1]

            return cipherText

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(text, key):
    try:
        if text == "" or key == "":
            ctypes.windll.user32.MessageBoxW(None, "No text/key entered!", "Error!", 0)
        else:
            pt = text.replace(" ", "").upper().replace("J", "I")
            keyVal = key.upper().replace(" ", "").replace("J", "I")
            matrixVals = []
            for c in keyVal:
                if c in field and c not in matrixVals:
                    matrixVals.append(c)
            for c in field:
                if c not in matrixVals:
                    matrixVals.append(c)

            matrix = []
            index = 0  # Start of indexing
            for rows in range(5):
                row = []
                for cols in range(5):
                    row.append(matrixVals[index])
                    index += 1
                matrix.append(row)
            location = []
            for letter in pt:
                bin = [(ix + 1, iy + 1) for ix, row in enumerate(matrix) for iy, i in enumerate(row) if i == letter]
                location.append(bin[0])
            final = [(str(i[0]), str(i[1])) for i in location]
            final = ["".join(i) for i in final]
            final = "".join(final)
            rows = final[:int(len(final) / 2)]
            col = final[int(len(final) / 2):]
            plain_text = ""

            for i in range(len(rows)):
                plain_text += matrix[int(rows[i]) - 1][int(col[i]) - 1]

            return plain_text

    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
