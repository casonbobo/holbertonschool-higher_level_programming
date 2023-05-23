#!/usr/bin/python3
""" 3 Print square"""


def print_square(size):
    """
    this prints a square. have we done this enough?
    """
    if type(size) is not int:
        if type(size) is float and size >= 0:
            size = int(size)
        else:
            raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print('#', end='')
        print()
