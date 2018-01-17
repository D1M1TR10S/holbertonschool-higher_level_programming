#!/usr/bin/python3
"""
Module testing an object to see which class it belongs to or is inherited from
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance in or inherited from a_class.
    Otherwisee, return False
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
