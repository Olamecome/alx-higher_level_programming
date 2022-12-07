#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = list()
    for row in matrix:
        new_matrix.append([item * item for item in row])

    return new_matrix
