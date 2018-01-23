#!/usr/bin/python3
"""
Creating a class called Square that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class inheriting from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiating Square
        """
        self.size = size
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Over-writing __str__ function of super class
        """
        return("[Square] ({}) {}/{} - {}".format
              (self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Getter for size
        """
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Updates the values of class attributes
        """
        sq_keys = ["id", "size", "x", "y"]

        for index, value in enumerate(args):
            setattr(self, sq_keys[index], value)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
