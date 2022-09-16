import string
import random


def status_genrator(size =7, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
