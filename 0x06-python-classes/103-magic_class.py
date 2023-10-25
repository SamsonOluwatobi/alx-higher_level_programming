#!/usr/bin/python3

"""This module defines a MagicClass that represents a circle and
provides methods to compute its area and circumference.

The MagicClass has a private attribute __radius that must be a number,
and two methods:
- area(self): Computes the area of the circle.
- circumference(self): Computes the circumference of the circle.

Example:
    mc = MagicClass(3)
    print(mc.area())
    print(mc.circumference())

Classes:
    MagicClass: A class that represents a circle and provides
    methods to compute its area and circumference.
"""


class MagicClass:
    """A class that represents a circle and provides methods to compute
    its area and circumference."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass instance with the given radius.

        Args:
            radius (int or float): The radius of the circle. Defaults to 0.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * 3.141592653589793

    def circumference(self):
        """Computes the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * 3.141592653589793 * self.__radius
