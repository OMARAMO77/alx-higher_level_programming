#!/usr/bin/python3
"""the class Rectangle"""
from .base import Base


class Rectangle(Base):
    """Defining the class that inherits form Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            width (int): width of the ractangle
            height (int): height of rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        ---
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        ---
        """
        self.__width = value

    @property
    def height(self):
        """
        ---
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        ---
        """
        self.__height = value

    @property
    def x(self):
        """
        ---
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        ---
        """
        self.__x = value

    @property
    def y(self):
        """
        ---
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        ---
        """
        self.__y = value
