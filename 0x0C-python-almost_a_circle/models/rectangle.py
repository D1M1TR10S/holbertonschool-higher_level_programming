#!/usr/bin/python3
"""Module for class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle class with private iinstance attributes
        """
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        super().__init__(id)

    def __str__(self):
        """Printing parameters to stdout
        """
        return("[Rectangle] ({}) {}/{} - {}/{}".format
              (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns arguments to class attributes
        """
        keys = ["id", "width", "height", "x", "y"]

        for index, value in enumerate(args):
            setattr(self, keys[index], value)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setting value size."""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting height value."""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setting y value."""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setting x value."""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    def area(self):
        """Defining the area method of Rectangle
        """
        return (self.width * self.height)

    def display(self):
        """Prints the square to stdout in # symbols
        """
        for drop in range(self.y):
            print()
        for y in range(self.height):
            for shift in range(self.x):
                print(' ', end="")
            for x in range(self.width):
                print("#", end="")
            print()

    def to_dictionary(self):
        """
        Returns a dictionary representation of Rectangle
        """
        d = {}
        attributes = ['x', 'y', 'id', 'height', 'width']
        for key in attributes:
            value = getattr(self, key)
            d.update({key: value})
        return d
