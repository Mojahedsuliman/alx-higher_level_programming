#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(matrix, list) or not isinstance(row, list) for row in matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not len(row) == len(matrix[0]) for row in matrix:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            divided_row.append(round(elem / div, 2))
        divided_matrix.append(divided_row)
    return (divided_matrix)
