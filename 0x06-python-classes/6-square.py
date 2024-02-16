#!/usr/bin/python3

"""Square Class.
This module contains a class that defines a square.
Usage Example:
    Square = __import__('6-square').Square
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
"""


class Square:
    """Defines the blueprint of a square.
    Attribute:
        size (int): An integer representing the object size.
        position (int, int): The position of the new square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """An object constructor method."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not self.__is_a_valid_position(position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """Gets the size private attribute value.
        Returns:
            The size private attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size private attribute value.
        Validates the assignment of the size private attribute.
        Arg:
            value: the value to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position private attribute value.
        Returns:
            The position private attribute
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position private attribute value.
        Validates the assignment of the position private attribute.
        Arg:
            value: the value to be set
        """
        if self.__is_a_valid_position(value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """A public object method.
        Returns:
            The current square area
        """
        return self.__size**2

    def my_print(self):
        """Displays the square object with # character"""
        if not self.size:
            print()
        else:
            for spaces_Y in range(self.position[1]):
                print()
            for row in range(self.size):
                for spaces_X in range(self.position[0]):
                    print(" ", end="")
                for row in range(self.size):
                    print("#", end="")
                print()

    def __is_a_valid_position(self, positions):
        """ Check if a value can be a position by checking
            if @positions is a tuple of exactly two positive integers
            Return:
                    True if @positions is a valid position field
                    False otherwise"""
        if type(positions) is tuple\
                and len(positions) == 2\
                and type(positions[0]) is int\
                and type(positions[1]) is int\
                and positions[0] >= 0\
                and positions[1] >= 0:
            return True
        else:
            return False
