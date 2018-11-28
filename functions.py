from collections import Counter

def prime_num(s):
    if not s.isdigit():
        return False
    c = int(s)
    res = True
    for i in range(2,c):
        if c % i == 0:
            res = False
            break

    return res

def square(s):
    if not s.isdigit():
        return False
    c=int(s)
    return c**2
