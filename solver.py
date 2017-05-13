from timeit import default_timer as timer

import state


class Solver:
    def __init__(self):
        self.FrontierStates = []
        self.VisitedStates = []
        self.NodesExpanded = 0
        self.FrontierMatrices = []
        self.VisitedMatrices = []

    def IsInVisitedStates(self, Matrix):
        for i in self.VisitedStates:
            if i.CurrentBoard.Matrix == Matrix:
                return True
        return False

    def IsInFrontierStates(self, Matrix):
        for i in self.FrontierStates:
            if i.CurrentBoard.Matrix == Matrix:
                return True
        return False

    def Solve(self, Numbers):
        GoalNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        GoalState = state.State()
        GoalState.Initialize(GoalNumbers)

        InitialState = state.State()
        InitialState.CurrentBoard.FillBoard(Numbers)
        InitialState.CurrentBoard.ZeroPosition = InitialState.CurrentBoard.GetZeroPosition()
        self.FrontierStates.append(InitialState)

        self.FrontierMatrices.append(InitialState.CurrentBoard.Matrix)


        while (len(self.FrontierStates) != 0):
            if (len(self.VisitedStates) % 2000 == 0):
                print str(timer()) + " (" + str(len(self.VisitedStates)) + ") "
            tmpState = self.FrontierStates.pop(0)
            self.VisitedStates.append((tmpState))
            self.VisitedMatrices.append(tmpState.CurrentBoard.Matrix)
            if GoalState.CurrentBoard.Matrix == tmpState.CurrentBoard.Matrix:
                tmpState.PrintSatePath()
                return True

            children = tmpState.GenerateChildren()
            for i in children:
                tmpChildren = i
                if (
                        tmpChildren.CurrentBoard.Matrix in self.FrontierMatrices or tmpChildren.CurrentBoard.Matrix in self.VisitedMatrices) == False:
                    self.FrontierStates.append(tmpChildren)
                    self.FrontierMatrices.append(tmpChildren.CurrentBoard.Matrix)

        print "False"
        return False
