#!/usr/bin/python3
def uppercase(str):
    for a in str:
        c = ord(a)
        if c >= 97 and c <= 122:
            c -= 32
        print("{:c}".format(c), end="")
    print()
