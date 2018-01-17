#!/usr/bin/python3
"""
Module testing an object to see which class it belongs to
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is an instance in a_class.
    Otherwsie, return False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
