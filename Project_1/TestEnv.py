import SudokuEnv
import RandomSearch
import HillClimbing
import SimulatedAnnealing
import random as R

test = SudokuEnv.Sudoku(20)

# for i in range(20):
#     test.update(R.randint(1, 9), R.randint(0, 8), R.randint(0, 8))

test.printBoard()

n, l = test.checkError()

print("Number of Errors:", n)
print("List of Errors:", end="\n\t")
print(*l, sep='\n\t')
