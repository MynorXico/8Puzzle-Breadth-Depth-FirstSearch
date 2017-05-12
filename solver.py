import state


class Solver:
    def __init__(self):
        self.FrontierStates = []
        self.VisitedStates = []

    def IsInVisitedStates(self, Matrix):
        for i in self.VisitedStates:
            if EqualMatrices(i.CurrentBoard.Matrix, Matrix):
                return True
        return False

    def IsInFrontierStates(self, Matrix):
        for i in self.FrontierStates:
            if EqualMatrices(i.CurrentBoard.Matrix, Matrix):
                return True
        return False

    def Solve(self, Numbers):

        GoalState = state.State()
        GoalState.Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        GoalState.CurrentBoard.FillBoard(GoalState.Numbers)

        InitialState = state.State()

        InitialState.CurrentBoard.FillBoard(Numbers)
        InitialState.Parent = 0
        self.FrontierStates.append(InitialState)

        while (len(self.FrontierStates) != 0):
            tmpState = self.FrontierStates.pop(0)
            self.VisitedStates.append((tmpState))
            if EqualMatrices(GoalState.CurrentBoard.Matrix, tmpState.CurrentBoard.Matrix):
                tmpState.PrintState()
                return True
            children = tmpState.GenerateChildren()
            for i in children:
                tmpChildren = i
                if (self.IsInFrontierStates(tmpChildren.CurrentBoard.Matrix) == False and self.IsInVisitedStates(
                        tmpChildren.CurrentBoard.Matrix
                ) == False):

                    self.FrontierStates.append(tmpChildren)

        print "False"
        return False


def EqualMatrices(Matrix1, Matrix2):
    row = 0
    for i in Matrix1:
        column = 0
        for j in i:
            if (j != Matrix2[row][column]):
                return False
            column += 1
        row += 1
    return True
