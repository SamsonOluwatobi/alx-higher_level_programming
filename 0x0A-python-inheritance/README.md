# 0x0A. Python - Inheritance

## Overview

This project covers the concept of inheritance in Python, a powerful object-oriented programming feature. The tasks involve creating classes, defining methods, and exploring the relationships between different classes. Below is an overview of the tasks and their respective objectives.

## Tasks and Learning Objectives

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object.

**Learning Objectives:**
- Understand how to retrieve and list attributes and methods of an object in Python.

### 1. My list
Write a class `MyList` that inherits from the built-in `list` class and includes a method to print the sorted list.

**Learning Objectives:**
- Implement a class that inherits from a built-in class.
- Define a method in the derived class to perform a specific operation on the inherited data structure.

### 2. Exact same object
Write a function that returns `True` if the object is exactly an instance of the specified class; otherwise, `False`.

**Learning Objectives:**
- Learn how to check if an object is an instance of a specific class.

### 3. Same class or inherit from
Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise, `False`.

**Learning Objectives:**
- Understand how to check if an object is an instance of a class or its subclasses.

### 4. Only sub class of
Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise, `False`.

**Learning Objectives:**
- Learn how to check if an object is an instance of a subclass.

### 5. Geometry module
Write an empty class `BaseGeometry` to serve as the base class for geometric shapes.

**Learning Objectives:**
- Create a base class for future geometric shapes.

### 6. Improve Geometry
Enhance the `BaseGeometry` class by adding a method that raises an exception with the message "area() is not implemented."

**Learning Objectives:**
- Implement an abstract method in a base class.

### 7. Integer validator
Extend the `BaseGeometry` class by adding a method to validate the type and value of an integer.

**Learning Objectives:**
- Validate input parameters within a class method.

### 8. Rectangle
Create a class `Rectangle` that inherits from `BaseGeometry` and includes instantiation with width and height.

**Learning Objectives:**
- Implement a derived class with specific attributes and methods.

### 9. Full rectangle
Enhance the `Rectangle` class by adding the implementation of the `area()` method and updating the string representation.

**Learning Objectives:**
- Implement a method in a derived class and override the `__str__` method.

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` and includes instantiation with size.

**Learning Objectives:**
- Create a derived class with specific attributes and methods.

### 11. Square #2
Extend the `Square` class by updating the string representation to include "Square" in the output.

**Learning Objectives:**
- Override the `__str__` method in a derived class.

### 12. My integer (Advanced)
Write a class `MyInt` that inherits from `int` and inverts the behavior of the equality operators `==` and `!=`.

**Learning Objectives:**
- Create a class that modifies the behavior of operators in a built-in class.

### 13. Can I? (Advanced)
Write a function that adds a new attribute to an object if it's possible, raising a `TypeError` exception otherwise.

**Learning Objectives:**
- Handle object attributes dynamically within a function.
