#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "A rectangle"

    def __init__(self, width, height):
        """make a rectangle"""
        self.interger_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area"""
        return self.__height * self.__width

    def __str__(self):
        """return the count and str of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
