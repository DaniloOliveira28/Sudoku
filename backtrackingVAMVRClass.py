#!/usr/bin/python
# -*- coding: utf-8 -*-
from copy import deepcopy


class btVAMVR():
    def __init__(self, bl=1000000, at=0):
        self.BREAK_LIMIT = bl
        self.ASSIGNMENT_TENTATIVES = at

    def get_assignment_tentatives(self):
        return self.ASSIGNMENT_TENTATIVES

    def find_next_cell_to_fill(self, assignment, i, j):
        cell = {}
        cell["x"] = 0
        cell["y"] = 0
        cell["set"] = set()
        first = True
        for x in range(0, 9):
            for y in range(0, 9):
                if type(assignment[x][y]) is set:
                    if first is True:
                        cell["x"] = x
                        cell["y"] = y
                        cell["set"] = assignment[x][y]
                        first = False
                    else:
                        if len(assignment[x][y]) < len(cell["set"]):
                            cell["x"] = x
                            cell["y"] = y
                            cell["set"] = assignment[x][y]
                        elif len(assignment[x][y]) == len(cell["set"]):
                            pass

        if len(cell["set"]) > 0:
            return cell["x"], cell["y"]

        return -1, -1

    def update_values(self, assignment, i, j, candidate):
        i_modified = []
        j_modified = []
        for column in range(0, 9):
            if column == j:
                continue
            if type(assignment[i][column]) is set:
                if candidate in assignment[i][column]:
                    assignment[i][column].remove(candidate)
                    i_modified.append(i)
                    j_modified.append(column)

        for row in range(0, 9):
            if row == i:
                continue
            if type(assignment[row][j]) is set:
                if candidate in assignment[row][j]:
                    assignment[row][j].remove(candidate)
                    i_modified.append(row)
                    j_modified.append(j)

        secTopX, secTopY = 3 * (i/3), 3 * (j/3)
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if x == i and y == j:
                    continue
                if type(assignment[x][y]) is set:
                    if candidate in assignment[x][y]:
                        assignment[x][y].remove(candidate)
                        i_modified.append(x)
                        j_modified.append(y)
        return i_modified, j_modified

    def restore_values(self, assignment, i_modified, j_modified, candidate):

        for item in range(0, len(i_modified)):
            assignment[i_modified[item]][j_modified[item]].add(candidate)

    def is_valid(self, assignment, i, j, candidate):
        # Verificação linha, coluna, grupo
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
            else:
                return False
        else:
            return False

        # Verificação Adiante!
        for column in range(0, 9):
            if column == j:
                continue
            if type(assignment[i][column]) is set:
                if candidate in assignment[i][column] and \
                        len(assignment[i][column]) == 1:

                    return False

        for row in range(0, 9):
            if row == i:
                continue
            if type(assignment[row][j]) is set:
                if candidate in assignment[row][j] and \
                        len(assignment[row][j]) == 1:

                    return False

        secTopX, secTopY = 3 * (i/3), 3 * (j/3)
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if x == i and y == j:
                    continue
                if type(assignment[x][y]) is set:
                    if candidate in assignment[x][y] and \
                            len(assignment[x][y]) == 1:
                        return False
        return True

    # % returns a solution (True) or failure (None)
    def recursive_backtracking(self, assignment, i=0, j=0):

        i, j = self.find_next_cell_to_fill(assignment, i, j)

        if i == -1:
            return True

        rangeValues = assignment[i][j]
        for value_candidate in rangeValues:
            if self.is_valid(assignment, i, j, value_candidate) is True:
                if self.ASSIGNMENT_TENTATIVES > self.BREAK_LIMIT:
                    raise ValueError("Numero de atribuicoes excede"
                                     " limite maximo",
                                     self.ASSIGNMENT_TENTATIVES)
                assignment[i][j] = value_candidate
                i_modified, j_modified = self.update_values(assignment,
                                                            i,
                                                            j,
                                                            value_candidate)
                # print assignment
                self.ASSIGNMENT_TENTATIVES += 1

                # sys.exit(0)
                if self.recursive_backtracking(assignment, i, j) is True:
                    # print "FOI"
                    return True
                assignment[i][j] = rangeValues
                self.restore_values(assignment,
                                    i_modified,
                                    j_modified,
                                    value_candidate)

        return None

    def get_valid_values(self, sudokuCSP, i, j):
        initialSet = set(range(1, 10))
        for column in range(0, 9):
            if sudokuCSP[i][column] in initialSet:
                initialSet.remove(sudokuCSP[i][column])
        for row in range(0, 9):
            if sudokuCSP[row][j] in initialSet:
                initialSet.remove(sudokuCSP[row][j])
        secTopX, secTopY = 3 * (i/3), 3 * (j/3)
        for x in range(secTopX, secTopX+3):
            for y in range(secTopY, secTopY+3):
                if sudokuCSP[x][y] in initialSet:
                    initialSet.remove(sudokuCSP[x][y])
        return initialSet

    def read(self, sudokuCSP):
        """ Read field into state (replace 0 with set of possible values) """
        state = deepcopy(sudokuCSP)
        for i in range(9):
            for j in range(9):
                cell = state[i][j]
                if cell == 0:
                    state[i][j] = self.get_valid_values(sudokuCSP, i, j)
        return state

    def solve(self, sudokuCSP):
        """ Solve sudoku """
        state = self.read(sudokuCSP)
        # print state
        self.recursive_backtracking(state)
        # print state
        return state
