from timeit import default_timer as timer

import state


class Solver:
    def __init__(self):
        self.FrontierStates = []
        self.NodesExpanded = 0
        self.FrontierMatrices = []
        self.VisitedMatrices = []
        self.ZeroPosition = 0

    def Solve(self, Numbers):
        GoalNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        GoalState = state.State()
        GoalState.CurrentBoard = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        InitialState = state.State()
        InitialState.CurrentBoard = Numbers[:]
        InitialState.ZeroPosition = InitialState.GetZeroPosition()

        self.FrontierStates.append(InitialState)
        self.FrontierMatrices.append(InitialState.CurrentBoard)

        print timer()
        while (len(self.FrontierStates) != 0):
            if (len(self.VisitedMatrices) % 10000 == 0):
                print len(self.VisitedMatrices)
                print (timer())
            tmpState = self.FrontierStates.pop(0)
            self.FrontierMatrices.pop(0)
            self.VisitedMatrices.append(tmpState.CurrentBoard)
            if GoalState.CurrentBoard == tmpState.CurrentBoard:
                tmpState.PrintSatePath()
                print str(timer()) + " (" + str(len(self.VisitedMatrices)) + ") "
                return True

            tmpState.GenerateChildren(self.VisitedMatrices, self.FrontierMatrices, self.FrontierStates)

        print ("False")
        return False

