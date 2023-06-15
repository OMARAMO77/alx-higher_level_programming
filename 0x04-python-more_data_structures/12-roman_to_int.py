#!/usr/bin/python3
def roman_to_int(roman_string):
    romstr = roman_string
    total = 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if romstr and type(romstr) == str:
        for a in range(len(romstr)):
            if a > 0 and dict[romstr[a]] > dict[romstr[a - 1]]:
                total += dict[romstr[a]] - (2 * dict[romstr[a - 1]])
            else:
                total += dict[romstr[a]]
        return total
    return 0
