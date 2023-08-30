import string
import random

def random_password_ex_symbols():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    max=random.choice([8,9,10,11,12,13,14,15,16,17,18,19,20])
    word=""    
    for x in range(0, max):
        word +=random.choice(chars)
    return word



def random_password_wit_symbols():
    chars = string.printable
    max=random.choice([8,9,10,11,12,13,14,15,16,17,18,19,20])
    word=""
    for x in range(0,max):
        word +=random.choice(chars)
    return word