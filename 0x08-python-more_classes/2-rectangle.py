#!/usr/bin/python3
"""
This is the Rectangle class
It provides several modules for the Rectangle
"""
class Rectangle:
    """
    Creating a class called Rectangle
    """

    def __init__(self, width=0, height=0):
        """Defining attributes called width and height."""
        self.__width = width
        """Setting width attribute."""
        self.__height = height
        """Setting height attribute."""

    @property
    def width(self):
        """Using getter for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setting value size."""
        if type(width) != int:
            print("width must be an integer", end="")
            raise TypeError
        elif width < 0:
            print("width must be >= 0", end="")
            raise ValueError
        else:
            self.__width = width
        """Setting width attribute."""

    @property
    def height(self):
        """Using getter for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting height value."""
        if type(height) != int:
            print("height must be an integer", end="")
            raise TypeError
        elif height < 0:
            print("height must be >= 0", end="")
            raise ValueError
        else:
            self.__height = height
        """Setting height attribute."""

    def area(self):
        """Defining object called area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Defining object called perimeter."""
        if width == 0 or height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)
