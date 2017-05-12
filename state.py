import board


class State:
    def __init__(self):
        self.Parent = []
        self.Children = []
        self.Numbers = []
        self.CurrentBoard = board.Board()

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
            tmpState.Parent = self
            GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveDown()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveDown()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Parent = self
            GeneratedChildren.append(tmpState)

        if (self.CurrentBoard.CanMoveLeft()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveLeft()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Parent = self
            GeneratedChildren.append(tmpState)

        if (self.CurrentBoard.CanMoveRight()):
            tmpState = State()
            tmpBoard = board.Board()
            tmpBoard.Matrix = self.CurrentBoard.MoveRight()
            tmpState.CurrentBoard = tmpBoard
            tmpState.Parent = self
            GeneratedChildren.append(tmpState)

        return GeneratedChildren
