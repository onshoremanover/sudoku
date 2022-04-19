#!/usr/local/bin/python3
#
#

from numpy.core.fromnumeric import trace
import pandas as pd
import numpy as np


a = np.array([[1,2,3,4,5,6],
              [2,3,4,5,6,7],
              [3,4,5,6,7,8]])

def test_subset(sudoku, row, col):
    """Tests if the value is in the row or column"""
    value = int([row][col])
    sub = sudoku[0:2, 0:3]
    return sub

def cut_out_subset(sudoku, row, col):
    klein = range(0,1)
    mittel = range(2,3)
    gross = range(3,5)
    if row in klein and col in gross:
        sudoku[0:2, 0:3] = 0
        return sudoku
    elif row in mittel and col in gross:
        sudoku[2:3, 0:3] = 0
        return sudoku




def main():
    """Main function"""
    matrix=cut_out_subset(a, 0, 4)
    print(matrix)



if __name__ == "__main__":
    main()