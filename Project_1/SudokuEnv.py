import random as R

class Sudoku:
            #1  2  3  4  5  6  7  8  9
    board =[[0, 0, 0, 0, 0, 0, 0, 0, 0], # 1
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2 
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
            [0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]  # 9

    initLoc = []

    def __init__(self, uFilledNum=0):
        if (uFilledNum > 81):
            uFilledNum = 81

        self.filledNum = uFilledNum
        
        i = 0
        while (i < uFilledNum):
            found = False
            x = R.randint(0, 8)
            y = R.randint(0, 8)
            for j in self.initLoc:
                if (j == [x, y]):
                    i -= 1
                    found = True
                    break
            if(~found):
                self.board[x][y] = R.randint(1, 9)
                if (self.checkError()[0] > 0):
                    self.board[x][y] = 0
                    i -= 1
                else:
                    self.initLoc.append([x, y])
            i += 1


    def update(self, n, x, y):
        check = [x, y]
        for i in self.initLoc:
            if (i == check):
                return self  #cannot change the initial value
        result = self.deepClone()
        result.board[x][y] = n
        result.filledNum = 0
        for i in range(9):
            for j in range(9):
                if (result.board[i][j] != 0):
                    result.filledNum += 1
        return result

    def update2(self, n, x, y):
        check = [x, y]
        for i in self.initLoc:
            if (i == check):
                return self  # cannot change the initial value
        result = self.deepClone()
        result.board[x][y] = n
        result.filledNum = 0
        for i in range(9):
            for j in range(9):
                if (result.board[i][j] != 0):
                    result.filledNum += 1
        return result
    def checkError(self):
        numError = 0
        errorLoc = []
        for i in range(9):
            for j in range(9):
                checkNum = self.board[i][j]
                if (checkNum != 0):
                    for k in range(j + 1, 9):
                        if (checkNum == self.board[i][k]):
                            numError += 1
                            errorLoc.append([i, j, "row"])
                    for k in range(i + 1, 9):
                        if (checkNum == self.board[k][j]):
                            numError += 1
                            errorLoc.append([i, j, "col"])
                    for k in range(i // 3 * 3, i // 3 * 3 + 3):
                        for l in range(j // 3 * 3, j // 3 + 3):
                            if (checkNum == self.board[k][l] and (i != k or j != l)):
                                numError += 1
                                errorLoc.append([i, j, "square"])

        return numError, errorLoc

    def checkError2(tempboard):
        numError = 0
        errorLoc = []
        for i in range(9):
            for j in range(9):
                checkNum = self.board[i][j]
                if (checkNum != 0):
                    for k in range(j + 1, 9):
                        if (checkNum == self.board[i][k]):
                            numError += 1
                            errorLoc.append([i, j, "row"])
                    for k in range(i + 1, 9):
                        if (checkNum == self.board[k][j]):
                            numError += 1
                            errorLoc.append([i, j, "col"])
                    for k in range(i // 3 * 3, i // 3 * 3 + 3):
                        for l in range(j // 3 * 3, j // 3 + 3):
                            if (checkNum == self.board[k][l] and (i != k or j != l)):
                                numError += 1
                                errorLoc.append([i, j, "square"])

        return numError, errorLoc

    def printBoard(self):
        for i in range(9):
            if (i % 3 == 0):
                    print("-------------------------")
            for j in range(9):
                if (j % 3 == 0):
                    print("|", end=" ")
                print(self.board[i][j], end=" ")

            print("|",i,"\n", end="")
        print("-------------------------")

    def returnBoard(self):
        return self.board

    def returnEmptyvaluePosition(self):
        Positionlist = []
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    Positionlist.append([i, j])
        return Positionlist

    def successor(self, n, x, y):
        tempboard = self.board



    def checkGoal(self):
        return self.checkError() and (self.filledNum == 81)

    def deepClone(self):
        result = Sudoku()
        for i in range(9):
            for j in range(9):
                result.board[i][j] = self.board[i][j]

        for i in range(len(self.initLoc)):
            for j in range(2):
                result.initLoc[i][j] = self.initLoc[i][j]

        result.filledNum = self.filledNum

        return result