#!/usr/bin/python3
"""
the tangle of rec
"""


class Rectangle:
    """this class defines a rec"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return(self.__width)

    @property
    def height(self):
        return(self.__height)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        string = ""
        if self.height == 0 or self.width == 0:
            return string
        for column in range(self.height):
            for row in range(self.width):
                string += '#'
            if column < self.height - 1:
                string += '\n'
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        return ("Bye rectangle...")
