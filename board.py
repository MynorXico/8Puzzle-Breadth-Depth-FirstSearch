class Board:
    Matrix = [[0 for i in range(3)] for j in range(3)]

    def GetBoard(self):
        return self.Matrix

    def FillBoard(self, Numbers):
        for i in Numbers:
            self.Matrix[i / 3][i % 3] = Numbers[i]

    # Moving 0
    def MoveUp(self):
        ZeroPosition = self.GetZeroPosition()
        tmp = self.Matrix[ZeroPosition / 3][ZeroPosition % 3]
        self.Matrix[ZeroPosition / 3][ZeroPosition % 3] = self.Matrix[(ZeroPosition / 3) - 1][ZeroPosition % 3]
        self.Matrix[(ZeroPosition / 3) - 1][ZeroPosition % 3] = tmp
        return self.Matrix

    def MoveDown(self):
        ZeroPosition = self.GetZeroPosition()
        tmp = self.Matrix[ZeroPosition / 3][ZeroPosition % 3]
        self.Matrix[ZeroPosition / 3][ZeroPosition % 3] = self.Matrix[(ZeroPosition / 3) + 1][ZeroPosition % 3]
        self.Matrix[(ZeroPosition / 3) + 1][ZeroPosition % 3] = tmp
        return self.Matrix

    def MoveLeft(self):
        ZeroPosition = self.GetZeroPosition()
        tmp = self.Matrix[ZeroPosition / 3][ZeroPosition % 3]
        self.Matrix[ZeroPosition / 3][ZeroPosition % 3] = self.Matrix[ZeroPosition / 3][(ZeroPosition % 3) - 1]
        self.Matrix[ZeroPosition / 3][(ZeroPosition % 3) - 1] = tmp
        return self.Matrix

    def MoveRight(self):
        ZeroPosition = self.GetZeroPosition()
        tmp = self.Matrix[ZeroPosition / 3][ZeroPosition % 3]
        self.Matrix[ZeroPosition / 3][ZeroPosition % 3] = self.Matrix[ZeroPosition / 3][(ZeroPosition % 3) + 1]
        self.Matrix[ZeroPosition / 3][(ZeroPosition % 3) + 1] = tmp
        return self.Matrix

    # Verifying 0
    def CanMoveUp(self):
        ZeroPosition = self.GetZeroPosition()
        if ((ZeroPosition / 3) != 0):
            return True
        return False

    def CanMoveDown(self):
        ZeroPosition = self.GetZeroPosition()
        if ((ZeroPosition / 3) != 2):
            return True
        return False

    def CanMoveLeft(self):
        ZeroPosition = self.GetZeroPosition()
        if ((ZeroPosition % 3 != 0)):
            return True
        return False

    def CanMoveRight(self):
        ZeroPosition = self.GetZeroPosition()
        if (ZeroPosition % 3 != 2):
            return True
        return False

    def GetZeroPosition(self):
        position = 0
        for i in self.Matrix:
            for j in self.Matrix:
                if (self.Matrix[i][j] == 0):
                    return position
                position += 1
        return position
