#!/usr/bin/python3
"""the class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the class that inherits form Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance attributes
        Args:
            size (int): size of rectangle
            x (int): x axis of rectangle
            y (int): y axis of the rectangle
            id (int): id of the rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        ---
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        ---
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        ---
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        ---
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

        if len(args) == 0 and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        ---
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
