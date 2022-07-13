import string
import math

from matplotlib.pyplot import table

def decrypt(msg, shift):
    shift %= 26
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    alpha = string.ascii_letters

    alphaShifted = lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift]

    table = str.maketrans(alphaShifted, alpha)

    return msg.translate(table)

