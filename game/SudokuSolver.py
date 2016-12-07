#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This contains a solver class used to solve a sudoku grid.
"""

__auteur__ = "SUPEL55"
__date__ = "2016-10-24"
__coequipiers__ = "RABOU264", "ANMIG8"

import random

from game import SudokuGrid


class SudokuSolver:
    """
    Grid solver for a sudoku grid.
    """

    def solve(self, sudokugrid, shuffle=False):
        """Returns the solved sudoku grid associated to the given sudoku grid
    Solves the given sudoku grid and returns it as a new grid. The grid given in parameter is copied
    and kept as it is.In case that the given grid has no solution, None type is returned instead of
    the solution grid.Set shuffle parameter to true to activate the shuffle solving. May only be
     used if the function is called to generate the sudoku.
    """
        if self.__respect_rules(sudokugrid):

            grid = SudokuGrid.SudokuGrid()
            grid.set_entries(list(sudokugrid.entries))

            empty = self.find_holes(grid)
            avail = [i for i in range(1, 10)]
            current_index = 0

            tried = [[] for i in empty]

            # Sorry not sorry for the while
            while current_index < len(empty):

                current_avail = list(avail)
                if shuffle:
                    random.shuffle(current_avail)

                (i, j) = empty[current_index]

                # Tests each number in the available ones.
                for index, num in enumerate(current_avail):

                    # If the number is not in the line, column or square, it is added at this index
                    if num not in tried[current_index] and num not in grid.get_column(j) \
                            and num not in grid.get_line(i) \
                            and num not in grid.get_square(grid.get_square_number(i, j)):

                        grid[i, j] = num
                        break

                    # Backtracking. We tried all the possibilities and None is working,
                    #  we backtrack to the previous number and try another number for it.
                    elif index == len(current_avail) - 1:

                        current_index -= 1

                        # Backtracked too far, there is no solution
                        if current_index < 0:
                            return None

                        previous_indexes = empty[current_index]

                        # Clears the tried for the indexes higher than the new current
                        for k in range(current_index + 1, len(tried)):
                            if tried[k] is []:
                                break
                            tried[k] = []

                        previous = grid[previous_indexes]
                        grid[previous_indexes] = None
                        tried[current_index].append(previous)
                        current_index -= 1

                current_index += 1

        else:
            return None

        return grid

    def __respect_rules(self, sudoku_grid):
        """
        Verifies if the given sudoku grid respects the rules of the game.
        Checks if each line, column and square only contain one instance of every number.
        """
        for i in range(sudoku_grid.width):
            line = sudoku_grid.get_line(i)
            col = sudoku_grid.get_column(i)
            sq = sudoku_grid.get_square(i)

            if self.__sum(line) != self.__sum(set(line)) or self.__sum(col) != self.__sum(set(col)) \
                    or self.__sum(sq) != self.__sum(set(sq)):
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
            line = self.__check_doubles(grid.get_line(i))
            col = self.__check_doubles(grid.get_column(i))
            sq = self.__check_doubles(grid.get_square(i))

            doubles = doubles + [(i, e) for e in line]
            doubles = doubles + [(e, i) for e in col]
            doubles = doubles + [(i // 3 * 3 + e // 3, (i % 3) * 3 + e % 3) for e in sq]

        return set(doubles)

    @staticmethod
    def __check_doubles(num_list):
        """Check for doubles in a given list and return the double"""
        seen = {}
        indexes = set()
        for i, e in enumerate(num_list):
            if e is not None:
                if e in seen.keys():
                    indexes.add(i)
                    indexes.add(seen.get(e))
                seen[e] = i

        return indexes

    @staticmethod
    def __sum(it):
        """
        Calculates the sum of the given iterable, considering None as a 0 value.
        This function should not be called from outside this class.
        """
        count = 0

        for i in it:
            if i is not None:
                count += i
        return count

    @staticmethod
    def find_holes(sudoku_grid):
        """
        Finds empty spaces in the grid, where there are no number (None), and return them as a
        List of type containing the line and the column of those spaces.
        """
        result = []

        for i in range(sudoku_grid.height):
            for j in range(sudoku_grid.width):
                if sudoku_grid[i, j] is None:
                    result.append((i, j))

        return result
