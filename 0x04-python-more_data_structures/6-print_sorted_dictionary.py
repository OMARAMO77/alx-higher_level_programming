#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord = sorted(a_dictionary.items())
    for k, v in ord:
        print("{}: {}".format(k, v))
