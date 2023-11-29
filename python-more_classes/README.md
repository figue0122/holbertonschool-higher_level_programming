# Rectangle Class 📐

## Description

This repository contains a Python class `Rectangle` that defines a rectangle with various properties and methods. The class is part of the Holberton School curriculum and consists of several stages, each building on the previous one.

## Table of Contents

1. **0-rectangle.py**
   - An empty class `Rectangle` that defines a rectangle.

2. **1-rectangle.py**
   - A class `Rectangle` with private attributes `width` and `height`, and their respective getter and setter methods.

3. **2-rectangle.py**
   - Extends the previous class by adding methods to calculate the area and perimeter of the rectangle.

4. **3-rectangle.py**
   - Enhances the class to include a string representation of the rectangle using the '#' character.

5. **4-rectangle.py**
   - Adds a method to the class that allows the use of the `eval()` function for recreation.

6. **5-rectangle.py**
   - Implements a message when an instance of `Rectangle` is deleted.

7. **6-rectangle.py**
   - Adds a class attribute `number_of_instances` to keep track of the number of instances created.

8. **7-rectangle.py**
   - Allows customization of the character used for string representation through the `print_symbol` class attribute.

9. **8-rectangle.py**
   - Adds a static method `bigger_or_equal` to compare two rectangles and return the one with the greater area.

10. **9-rectangle.py**
    - Introduces a class method `square` to create a square instance of the `Rectangle` class.

## Usage

```python
# Example Usage
from 9-rectangle import Rectangle

# Create a square instance
my_square = Rectangle.square(5)

# Print area and perimeter
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))

# Print the rectangle
print(my_square)

## Author
- [Miguel Figueroa](https://github.com/figue0122) 🚀