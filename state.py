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
            print row
        print "\n"
    def GenerateChildren(self):
        GeneratedChildren = []
        if (self.CurrentBoard.CanMoveUp()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveUp()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Movement = self.Movement + ", Up"
            tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition - 3
            GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveDown()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveDown()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Movement = self.Movement + ", Down"
            tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition + 3
            GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveLeft()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveLeft()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Movement = self.Movement + ", Left"
            tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition - 1
            GeneratedChildren.append(tmpState)

        if (self.CurrentBoard.CanMoveRight()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveRight()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Movement = self.Movement + ", Right"
            tmpState.CurrentBoard.ZeroPosition = self.CurrentBoard.ZeroPosition + 1
            GeneratedChildren.append(tmpState)

        return GeneratedChildren

    def PrintSatePath(self):
        current = self
        print current.Movement
