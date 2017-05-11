import board


class State:
    Parent = []
    Children = []
    Numbers = []
    CurrentBoard = board.Board()

    def GenerateChildren(self):
        GeneratedChildren = []
        if (self.CurrentBoard.CanMoveUp()):
            tmpState = State()
            tmpState.CurrentBoard = self.CurrentBoard.MoveUp()
            GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveDown()):
            tmpState = State()
            tmpState.CurrentBoard = self.CurrentBoard.MoveDown()
            GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveLeft()):
            tmpState = State()
            tmpState.CurrentBoard = self.CurrentBoard.MoveLeft()
            GeneratedChildren.append(tmpState)
        if (self.CurrentBoard.CanMoveRight()):
            tmpState = State()
            tmpState.CurrentBoard = self.CurrentBoard.MoveRight()
            GeneratedChildren.append(tmpState)
        return GeneratedChildren
