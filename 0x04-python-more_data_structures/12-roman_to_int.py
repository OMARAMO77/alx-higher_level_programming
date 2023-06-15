def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return (0)
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for lett in roman_string:
        if lett in dict:
            res += dict[lett]
            if dict[lett] > prev:
                res -= - 2 * prev
            prev = dict[lett]
        else:
            return (0)
    return res
