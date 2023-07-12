#!/usr/bin/python3
"""pascal_triangle function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    my_list = [[0 for b in range(a + 1)] for a in range(n)]
    for a in range(n):
        for b in range(a + 1):
            if b == 0:
                my_list[a][b] = 1
            elif b == a:
                my_list[a][b] = 1
            else:
                my_list[a][b] = my_list[a-1][b] + my_list[a-1][b-1]
    return my_list
