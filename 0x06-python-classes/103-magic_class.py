#!/usr/bin/python3
import math

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
    def __init__(self, radius=0):
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
