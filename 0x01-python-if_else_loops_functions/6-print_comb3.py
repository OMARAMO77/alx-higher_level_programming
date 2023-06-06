#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if b > a:
            if b < 9 or a < 8:
                print(f"{:d}{:d}".format(a, b), end=", ")
            else:
                print(f"{:d}{:d}".format(a, b))
