import solver

numbers = [5, 8, 2, 3, 7, 1, 6, 4]
s = solver.Solver()
s.Solve(numbers)

'''Tests'''
test1 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
test2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# print solver.EqualMatrices(test1, test2)
