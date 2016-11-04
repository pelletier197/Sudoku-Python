import random
import copy
from game import SudokuGrid


class SudokuSolver:
    # Returned the solved sudoku grid associated to the given sudoku grid
    def solve(self, sudokuGrid):

        grid = copy.copy(sudokuGrid)

        empty = self.findHoles(grid)
        avail = [i for i in range(1, 10)]
        currentIndex = 0

        tried = [[] for i in empty]

        while currentIndex < len(empty):

            currentAvail = list(avail)
            random.shuffle(currentAvail)

            (i, j) = empty[currentIndex]

            for index, num in enumerate(currentAvail):

                if num not in grid.getColumn(j) and num not in grid.getLine(i) and num not in grid.getSquare(
                        grid.getSquareNumber(i, j)) and num not in tried[currentIndex]:
                    grid[i, j] = num
                    print(sudokuGrid)
                    break
                # Backtracking
                elif index == len(currentAvail) - 1:

                    currentIndex -= 1
                    previousIndexes = empty[currentIndex]

                    # Clears the tried for the indexes higher than the new current
                    for k in range(currentIndex + 1, len(tried)):
                        tried[k] = []

                    previous = grid[previousIndexes]
                    grid[previousIndexes] = None
                    print((i, j), " elem : ", previous)
                    tried[currentIndex].append(previous)
                    currentIndex -= 1

            currentIndex += 1

        return grid

    def findHoles(self, sudokuGrid):

        result = []

        for i in range(sudokuGrid.height):
            for j in range(sudokuGrid.width):
                if sudokuGrid[i, j] is None:
                    result.append((i, j))

        print(result)
        return result


solver = SudokuSolver()
print(SudokuGrid.SudokuGrid())
print(solver.solve(SudokuGrid.SudokuGrid()))
