import ctypes

field = {
    '0': ' ', '11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e', '21': 'f', '22': 'g', '23': 'h', '24': 'i' or 'j',
    '25': 'k', '31': 'l',
    '32': 'm', '33': 'n', '34': 'o', '35': 'p', '41': 'q', '42': 'r', '43': 's', '44': 't', '45': 'u', '51': 'v',
    '52': 'w', "53": 'x',
    '54': 'y', '55': 'z'
}

values = []
key = []
for k, v in field.items():
    values.append(v)
    key.append(k)


def encrypt(text):
    try:
        if text == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered!", "Error!", 0)
        else:
            keys = []
            for i in text:
                if i not in values:
                    keys.append(i)
                else:
                    if i == " ":
                        row = 0
                        cipher = row
                    else:
                        row = int((ord(i) - ord('a')) / 5) + 1
                        col = int((ord(i) - ord('a')) % 5) + 1
                        cipher = str(row) + str(col)
                        if int(cipher) >= 25:
                            cipher = int(cipher) - 1
                            if int(cipher) == 30 or int(cipher) == 40 or int(cipher) == 50 or int(cipher) == 60:
                                cipher = int(cipher) - 5

                    keys.append(int(cipher))

            return ' '.join(str(x) for x in keys)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)


def decrypt(cipher):
    cipher = cipher.split()
    try:
        res = []
        for i in cipher:
            if i in key:
                res.append(field[i])
            else:
                res.append(i)

        return ''.join(res)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
