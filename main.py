import solver

numbers = [8, 5, 7, 2, 4, 3, 6, 0, 2]
s = solver.Solver()
s.Solve(numbers)

# Tests
test1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
test2 = [[0, 1, 2], [3, 4, 5], [5, 7, 8]]
