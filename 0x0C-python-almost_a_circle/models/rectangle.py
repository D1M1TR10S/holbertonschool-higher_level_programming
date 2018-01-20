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

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @width.setter
    def width(self, width):
        """Setting value size."""
        self.__width = width

    @height.setter
    def height(self, height):
        """Setting height value."""
        self.__height = height

    @y.setter
    def y(self, y):
        """Setting y value."""
        self.__y = y

    @x.setter
    def x(self, x):
        """Setting x value."""
        self.__x = x
