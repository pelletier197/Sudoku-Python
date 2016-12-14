#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains a sudoku generator that may be used to generate a grid.
"""
__auteur__ = "RABOU264"
__date__ = "2016-10-24"
__coequipiers__ = "SUPEL55", "ANMIG8"

import random

from game import SudokuGrid


class SudokuGenerator:
    """
    Generator for a Sudoku grid. It first generate a valid grid using a sudoku
    solver on an empty grid, then removes between 65 and 75 values from this grid
    to complexify the game
    """

    def generate_grid(self):
        """
        From this grid, only a few cases will be removed from the grid to generate the sudoku.
        The result returned by this function is a tuple containing (generatedGrid, solution_to_the_grid).
        Note that the generation algorithm may allow multiple solution to the grid returned by this function.
        """
        grid = self.generate(SudokuGrid.SudokuGrid(), shuffle=True)
        pierced = self.__pierce_grid(grid)
        return pierced, grid

    @staticmethod
    def __pierce_grid(sudoku_grid):
        """Takes the given grid and returns a copy of it with holes in it set as None for random indexes."""
        cop = sudoku_grid.copy()

        # Random amount of holes
        num_hole = random.randrange(70, 75)

        for i in range(num_hole):
            i, j = random.randrange(0, 9), random.randrange(0, 9)
            cop[i, j] = None

        return cop

    def generate(self, sudokugrid, shuffle=False):
        """
        Uses a non optimal solve algorithm to generate a random valid sudoku grid
    """

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

        return grid

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
