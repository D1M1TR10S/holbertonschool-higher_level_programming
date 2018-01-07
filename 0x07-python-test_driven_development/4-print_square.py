#!/usr/bin/python3
"""
This is the 4-print_square module.
It supplies one function, print_square.
"""
def print_square(size):
    """
    size is the size length of the square.
    size must be an int, otherwise raise TypeError
    with the message size must be an integer.
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0.
    if size is a float and is less than 0,
    raise a TypeError exception with the message size must be an integer.
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for y in range(size):
        for x in range(size):
            print("#", end="")
        print()
