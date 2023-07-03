#!/usr/bin/python3
"""A rectangle module"""


class Rectangle:
    """An Rectangle with Width and height"""

    def __init__(self, width=0, height=0):
        """Initialized Rectangle

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the size of width of the retangle

        Returns:
            width (int)
        """

        return self.__width

    @width.setter
    def width(self, width):
        """Changes the width of the rectangle

        Args:
            width (int): New width
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Gets the size of height of the retangle

        Returns:
            height (int)
        """

        return self.__height

    @height.setter
    def height(self, height):
        """Changes the height of the rectangle
        Args:
            height (int): New height
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle

        Returns:
            area (int)
        """

        return self.__width * self.__height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle

        Returns:
            perimeter (int)
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """return rectangle in a user readable form

        Returns:
            rectangle(string)
        """

        str = ""

        for i in range(self.__height):
            str += "#" * self.__width
            if i < self.height - 1:
                str += "\n"

        return str

    def __repr__(self):
        """return rectangle in a string format

        Returns:
            rectangle (string)
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
