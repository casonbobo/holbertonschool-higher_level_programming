#!/usr/bin/python3
"""
square
"""


class Square:
    """this class defines a square"""
    def __init__(self, size=0):
        if size != type(int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    pass
