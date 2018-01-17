#!/usr/bin/python3
"""
Module with Rectangle() class which inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class
    """
    def __init__(self, width, height):
        """
        Instantiates Rectangle and defines attributes called width and height.
        Sends width and height into integer validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
