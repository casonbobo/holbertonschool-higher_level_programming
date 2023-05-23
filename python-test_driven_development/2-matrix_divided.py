#!/usr/bin/python3
"""
takes a matrix and divides it by a passed number
"""
def matrix_divided(matrix, div):
    """
    OoooOOoo
    the matrix
    """
    if (isinstance(matrix, list) and all(isinstance(row, list)
        and all(isinstance(element, int) for element in row) for row in matrix)):
        for row in matrix:
            for element in row:
                new_matrix = round(element / div, 2)
