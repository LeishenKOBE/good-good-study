import random
from tkinter import ALL

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_code(code_len=4):
    code = ''
    for _ in range(code_len):
        index = random.randrange(0, len(ALL_CHARS))
        code += ALL_CHARS[index]

    return code


print(generate_code(10))
