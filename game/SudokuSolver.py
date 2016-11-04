import random
import copy
from game import SudokuGrid


# Solves the given sudoku grid and returns it as a new grid. The grid given in parameter is copied and kept as it is.
# In case that the given grid has no solution, None type is returned instead of the solution grid.
class SudokuSolver:
    # Returned the solved sudoku grid associated to the given sudoku grid
    def solve(self, sudokuGrid):

        if self.respectRules(sudokuGrid):

            grid = copy.copy(sudokuGrid)

            empty = self.findHoles(grid)
            avail = [i for i in range(1, 10)]
            currentIndex = 0

            tried = [[] for i in empty]

            # Sorry not sorry for the while
            while currentIndex < len(empty):

                currentAvail = list(avail)
                random.shuffle(currentAvail)

                (i, j) = empty[currentIndex]

                # Tests each number in the available ones.
                for index, num in enumerate(currentAvail):

                    # If the number is not in the line, column or square, it is added at this index
                    if num not in grid.getColumn(j) and num not in grid.getLine(i) and num not in grid.getSquare(
                            grid.getSquareNumber(i, j)) and num not in tried[currentIndex]:
                        grid[i, j] = num
                        break
                    # Backtracking. We tried all the possibilities and None is working,
                    #  we backtrack to the previous number and try another number for it.
                    elif index == len(currentAvail) - 1:

                        currentIndex -= 1

                        # Backtracked too far, there is no solution
                        if currentIndex < 0:
                            return None

                        previousIndexes = empty[currentIndex]

                        # Clears the tried for the indexes higher than the new current
                        for k in range(currentIndex + 1, len(tried)):
                            tried[k] = []

                        previous = grid[previousIndexes]
                        grid[previousIndexes] = None
                        tried[currentIndex].append(previous)
                        currentIndex -= 1

                currentIndex += 1

        else:
            return None

        return grid

    # Verifies if the given sudoku grid respects the rules of the game.
    # Checks if each line, column and square only contain one instance of every number.
    def respectRules(self, sudokuGrid):

        for i in range(sudokuGrid.width):
            line = sudokuGrid.getLine(i)
            col = sudokuGrid.getColumn(i)
            sq = sudokuGrid.getSquare(i)

            if self.__sum(line) != self.__sum(set(line)) or self.__sum(col) != self.__sum(set(col)) or self.__sum(sq) != self.__sum(
                    set(sq)):
                return False

        return True

    # Calculates the sum of the given iterable, considering None as a 0 value.
    # This function should not be called from outside this class.
    def __sum(self, it):

        sum = 0

        for i in it:
            if i is not None:
                sum += i
        return sum

    # Finds empty spaces in the grid, where there are no number (None), and return them as a
    # List of type containing the line and the column of those spaces.
    def findHoles(self, sudokuGrid):

        result = []

        for i in range(sudokuGrid.height):
            for j in range(sudokuGrid.width):
                if sudokuGrid[i, j] is None:
                    result.append((i, j))

        return result


