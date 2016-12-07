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
from game import SudokuSolver


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
        grid = SudokuSolver.SudokuSolver().solve(SudokuGrid.SudokuGrid(), shuffle=True)
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
