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

    def __str__(self):
        """
        ---
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
