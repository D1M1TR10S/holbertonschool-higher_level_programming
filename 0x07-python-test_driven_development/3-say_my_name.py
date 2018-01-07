#!/usr/bin/python3
"""
This is the 3-say_my_name module.
It supplies one function, say_my_name.
"""
def say_my_name(first_name, last_name=""):
    """
    Prints the first_name followed by the last_name
    """
    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    first_name = first_name.strip()
    last_name = last_name.strip()
    print("My name is {} ".format(first_name), end="")
    print("{}".format(last_name))
