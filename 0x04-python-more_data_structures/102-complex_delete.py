#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[k]
    return a_dictionary
