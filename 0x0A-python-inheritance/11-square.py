#!/usr/bin/python3
"""
My module for squares
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class called Square inheriting from Rectangle
    """
    def __init__(self, size):
        """
        Instantiating square
        """
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Overriding str function
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
