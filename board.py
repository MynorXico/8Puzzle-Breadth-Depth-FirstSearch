class Board:
    # Matrix = [[ 0 for i in range(3) ] for j in range(3)]

    def __init__(self):
        self.Matrix = [[0 for i in range(3)] for j in range(3)]
        self.ZeroPosition = 0

    def GetBoard(self):
        return self.Matrix

    def FillBoard(self, Numbers):
        for i in range(len(Numbers)):
            self.Matrix[i / 3][i % 3] = Numbers[i]
    # Moving 0
    def MoveUp(self):
        tmpMatrix = Clone3x3Matrix(self.Matrix)
        ZeroPosition = self.ZeroPosition
        tmp = tmpMatrix[ZeroPosition / 3][ZeroPosition % 3]
        tmpMatrix[ZeroPosition / 3][ZeroPosition % 3] = tmpMatrix[(ZeroPosition / 3) - 1][ZeroPosition % 3]
        tmpMatrix[(ZeroPosition / 3) - 1][ZeroPosition % 3] = tmp

        return tmpMatrix

    def MoveDown(self):
        tmpMatrix = Clone3x3Matrix(self.Matrix)
        ZeroPosition = self.ZeroPosition
        tmp = tmpMatrix[ZeroPosition / 3][ZeroPosition % 3]
        tmpMatrix[ZeroPosition / 3][ZeroPosition % 3] = tmpMatrix[(ZeroPosition / 3) + 1][ZeroPosition % 3]
        tmpMatrix[(ZeroPosition / 3) + 1][ZeroPosition % 3] = tmp
        return tmpMatrix

    def MoveLeft(self):
        tmpMatrix = Clone3x3Matrix(self.Matrix)
        ZeroPosition = self.ZeroPosition
        tmp = tmpMatrix[ZeroPosition / 3][ZeroPosition % 3]
        tmpMatrix[ZeroPosition / 3][ZeroPosition % 3] = tmpMatrix[ZeroPosition / 3][(ZeroPosition % 3) - 1]
        tmpMatrix[ZeroPosition / 3][(ZeroPosition % 3) - 1] = tmp
        return tmpMatrix

    def MoveRight(self):
        tmpMatrix = Clone3x3Matrix(self.Matrix)
        ZeroPosition = self.ZeroPosition
        tmp = tmpMatrix[ZeroPosition / 3][ZeroPosition % 3]
        tmpMatrix[ZeroPosition / 3][ZeroPosition % 3] = tmpMatrix[ZeroPosition / 3][(ZeroPosition % 3) + 1]
        tmpMatrix[ZeroPosition / 3][(ZeroPosition % 3) + 1] = tmp
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
        position = 0
        for i in self.Matrix:
            for j in i:
                if (j == 0):
                    return position
                position += 1
        return position


def Clone3x3Matrix(Matriz):
    Output = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(Output)):
        Output[i] = Matriz[i][:]
    return Output
