from game import SudokuSolver
from game import SudokuGrid
import copy
import random

class SudokuGenerator:

    # Returns an auto-generated valid Sudoku grid.
    # This grid is a unique solution to the Sudoku generated by generate() method.
    # From this grid, only a few cases will be removed from the grid to generate the sudoku.
    def generateGrid(self):

        grid = SudokuSolver.SudokuSolver().solve(SudokuGrid.SudokuGrid())
        pierced = self.pierceGrid(grid)

        return (pierced, grid)

    # Take the given grid and returns a copy of it with holes in it set as None for random indexes.
    def pierceGrid(self, sudokuGrid):

        cop = SudokuGrid.SudokuGrid()
        cop.setEntries(list(sudokuGrid.entries))

        # Random amount of holes
        numHole = random.randrange(65, 75)

        for i in range(numHole):
            i,j = random.randrange(0, 9), random.randrange(0, 9)
            cop[i,j] = None

        return cop


