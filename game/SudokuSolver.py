import random
from game import SudokuGrid


# Solves the given sudoku grid and returns it as a new grid. The grid given in parameter is copied and kept as it is.
# In case that the given grid has no solution, None type is returned instead of the solution grid.
class SudokuSolver:
    # Returned the solved sudoku grid associated to the given sudoku grid
    def solve(self, sudokugrid):

        if self.respectrules(sudokugrid):

            grid = SudokuGrid.SudokuGrid()
            grid.setentries(list(sudokugrid.entries))

            empty = self.findholes(grid)
            avail = [i for i in range(1, 10)]
            currentindex = 0

            tried = [[] for i in empty]

            # Sorry not sorry for the while
            while currentindex < len(empty):

                current_avail = list(avail)
                random.shuffle(current_avail)

                (i, j) = empty[currentindex]

                # Tests each number in the available ones.
                for index, num in enumerate(current_avail):

                    # If the number is not in the line, column or square, it is added at this index
                    if num not in grid.getcolumn(j) and num not in grid.getline(i) and num not in grid.getsquare(
                            grid.get_square_number(i, j)) and num not in tried[currentindex]:
                        grid[i, j] = num
                        break
                    # Backtracking. We tried all the possibilities and None is working,
                    #  we backtrack to the previous number and try another number for it.
                    elif index == len(current_avail) - 1:

                        currentindex -= 1

                        # Backtracked too far, there is no solution
                        if currentindex < 0:
                            return None

                        previous_indexes = empty[currentindex]

                        # Clears the tried for the indexes higher than the new current
                        for k in range(currentindex + 1, len(tried)):
                            tried[k] = []

                        previous = grid[previous_indexes]
                        grid[previous_indexes] = None
                        tried[currentindex].append(previous)
                        currentindex -= 1

                currentindex += 1

        else:
            return None

        return grid

    # Verifies if the given sudoku grid respects the rules of the game.
    # Checks if each line, column and square only contain one instance of every number.
    def respectrules(self, sudokugrid):

        for i in range(sudokugrid.width):
            line = sudokugrid.getline(i)
            col = sudokugrid.getcolumn(i)
            sq = sudokugrid.getsquare(i)

            if self.__sum(line) != self.__sum(set(line)) or self.__sum(col) != self.__sum(set(col)) or self.__sum(sq) != self.__sum(
                    set(sq)):
                return False

        return True

    # Calculates the sum of the given iterable, considering None as a 0 value.
    # This function should not be called from outside this class.
    def __sum(self, it):

        count = 0

        for i in it:
            if i is not None:
                count += i
        return count

    # Finds empty spaces in the grid, where there are no number (None), and return them as a
    # List of type containing the line and the column of those spaces.
    def findholes(self, sudokugrid):

        result = []

        for i in range(sudokugrid.height):
            for j in range(sudokugrid.width):
                if sudokugrid[i, j] is None:
                    result.append((i, j))

        return result


