#!/usr/bin/python3
class Square:
    """Creating an empty class called Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Defining attribute called size."""
        self.__size = size
        self.__position = position
        """Setting size attribute."""

    @property
    def size(self):
        """Using getter for size."""
        return self.__size

    @size.setter
    def size(self, size):
        """Setting value size."""
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
        """Setting size attribute."""

    @property
    def position(self):
        """Using getter for starting position."""
        return self.__position

    @position.setter
    def position(self, position):
        """Setting position value."""
        if type(position) is not tuple:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = position
            """Setting position attribute."""

    def area(self):
        """Defining object called area."""
        return (self.__size ** 2)

    def my_print(self):
        """Print square in # symbols."""
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
