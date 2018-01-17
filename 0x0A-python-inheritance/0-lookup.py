#!/usr/bin/python3
"""
Module for the lookup method
"""


def lookup(obj):
    """
    Returns a list of all the attributes and methods in the current class.
    """
    return (list(dir(obj)))
