#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains the sudoku solver for a sudoku grid
"""

__auteur__ = "SUPEL55"
__date__ = "2016-11-21"
__coequipiers__ = "RABOU264", "ANMIG8"


class SudokuSolver:
    """
    Grid solver for a sudoku grid.
    """

    def solve(self, sudokugrid):
        """Returns the solved sudoku grid associated to the given sudoku grid
    Solves the given sudoku grid and returns it as a new grid. The grid given in parameter is copied
    and kept as it is.In case that the given grid has no solution, None type is returned instead of
    the solution grid.Set shuffle parameter to true to activate the shuffle solving. May only be
     used if the function is called to generate the sudoku.
    """
        if self.__respect_rules(sudokugrid):

            grid = sudokugrid.copy()
            empty = self.find_holes(grid)
            current_index = 0

            # We have one list for components in lines, col and square
            lines, col, sq = self.__init_possibilities(grid)
            tried = [set() for i in empty]

            length = len(empty)

            # Sorry not sorry for the while
            while current_index < length:
                # The current index we test
                (i, j) = empty[current_index]
                current_line = lines[i]
                current_col = col[j]
                current_sq = sq[grid.get_square_number(i, j)]
                current_try = tried[current_index]

                current_possi = (current_line & current_col & current_sq) - current_try

                if len(current_possi) != 0:

                    # Pops the first value and test it
                    test = current_possi.pop()
                    current_try.add(test)

                    current_line.remove(test)
                    current_col.remove(test)
                    current_sq.remove(test)

                    grid[i, j] = test
                    current_index += 1

                # There is zero possibilities for this case, so we backtrack
                else:  # The current possibilities are reset, as we go back, so possibilities may change
                    tried[current_index].clear()
                    current_index -= 1

                    # No solution we backtracked behind possibilities, so None is returned
                    if current_index < 0:
                        return None
                    previous_index = empty[current_index]
                    (i, j) = previous_index
                    previous_item = grid[previous_index]

                    lines[i].add(previous_item)
                    col[j].add(previous_item)
                    sq[grid.get_square_number(i, j)].add(previous_item)

                    grid[previous_index] = None

        else:
            return None

        return grid

    @staticmethod
    def __init_possibilities(grid):
        """Finds the possibilities for the lines, columns and squares removing the elements from
        the grid that are present in them. The result are returned as a tuple containing
        (possibilities for each lines, possibilities for each columns, possibilities for each square
        """
        avail = set([i for i in range(1, 10)])
        lines, col, sq = [], [], []

        for i in range(9):
            lines.append(avail - set(grid.get_line(i)))
            col.append(avail - set(grid.get_column(i)))
            sq.append(avail - set(grid.get_square(i)))

        return lines, col, sq

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
        for i, obj in enumerate(num_list):
            if obj is not None:
                if obj in seen.keys():
                    indexes.add(i)
                    indexes.add(seen.get(obj))
                seen[obj] = i

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
