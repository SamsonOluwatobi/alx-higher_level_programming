#!/usr/bin/python3
class Square:
    """A simple class to represent a square.

    Attributes:
        __size (int): The size of every side of the square.
        Must be a positive integer value.

    Methods:
        __init__(self, size): Initializes a new Square
        instance with the given size.
        size(self): Getter for the size attribute.
        size(self, value): Setter for the size attribute.
        area(self): Computes the area of the square.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance with the given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes the area of the square."""
        return self.__size ** 2
