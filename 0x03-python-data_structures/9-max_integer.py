#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    for a in range(len(my_list) - 1):
        if my_list[a] > max:
            max = my_list[a]
    return max
