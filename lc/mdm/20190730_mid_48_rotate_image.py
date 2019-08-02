#-*- coding: utf-8 -*-
from typing import List
import math


class Solution:
    def __init__(self):
        self.__di = 'right'

    def shift(self, matrix, s, e, i, j):
        if self.__di == 'right':
            self.__di == 'down'
        elif self.__di == 'down':
            self.__di == 'left'
        elif self.__di == 'left':
            self.__di == 'up'
        elif self.__di == 'up':
            self.__di == 'right'
        else:
            assert(True)

    def next(self, matrix, s, e, i, j):
        if self.__di == 'right':
            j += 1
        elif self.__di == 'down':
            i -= 1
        elif self.__di == 'left':
            j -= 1
        elif self.__di == 'up':
            i += 1
        else:
            assert(True)

        if self.is_valide(matrix, s, e, i, j):
            pass
        else:
            # revert
            if self.__di == 'right':
                j -= 1
            elif self.__di == 'down':
                i += 1
            elif self.__di == 'left':
                j += 1
            elif self.__di == 'up':
                i -= 1
            else:
                assert(True)
            self.shift(matrix, s, e, i, j)
            self.next(matrix, s, e, i, j)

        return (i, j)


    def is_valide(self, matrix, s, e, i, j):
        if i >= s and i <= e and j >=s and j <= e:
            return True
        else:
            return False

    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(int(math.ceil(rows/2))):
            s = r
            e = (cols - r) - 1
            print("s:%s, e:%s" % (s, e))
            print("left upper corner:%s" % matrix[s][s])
            print("right upper corner:%s" % matrix[s][e])


class Solution():
    def show(self, mat: List[List[int]]):
        for row in mat:
            print (row)


    def rotate(self, mat: List[List[int]]) -> None:
        N = len(mat)
        for x in range(0, int(N/2)):

            # Consider elements in group
            # of 4 in current square
            for y in range(x, N-x-1):

                # store current cell in temp variable
                temp = mat[x][y]
                mat[x][y] = mat[N-1-y][x] # left-bottom to left-top
                mat[N-1-y][x] = mat[N-1-x][N-1-y]
                mat[N-1-x][N-1-y] = mat[y][N-1-x]
                mat[y][N-1-x] = temp
                #
                # # move values from right to top
                # mat[x][y] = mat[y][N-1-x]
                #
                # # move values from bottom to right
                # mat[y][N-1-x] = mat[N-1-x][N-1-y]
                #
                # # move values from left to bottom
                # mat[N-1-x][N-1-y] = mat[N-1-y][x]
                #
                # # assign temp to left
                # mat[N-1-y][x] = temp



matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]

matrix = [
    [ 1, 2, 3, 4],
    [ 5, 6, 7, 8],
    [ 9,10,11,12],
    [12,13,14,15]
]

# matrix = [
#     [ 5, 1, 9,11, 12],
#     [ 2, 4, 8,10, 91],
#     [13, 3, 6, 7, 92],
#     [15,14,12,16, 93],
#     [27,20,21,22, 94]
#
# ]

Solution().rotate(matrix)
Solution().show(matrix)
