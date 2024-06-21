# 0x13. Javascript - Objects, Scopes and Closures

## About

This project aims to reinforce understanding of fundamental concepts in JavaScript, including:

- Object creation
- Usage of `this` keyword
- Understanding of `undefined`
- Importance of variable type and scope
- Concept of closures
- Prototype chain
- Object inheritance

## Tasks

### 0. [Rectangle #0](./0-rectangle.js)

Create an empty class Rectangle using ES6 class notation.

### 1. [Rectangle #1](./1-rectangle.js)

Define a class Rectangle using ES6 class notation with:
- Constructor that takes arguments `w` (width) and `h` (height).
- Initialize instance attributes `width` and `height` with `w` and `h`.
  
### 2. [Rectangle #2](./2-rectangle.js)

Enhance Rectangle #1:
- Validate if `w` or `h` is 0 or not a positive integer. If so, create an empty object.

### 3. [Rectangle #3](./3-rectangle.js)

Enhance Rectangle #2:
- Add an instance method `print()` that prints the rectangle using the character 'X'.

### 4. [Rectangle #4](./4-rectangle.js)

Enhance Rectangle #3:
- Add instance methods:
  - `rotate()` to exchange the width and height of the rectangle.
  - `double()` to multiply the width and height of the rectangle by 2.

### 5. [Square #0](./5-square.js)

Create a class Square that inherits from Rectangle #4:
- Use ES6 `extends` and `super()` to inherit from Rectangle.
- Constructor takes one argument `size` and initializes both width and height of the rectangle to `size`.

### 6. [Square #1](./6-square.js)

Enhance Square #0:
- Add an instance method `charPrint(c)` that prints the rectangle using the character `c`. If `c` is undefined, use 'X'.

### 7. [Occurrences](./7-occurrences.js)

Implement a function `nbOccurences`:
- Prototype: `exports.nbOccurences = function (list, searchElement)`
- Returns the number of occurrences of `searchElement` in `list`.

### 8. [Esrever](./8-esrever.js)

Implement a function `esrever`:
- Prototype: `exports.esrever = function (list)`
- Returns a reversed version of `list` without using the built-in `reverse()` method.

### 9. [Log me](./9-logme.js)

Implement a function `logMe`:
- Prototype: `exports.logMe = function (item)`
- Prints the number of arguments already printed and the new argument value in the format `<number arguments already printed>: <current argument value>`.

### 10. [Number conversion](./10-converter.js)

Implement a function `converter`:
- Prototype: `exports.converter = function (base)`
- Converts a number from base 10 to another base passed as `base` without using `var`, `let`, or any new variable declaration.

### 11. [Factor index](./100-map.js)

Create a script that imports an array `list` from `100-data.js`:
- Use `map` to create a new array where each value equals the value of the initial list multiplied by its index.
- Print both the initial list and the new list.

### 12. [Sorted occurrences](./101-sorted.js)

Create a script that imports a dictionary `dict` from `101-data.js`:
- Computes a new dictionary where:
  - Keys are numbers of occurrences.
  - Values are lists of user IDs.
- Print the new dictionary.

### 13. [Concat files](./102-concat.js)

Create a script that concatenates two files:
- First argument: path of the first source file.
- Second argument: path of the second source file.
- Third argument: path of the destination file.

## Author

- **Lana Samson OLuwatobi** - (https://github.com/SamsonOluwatobi)
