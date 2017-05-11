class Board:
    Matrix = [[0 for i in range(3)] for j in range(3)]

    def GetBoard(self):
        return self.Matrix

    def FillBoard(self, Numbers):
        for i in Numbers:
            self.Matrix[i / 3][i % 3] = Numbers[i]
