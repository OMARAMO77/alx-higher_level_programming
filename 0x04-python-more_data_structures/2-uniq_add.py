#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    for a in set(my_list):
        s += a
    return s
