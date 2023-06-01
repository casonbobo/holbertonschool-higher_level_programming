#!/usr/bin/python3
"""
Rectangle
"""

class Rectangle:
    """ is a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int or type(height) is not int:
            raise TypeError("size must be an integer")
        if width < 0 or height < 0:
            raise ValueError("size must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def area(self):
        return(self.__height * self.__height)
    
    @property
    def width(self):
        return(self.__width)
    
    @property
    def height(self):
        return(self.__height)
    
    @property
    def x(self):
        return(self.__x)
    
    @property
    def y(self):
        return(self.__y)
    
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__width = value

    @x.setter
    def x(self, value):
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__x = value
    
    @y.setter
    def y(self, value):
        if type(value) is not int:
                raise TypeError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__y = value

