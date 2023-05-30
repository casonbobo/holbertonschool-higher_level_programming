#!/usr/bin/python3
"""this is a file to read other files"""


def read_file(filename=""):
    """this is a function to read a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
