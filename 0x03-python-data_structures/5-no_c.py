#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for a in my_string:
        if a not in "cC":
            new_string += a
    return (new_string)
