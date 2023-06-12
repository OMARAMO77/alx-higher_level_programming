#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    maxval = my_list[0]
    for a in range(len(my_list) - 1):
        if my_list[a] > maxval:
            maxval = my_list[a]
    return maxval
