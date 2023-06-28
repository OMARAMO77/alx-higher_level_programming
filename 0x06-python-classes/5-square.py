#!/usr/bin/python3
"""Defining a class square"""


class Square:
    """The class Square"""

    def __init__(self, size=0):
        """Initializes a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

        """
        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.
        """
    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print()
        else:
            for a in range(self.size):
                for b in range(self.size):
                    print("#", end="")
                print()
