#!/usr/bin/python3

"""Square Class.
This module contains a class that defines a square.
Usage Example:
    Square = __import__('1-square').Square
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """Simple square class with his size as a field"""

    def __init__(self, size):
        """ Instance the class Square
            Arguments:
                @size: the size of every side of the Square"""
        self.__size = size
