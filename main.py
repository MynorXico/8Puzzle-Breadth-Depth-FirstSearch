import solver

numbers = [1, 2, 5, 3, 4, 0, 6, 7, 8]
s = solver.Solver()
s.Solve(numbers)

'''Tests'''
test1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
test2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# print solver.EqualMatrices(test1, test2)
