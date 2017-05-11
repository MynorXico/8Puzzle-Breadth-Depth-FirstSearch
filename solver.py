import board
import state


class Solver:
    FrontierStates = []
    VisitedStates = []

    def IsInVisitedStates(self, Matrix):
        for i in self.VisitedStates:
            if Equals(self.VisitedStates[i].CurrentBoard.Matrix, Matrix):
                return True
        return False

    def IsInFrontierStates(self, Matrix):
        for i in self.FrontierStates:
            if Equals(self.FrontierStates[i].CurrentBoard.Matrix, Matrix):
                return True
        return False

    def Solve(self, Numbers):

        GoalState = state.State()
        GoalState.Numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        GoalState.CurrentBoard = board.Board.FillBoard(Numbers)

        InitialState = state.State()
        InitialState.CurrentBoard.FillBoard(Numbers)
        self.FrontierStates.append(InitialState)

        while (len(self.FrontierStates) != 0):
            tmpState = self.FrontierStates.pop()
            self.VisitedStates.append((tmpState))
            if Equals(GoalState.CurrentBoard, tmpState.CurrentBoard):
                return True
            children = tmpState.GenerateChildren
            for i in children:
                tmpChildren = children[i]
                if (self.IsInFrontierStates(tmpChildren.CurrentBoard.Matrix) != False and self.IsInVisitedStates(
                        tmpChildren.CurrentBoard.Matrix
                ) != False):
                    self.FrontierStates.append(tmpChildren)
        return False


def Equals(Matrix1, Matrix2):
    for i in Matrix1:
        for j in Matrix1[i]:
            if (Matrix1[i][j] != Matrix2[i][j]):
                return False
    return True
