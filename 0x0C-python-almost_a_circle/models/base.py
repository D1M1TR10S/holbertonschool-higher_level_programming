#!/usr/bin/python3
"""Module for Base class
"""


class Base:
    """My Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
