#!/usr/bin/python3
class Square:
    """Creating an empty class called Square"""

    def __init__(self, size=0):
        """Defining object called Square."""
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
        """Setting size attribute."""
        
    def area(self):
        """Defining object called area."""
        return (self.__size ** 2)
