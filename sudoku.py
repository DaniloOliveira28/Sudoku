#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import getopt
import unicodecsv
import csv
import time
import backtrackingClass
import backtrackingVAClass
import backtrackingVAMVRClass
import cowsay


def formatSudoku(sudoku):
    return ('\n'.join([''.join(['{:1} '.format(item) for item in row])
            for row in sudoku]))


def solveSudoku(mode, inputItem):
    resultSudoku = inputItem
    assignment_tentatives = 0

    if mode == "a":
        btClass = backtrackingClass.btDefault()
        resultSudoku = btClass.solve(inputItem)
        assignment_tentatives = btClass.get_assignment_tentatives()
    elif mode == "b":
        btClass = backtrackingVAClass.btVA()
        resultSudoku = btClass.solve(inputItem)
        assignment_tentatives = btClass.get_assignment_tentatives()
    elif mode == "c":
        btClass = backtrackingVAMVRClass.btVAMVR()
        resultSudoku = btClass.solve(inputItem)
        assignment_tentatives = btClass.get_assignment_tentatives()

    return resultSudoku, assignment_tentatives


def usage():
    print "Usage: sudoku.py -p [a | b | c] [--cowmode]"
    print "a : Verificação Adiante"
    print "b : Verificação Adiante"
    print "c : Verificação Adiante e MVR"
    print "--cowmode: Cow Heuristic"


def main(argv):
    # configuracao de flags
    cowmode = False
    heuristica = None
    try:
        opts, args = getopt.getopt(argv, "hp:", ["cowmode"])
    except getopt.GetoptError:
        print "sudoku.py -h -p <heuristica>"
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            usage()
            sys.exit(0)
        elif opt in ("-p"):
            heuristica = arg
        elif opt in ("--cowmode"):
            cowmode = True

    if heuristica is None:
        usage()
        sys.exit(2)

    # analysis data
    if heuristica is not None and heuristica == "b":
        analysisFile = open("./Data/bVerAdi.csv", "wa")
    elif heuristica is not None and heuristica == "c":
        analysisFile = open("./Data/cbVerAdiMVR.csv", "wa")
    else:
        analysisFile = open("./Data/aSemHeuristica.csv", "wa")

    w = unicodecsv.writer(analysisFile,
                          encoding='UTF-8',
                          delimiter=';',
                          quotechar='"',
                          quoting=csv.QUOTE_ALL)
    w.writerow(["ASSIGNMENT_TENTATIVES", "TIME"])
    # reading the input file
    sudokuFile = open("./Data/entrada.txt", "r")
    first_line = sudokuFile.readline()
    first_line = int(first_line)
    inputSet = []
    for x in range(0, first_line):

        input = []
        for line in sudokuFile:
            if line != "\n":
                line = line.replace('\n', '')
                line = line.split(" ")
                line = map(int, line)
                input.append(line)
            else:
                inputSet.append(input)
                # print "input"
                # print " "
                input = []
                break
    inputSet.append(input)
    # print len(inputSet)

    # My code here
    for inputItem in inputSet:
        # if cowmode is True:
        #     print cowsay.CowSay().cowsay(formatSudoku(inputItem), 18)
        # else:
        #     print formatSudoku(inputItem)
        # btClass = backtrackingClass.btDefault()
        # formatSudoku(state)
        try:
            start_time = time.clock()
            result, at = solveSudoku(heuristica, inputItem)
            # resultSudoku = btClass.solve(inputItem)
            elapsed_time = time.clock() - start_time

            if result is not None:
                w.writerow([at, elapsed_time])

                if cowmode is True:
                    print cowsay.CowSay().cowsay(formatSudoku(result), 18)
                else:
                    print formatSudoku(result)
                print
            else:
                if cowmode is True:
                    print cowsay.CowSay().cowsay("MUHHH")
                else:
                    print "Failure"
        except ValueError as error:
            elapsed_time = time.clock() - start_time
            w.writerow([error.args[1], elapsed_time])
            if cowmode is True:
                print cowsay.CowSay().cowsay(str(error.args[0]))
            else:
                print(error.args[0])
                print

# start Sudoku Solver
if __name__ == "__main__":

    main(sys.argv[1:])

