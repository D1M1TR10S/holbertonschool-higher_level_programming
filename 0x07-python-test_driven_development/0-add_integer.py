#!/usr/bin/python3
"""
This is the add_integer module.
It supplies one function, add_integer. For example,

"""
def add_integer(a, b):
    """
    Return the sum of variables a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if a + 1 == a:
        raise OverflowError("a too large")
    if b + 1 == b:
        raise OverflowError("b too large") 
    return (int(a) + int(b))
