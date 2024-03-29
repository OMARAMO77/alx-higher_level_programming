#!/usr/bin/python3
"""the class Rectangle"""
from models.base import Base


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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        ---
        """
        return self.__width * self.__height

    def display(self):
        """
        ---
        """
        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        ---
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        ---
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

        if len(args) == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        ---
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
