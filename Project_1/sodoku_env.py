import gym
import numpy as np
import random
from gym import spaces, multi_discrete, tuples

def checkcondition(grid, x, y):
    error_location = []
    col_array = grid[:, x]
    if len(col_array) > len(set(col_array)):
        for row in range(0,8):
            if grid[x][y] == grid[row]:
                error_location.append([x,row])
    row_array = grid[y, :]
    if len(row_array) > len(set(row_array)):
        for col in range(0,8):
            if grid[x][y] == grid[col]:
                error_location.append([col,y])
            
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
            
        
class SodukuEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    
    def __init__(self):
        #self.observation_space = spaces.Box(low = 1, high = 9 , shape = (9,9), dtype=np.int8)
        self.current_grid = np.zeros(shape=(9,9))
        self.current_assigned = 0