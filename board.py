class Board:
    # Matrix = [[ 0 for i in range(3) ] for j in range(3)]

    def __init__(self):
        self.Matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.ZeroPosition = 0

    def GetBoard(self):
        return self.Matrix

    def FillBoard(self, Numbers):
        self.Matrix = Numbers[:]
    # Moving 0
    def MoveUp(self):
        tmpMatrix = self.Matrix[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition - 3]
        tmpMatrix[self.ZeroPosition - 3] = tmp

        return tmpMatrix

    def MoveDown(self):
        tmpMatrix = self.Matrix[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition + 3]
        tmpMatrix[self.ZeroPosition + 3] = tmp
        return tmpMatrix

    def MoveLeft(self):
        tmpMatrix = self.Matrix[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition - 1]
        tmpMatrix[self.ZeroPosition - 1] = tmp
        return tmpMatrix

    def MoveRight(self):
        tmpMatrix = self.Matrix[:]
        tmp = tmpMatrix[self.ZeroPosition]
        tmpMatrix[self.ZeroPosition] = tmpMatrix[self.ZeroPosition + 1]
        tmpMatrix[self.ZeroPosition + 1] = tmp
        return tmpMatrix

    # Verifying 0 position
    def CanMoveUp(self):
        if ((self.ZeroPosition / 3) != 0):
            return True
        return False

    def CanMoveDown(self):
        if ((self.ZeroPosition / 3) != 2):
            return True
        return False

    def CanMoveLeft(self):
        if ((self.ZeroPosition % 3 != 0)):
            return True
        return False

    def CanMoveRight(self):
        if (self.ZeroPosition % 3 != 2):
            return True
        return False

    def GetZeroPosition(self):
        return self.Matrix.index(0)
