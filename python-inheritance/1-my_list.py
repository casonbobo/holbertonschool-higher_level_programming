#!/usr/bin/python3
"""
this is a funuction to sort a list without altering the list
"""


class MyList(list):
    """ this is the class. duh"""
    def print_sorted(self):
        print(sorted(self))
