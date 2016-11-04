import random
import copy
from game import SudokuGrid


class SudokuSolver:
    # Returned the solved sudoku grid associated to the given sudoku grid
    def solve(self, sudokuGrid):

        grid = copy.copy(sudokuGrid)

        # The available values from 1 to 9 shuffled
        values = [i for i in range(1, 10)]
        random.shuffle(values)

        j = 0

        for i in range(grid.height):
            # start new line, get the available values back
            avail = list(values)
            random.shuffle(avail)
            j = 0

            for j in range(grid.width):

                if grid[i, j] == None:
                    # Tests until given element works
                    for e, k in enumerate(avail):

                        # If k is not in either line, column or square, we test it there
                        if k not in grid.getColumn(j) and k not in grid.getLine(i) and k not in grid.getSquare(
                                grid.getSquareNumber(i, j)):
                            grid[i, j] = k
                            break






        return grid


solver = SudokuSolver()
print(SudokuGrid.SudokuGrid())
print(solver.solve(SudokuGrid.SudokuGrid()))
