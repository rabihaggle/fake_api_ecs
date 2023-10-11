import random
import string
def information(str_aa):
    length = 100
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))