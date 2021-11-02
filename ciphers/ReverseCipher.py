import ctypes


def reverse(text):
    try:
        if text == "":
            ctypes.windll.user32.MessageBoxW(None, "No text entered!", "Error!", 0)
        else:
            res = [text[::-1]]
            return ''.join(res)
    except ValueError:
        ctypes.windll.user32.MessageBoxW(None, "Invalid Entry", "Error!", 0)
