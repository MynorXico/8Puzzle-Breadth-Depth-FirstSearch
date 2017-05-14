import board


class State:

    def __init__(self):
        self.Parent = []
        self.Children = []
        self.Numbers = []
        self.CurrentBoard = board.Board()
        self.Movement = ""

    def Initialize(self, Numbers):
        self.Numbers = Numbers
        self.CurrentBoard.FillBoard(Numbers)

    def PrintState(self):
        for row in self.CurrentBoard.Matrix:
            print (row)
        print ("\n")

    def GenerateChildren(self, VisitedMatrices, FrontierMatrices):
        GeneratedChildren = []
        if (self.CurrentBoard.CanMoveUp()):
            tmpMatrix = self.CurrentBoard.MoveUp()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpBoard = board.Board()
                tmpBoard.Matrix = tmpMatrix
                tmpState.CurrentBoard = tmpBoard
                tmpState.Movement = self.Movement + "U"
                tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition - 3
                GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveDown()):
            tmpMatrix = self.CurrentBoard.MoveDown()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpBoard = board.Board()
                tmpBoard.Matrix = tmpMatrix
                tmpState.CurrentBoard = tmpBoard
                tmpState.Movement = self.Movement + "D"
                tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition + 3
                GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveLeft()):
            tmpMatrix = self.CurrentBoard.MoveLeft()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpBoard = board.Board()
                tmpBoard.Matrix = tmpMatrix
                tmpState.CurrentBoard = tmpBoard
                tmpState.Movement = self.Movement + "L"
                tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition - 1
                GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveRight()):
            tmpMatrix = self.CurrentBoard.MoveRight()
            if (tmpMatrix in VisitedMatrices or tmpMatrix in FrontierMatrices) == False:
                tmpState = State()
                tmpBoard = board.Board()
                tmpBoard.Matrix = tmpMatrix
                tmpState.CurrentBoard = tmpBoard
                tmpState.Movement = self.Movement + "R"
                tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition + 1
                GeneratedChildren.append(tmpState)

        return GeneratedChildren

    def PrintSatePath(self):
        current = self
        print (current.Movement)
