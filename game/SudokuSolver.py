import random

from game import SudokuGrid


class SudokuSolver:
    """
    Solves the given sudoku grid and returns it as a new grid. The grid given in parameter is copied and kept as it is.
    In case that the given grid has no solution, None type is returned instead of the solution grid.
    """
    def solve(self, sudokugrid):
        """Returned the solved sudoku grid associated to the given sudoku grid"""
        if self.__respectrules(sudokugrid):

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
                    if num not in tried[currentindex] and num not in grid.getcolumn(j) and num not in grid.getline(
                            i) and num not in grid.getsquare(grid.get_square_number(i, j)):
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

    def __respectrules(self, sudokugrid):
        """
        Verifies if the given sudoku grid respects the rules of the game.
        Checks if each line, column and square only contain one instance of every number.
        """
        for i in range(sudokugrid.width):
            line = sudokugrid.getline(i)
            col = sudokugrid.getcolumn(i)
            sq = sudokugrid.getsquare(i)

            if self.__sum(line) != self.__sum(set(line)) or self.__sum(col) != self.__sum(set(col)) or self.__sum(
                    sq) != self.__sum(
                set(sq)):
                return False

        return True

    def get_rules_not_respected(self, grid):
        """
        Returns a set containing the elements in the grid that do not respect the sudoku rules.
        For instance if there is  sevens in a row, the function will return the index in the grid
        of the 2 sevens meaning that both of them are not correct
        """
        doubles = []
        for i in range(grid.width):
            line = self.__check_doubles(grid.getline(i))
            col = self.__check_doubles(grid.getcolumn(i))
            sq = self.__check_doubles(grid.getsquare(i))

            doubles = doubles + [(i, e) for e in line]
            doubles = doubles + [(e, i) for e in col]
            doubles = doubles + [(i // 3 * 3 + e // 3, (i % 3) * 3 + e % 3) for e in sq]

        return set(doubles)

    def __check_doubles(self, list):
        """Check for doubles in a given list and return the double"""
        seen = {}
        indexes = set()
        for i, e in enumerate(list):
            if e is not None:
                if e in seen.keys():
                    indexes.add(i)
                    indexes.add(seen.get(e))
                seen[e] = i

        return indexes

    def __sum(self, it):
        """
        Calculates the sum of the given iterable, considering None as a 0 value.
        This function should not be called from outside this class.
        """
        count = 0

        for i in it:
            if i is not None:
                count += i
        return count

    def findholes(self, sudokugrid):
        """
        Finds empty spaces in the grid, where there are no number (None), and return them as a
        List of type containing the line and the column of those spaces.
        """
        result = []

        for i in range(sudokugrid.height):
            for j in range(sudokugrid.width):
                if sudokugrid[i, j] is None:
                    result.append((i, j))

        return result
