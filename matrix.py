    # -*- coding: utf-8 -*-
"""
Created on Wed May 10 20:49:06 2023

@author: Venom
"""

import random
import numpy as np

# matrix = [[random.randint(0, 1) for _ in range(8)] for _ in range(8)]

# # Print the matrix
# for row in matrix:
#     print(row)
    
    
a = [[1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0]]

b = [[1, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 0, 0]]

def sub(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] - matrix2[i][j]
    
    return result

result=sub(b,a)
# print(result)

def search(array, target):
    letters = {
        '0': 'a',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h'
    }
    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == target:
                i_letter = letters[str(i)]
                move = i_letter + str(j)
                return(move)
            

new = str(search(result, -1))
ori = str(search(result, 1))

player_move=ori+new
# print(player_move)
