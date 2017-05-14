class State:

    def __init__(self):
        self.Parent = []
        self.Children = []
        self.Numbers = []
        self.CurrentBoard = [0, 0, 0, 0, 0, 0, 0, 0]
        self.Movement = ""
        self.ZeroPosition = 0

    def Initialize(self, Numbers):
        self.Numbers = Numbers
        self.CurrentBoard = Numbers[:]
        self.ZeroPosition = self.CurrentBoard.index(0)

    def GenerateChildren(self, VisitedMatrices, FrontierMatrices, FrontierStates):
        if (self.ZeroPosition / 3) != 0:
            tmpMatrix = self.MoveUp()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpState.CurrentBoard = tmpMatrix
                tmpState.Movement = self.Movement + "U"
                tmpState.ZeroPosition = self.ZeroPosition - 3
                FrontierStates.append(tmpState)
                FrontierMatrices.append(tmpMatrix)
        if ((self.ZeroPosition / 3) != 2):
            tmpMatrix = self.MoveDown()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpState.CurrentBoard = tmpMatrix
                tmpState.Movement = self.Movement + "D"
                tmpState.ZeroPosition = self.ZeroPosition + 3
                FrontierStates.append(tmpState)
                FrontierMatrices.append(tmpMatrix)
        if self.ZeroPosition % 3 != 0:
            tmpMatrix = self.MoveLeft()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpState.CurrentBoard = tmpMatrix
                tmpState.Movement = self.Movement + "L"
                tmpState.ZeroPosition = self.ZeroPosition - 1
                FrontierStates.append(tmpState)
                FrontierMatrices.append(tmpMatrix)
        if (self.ZeroPosition % 3 != 2):
            tmpMatrix = self.MoveRight()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpState.CurrentBoard = tmpMatrix
                tmpState.Movement = self.Movement + "R"
                tmpState.ZeroPosition = self.ZeroPosition + 1
                FrontierStates.append(tmpState)
                FrontierMatrices.append(tmpMatrix)
    def PrintSatePath(self):
        current = self
        print (current.Movement)

    def MoveUp(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition - 3]
        tmpMatrix[self.ZeroPosition - 3] = tmp

        return tmpMatrix

    def MoveDown(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition + 3]
        tmpMatrix[self.ZeroPosition + 3] = tmp
        return tmpMatrix

    def MoveLeft(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition - 1]
        tmpMatrix[self.ZeroPosition - 1] = tmp
        return tmpMatrix

    def MoveRight(self):
        tmpMatrix = self.CurrentBoard[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition + 1]
        tmpMatrix[self.ZeroPosition + 1] = tmp
        return tmpMatrix

    def GetZeroPosition(self):
        return self.CurrentBoard.index(0)
