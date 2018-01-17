#!/usr/bin/python3
"""
Module with a class called MyList that inherits from list
"""


class MyList(list):
    """
    Class inheriting from list
    """
    def print_sorted(self):
        """
        Print list of integers in ascending order
        """
        print(sorted(self))
