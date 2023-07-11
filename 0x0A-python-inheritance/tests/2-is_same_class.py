#!/usr/bin/python3
"""is_same_class function"""


def is_same_class(obj, a_class):
    """
        Checks if two objects are the same class
    """

    if type(obj) == a_class:
        return True

    return False
