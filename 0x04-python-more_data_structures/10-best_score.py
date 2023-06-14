#!/usr/bin/python3
def best_score(a_dictionary):
    maxval = 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > maxval:
                maxval = v
                key = k
        return key
