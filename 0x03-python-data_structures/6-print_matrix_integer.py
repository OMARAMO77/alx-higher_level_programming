#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lenght = len(row)
        for a in range(lenght):
            if a != lenght - 1:
                print("{:d}".format(row[a]), end=' ')
            else:
                print("{:d}".format(row[a]), end='')
        print()
