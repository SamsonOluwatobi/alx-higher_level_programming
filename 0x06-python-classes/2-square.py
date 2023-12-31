#!/usr/bin/python3

"""Square Class.
This module contains a class that defines a square.
Usage Example:
    Square = __import__('2-square').Square
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """A simple class to represent a square.

    Attributes:
        __size (int): The size of every side of the square.
        Must be a positive integer value.

    Methods:
        __init__(self, size): Initializes a new Square
        instance with the given size.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
