#!/usr/bin/python3
"""add_attribute function"""


def add_attribute(self, attribute, value):
    """Add attribute into the class if it's possible"""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
