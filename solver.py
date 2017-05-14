from timeit import default_timer as timer

import state


class Solver:
    def __init__(self):
        self.FrontierStates = []
        self.NodesExpanded = 0
        self.FrontierMatrices = []
        self.VisitedMatrices = []

    def Solve(self, Numbers):
        GoalNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        GoalState = state.State()
        GoalState.Initialize(GoalNumbers)

        InitialState = state.State()
        InitialState.CurrentBoard.Matrix = Numbers[:]
        InitialState.CurrentBoard.ZeroPosition = InitialState.CurrentBoard.GetZeroPosition()

        self.FrontierStates.append(InitialState)
        self.FrontierMatrices.append(InitialState.CurrentBoard.Matrix)

        print timer()
        while (len(self.FrontierStates) != 0):
            if (len(self.VisitedMatrices) == 10000):
                print (timer())
            tmpState = self.FrontierStates.pop(0)
            self.VisitedMatrices.append(tmpState.CurrentBoard.Matrix)
            if GoalState.CurrentBoard.Matrix == tmpState.CurrentBoard.Matrix:
                tmpState.PrintSatePath()
                print str(timer()) + " (" + str(len(self.VisitedMatrices)) + ") "
                return True

            children = tmpState.GenerateChildren(self.VisitedMatrices, self.FrontierMatrices)
            for i in children:
                self.FrontierStates.append(i)
                self.FrontierMatrices.append(i.CurrentBoard.Matrix)

        print ("False")
        return False
