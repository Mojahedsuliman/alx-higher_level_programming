#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for in range(len(matrix)):
        for i in range(len(matrix[in])):
            print("{:d}".format(matrix[in][i]), end="")
            if i != (len(matrix[in]) - 1):
                print(" ", end="")
