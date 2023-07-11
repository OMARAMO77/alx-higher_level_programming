#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """Inherits from int base class"""
    def __init__(self, value):
        """Initializes the value"""
        self.value = value

    def __ne__(self, x):
        """not equal to comparison"""
        if self.value is x:
            return True
