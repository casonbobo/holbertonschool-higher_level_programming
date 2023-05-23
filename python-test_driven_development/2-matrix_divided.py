def matrix_divided(matrix, div):
    if (isinstance(matrix, list) and all(isinstance(row, list)
        and all(isinstance(element, int) for element in row) for row in matrix)):
        for row in matrix:
            for element in row:
                new_matrix = round(element / div, 2)
