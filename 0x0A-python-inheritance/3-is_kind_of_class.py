#!/usr/bin/python3
"""
Module testing an object to see which class it belongs to or is inherited from
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance in or inherited from a_class.
    Otherwisee, return False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
