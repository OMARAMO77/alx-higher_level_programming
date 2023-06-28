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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False \
           or self.__check_indexes(position) is False \
           or self.__check_integers(position) is False \
           or self.__check_values(position) is False:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        if type(position[0]) is int and type(position[1]) is int:
            return True

        return False

    def __check_values(self, position):
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """Return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.size):
                for b in range(self.size):
                    print("#", end="")
                print()
