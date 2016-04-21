#!/usr/bin/python
# -*- coding: utf-8 -*-
from copy import deepcopy


class btDefault():
    def __init__(self, bl=1000000, at=0):
        self.BREAK_LIMIT = bl
        self.ASSIGNMENT_TENTATIVES = at

    def get_assignment_tentatives(self):
        return self.ASSIGNMENT_TENTATIVES

    def find_next_cell_to_fill(self, assignment, i, j):

        for x in range(0, 9):
            for y in range(0, 9):
                if assignment[x][y] == 0:
                    return x, y

        return -1, -1

    def is_valid(self, assignment, i, j, candidate):
        row = all([candidate != assignment[i][x] for x in range(9)])
        if row is True:
            column = all([candidate != assignment[x][j] for x in range(9)])
            if column is True:
                # finding the top left x,y
                # co-ordinates of the section containing the i,j cell
                secTopX, secTopY = 3 * (i/3), 3 * (j/3)
                for x in range(secTopX, secTopX+3):
                    for y in range(secTopY, secTopY+3):
                        if assignment[x][y] == candidate:
                            return False
                return True
        return False

    # % returns a solution (True) or failure (None)
    def recursive_backtracking(self, assignment, i=0, j=0):

        i, j = self.find_next_cell_to_fill(assignment, i, j)

        if i == -1:
            return True

        for value_candidate in range(1, 10):
            if self.is_valid(assignment, i, j, value_candidate) is True:
                if self.ASSIGNMENT_TENTATIVES > self.BREAK_LIMIT:
                    raise ValueError("Numero de atribuicoes excede"
                                     " limite maximo",
                                     self.ASSIGNMENT_TENTATIVES)

                assignment[i][j] = value_candidate
                self.ASSIGNMENT_TENTATIVES += 1

                # sys.exit(0)
                if self.recursive_backtracking(assignment, i, j) is True:
                    return True
                assignment[i][j] = 0

        return None

    def read(self, sudokuCSP):
        """ Read field into state (replace 0 with set of possible values) """
        state = deepcopy(sudokuCSP)

        return state

    def solve(self, sudokuCSP):
        """ Solve sudoku """
        state = self.read(sudokuCSP)
        # print state
        self.recursive_backtracking(state)
        # print state
        return state
