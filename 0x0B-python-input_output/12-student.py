#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation of class attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json method that returns dict representations of attributes
        """
        if type(attrs) is list and attrs is not None:
            new_dict = {}
            for key, value in self.__dict__.items():
                for i in range(len(attrs)):
                    if key == attrs[i]:
                        new_dict[key] = self.__dict__[key]
            return new_dict
        else:
            return self.__dict__
