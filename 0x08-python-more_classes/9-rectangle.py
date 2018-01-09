#!/usr/bin/python3
"""This is the Rectangle class
It provides several modules for the Rectangle
"""


class Rectangle:
    """
    Creating a class called Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Defining attributes called width and height."""
        type(self).number_of_instances += 1
        """Counting number of instances."""
        self.__width = width
        """Setting width attribute."""
        self.__height = height
        """Setting height attribute."""

    def __str__(self):
        """Creating a rectangle of # symbols."""
        string = ""
        if self.__width != 0 and self.__height != 0:
            for y in range(self.height):
                for x in range(self.width):
                    string += str(self.print_symbol)
                if y < (self.height - 1):
                    string += '\n'
        return (string)

    def __repr__(self):
        """Return a string representation of Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Detect when an instance of Rectangle is deleted."""
        print('Bye rectangle...')
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Defining class method called square."""
        width = size
        height = size
        squared = cls(width, height)
        return squared

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def height(self):
        """Getter for height."""
        return self.__height

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
        return (self.width * self.height)

    def perimeter(self):
        """Defining object called perimeter."""
        if self.width == 0 or self.height == 0:
            return (0)
        else:
            return ((self.width + self.height) * 2)
