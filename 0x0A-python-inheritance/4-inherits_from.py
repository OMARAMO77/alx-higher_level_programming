#!/usr/bin/python3
"""inherits_from function"""


def inherits_from(obj, a_class):
    """
        Checks if the object is instance of a class inherited
        from directly or indirectly
    """
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
