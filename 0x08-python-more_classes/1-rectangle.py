#!/usr/bin/python3
"""A rectangle module that does nothing"""


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
        """Returns the width of the Rectangle"""

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
