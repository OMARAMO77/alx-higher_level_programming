def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for lett in roman_string:
        val = dict.get(lett, 0)
        if val > prev:
            res += val - 2 * prev
        else:
            res += val
        prev = val
    return res
