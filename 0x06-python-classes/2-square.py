#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """The class Square"""

    def __init__(self, size):
        """Initializes a new Square.
        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
