import random

from game import SudokuGrid
from game import SudokuSolver


# Generator for a Sudoku grid. It first generate a valid grid using a sudoku
# solver on an empty grid, then removes between 65 and 75 values from this grid
# to complexify the game
class SudokuGenerator:
    # Returns an auto-generated valid Sudoku grid.
    # This grid is a unique solution to the Sudoku generated by generate() method.
    # From this grid, only a few cases will be removed from the grid to generate the sudoku.
    # The result returned by this function is a tuple containing (generatedGrid, solution to the grid).
    def generate_grid(self):
        grid = SudokuSolver.SudokuSolver().solve(SudokuGrid.SudokuGrid())
        pierced = self.pierce_grid(grid)

        return pierced, grid

    # Takes the given grid and returns a copy of it with holes in it set as None for random indexes.
    def pierce_grid(self, sudokugrid):
        cop = SudokuGrid.SudokuGrid()
        cop.setentries(list(sudokugrid.entries))

        # Random amount of holes
        numhole = random.randrange(65, 75)

        for i in range(numhole):
            i, j = random.randrange(0, 9), random.randrange(0, 9)
            cop[i, j] = None

        return cop
