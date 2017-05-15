#!/usr/bin/python2.7.2
import sys

import solver

numbers = [4, 0, 3, 8, 6, 7, 1, 2, 5]
s = solver.Solver(sys.argv[1])
s.Solve(numbers)

