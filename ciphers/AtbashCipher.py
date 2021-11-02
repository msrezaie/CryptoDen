import ctypes

field = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
         'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
         'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
         'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
         'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A'}

values = []
for k, v in field.items():
    values.append(v)


def atbash(text):
    try:
        if text == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered!", "Error!", 0)
        else:
            res = []
            for i in text.upper():
                if i not in values:
                    res.append(i)
                else:
                    res.append(field[i])

            return ''.join(res)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)