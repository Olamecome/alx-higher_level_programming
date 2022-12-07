#!/usr/bin/python3

if __name__ == "__main__":
    def square_matrix_simple(matrix=[]):
        new_matrix = list()
        for row in matrix:
            for item in row:
                new_matrix[matrix.index(row)][matrix.index(item)] = item * item

        return new_matrix
