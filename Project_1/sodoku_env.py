import numpy as np
import random

def checkcondition(grid, x, y):
    error_location = []
    col_array = grid[:, x]
    #check the condidtion in col
    if len(col_array) > len(set(col_array)):
        for row in range(0,8):
            if grid[x][y] == grid[row]:
                error_location.append([x,row])
    #check the condition in row
    row_array = grid[y, :]
    if len(row_array) > len(set(row_array)):
        for col in range(0,8):
            if grid[x][y] == grid[col]:
                error_location.append([col,y])
    #check the condition in square
    # * Use mod to remove remainder
    posX = (x // 3) * 3
    posY = (y // 3) * 3
    # ! The posX & posY need to increase by 1 to get specific index [Block]
    square_array = grid[posX:, posY:]
    # Convert 2D into 1D array
    temp_array = np.array(square_array) # Convert normal list into narray
    oneD_array = temp_array.flatten()
    if len(oneD_array) > len(set(row_array)):
        for ax in range(0,8):
            if grid[x][y] == grid[ax]:
                error_location.append([((ax // 3) % 3) - 1,ax // 3])
    return error_location
    
def GenerateGrid():
    #Amount_of_assigned = random.randint(30,61)
    #current_assigned = Amount_of_assigned
    
    grid = np.zeros(shape=(9,9))
    for row in range(0, 8): #row
        random_value = random.randint(2,5)
        for value in range(0,random_value):
            list_location = []
            random_position = random.randint(0,9)
            while random_position in list_location:
                random_position = random.randint(0,9)
            if grid[row][random_position] == 0:
                grid[row][random_position] = random.randint(0,9)
                while len(checkcondition(grid, row, random_position)) > 0:
                    grid[row][random_position] = random.randint(0,9)
                list_location.append(random_position)
    return grid
            
        
class SodokuEnv:

    def __init__(self):
        self.OriginalGrid = GenerateGrid()
        self.Grid = self.OriginalGrid

    def successors(self,num,x,y):
        currentgrid = self.Grid
        currentgrid[x][y] = num
        error_location = checkcondition(currentgrid,x,y)
        return error_location

    def update(self, n, x, y):
        if self.Grid[x][y] == 0:
            self.Grid[x][y] = n
            return True
        else:
            return False

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
        return self.Grid

    def returnEmptyvaluePosition(self):
        Positionlist = []
        for i in range(9):
            for j in range(9):
                if self.Grid[i][j] == 0:
                    Positionlist.append([i, j])
        return Positionlist

    def checkGoal(self):
        count = 0
        for x in range(9):
            for y in range(9):
                if self.Grid[x][y] != 0:
                    count += 1
        if count == 81:
            return True
        else:
            return False
