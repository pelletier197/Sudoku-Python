#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains utils to read and to write Sudoku grids to a given file
"""

__auteur__ = "RABOU264"
__date__ = "2016-11-05"
__coequipiers__ = "SUPEL55", "ANMIG8"

from game import SudokuGrid


def read_sudoku(file):
    """Reads a list of soduku grids in a txt file and returns it as a list of sudoku grids"""
    with open(file, 'r') as fi:
        text = fi.read()
        text = text.replace(" ", "").replace("\n", "")

    grid_qty = len(text) // 81
    grids = []

    for i in range(grid_qty):
        cur = text[i * 81:i * 81 + 81]
        grids.append(__togrid(cur))

    return grids


def __togrid(text):
    """
    Converts the given text input into a grid of sudoku.
    This function should only be used internally and not be called from outside this class.
    """
    grid = SudokuGrid.SudokuGrid()
    entries = []

    for i in text:
        if i == ".":
            entries.append(None)
        else:
            entries.append(int(i))
    grid.set_entries(entries)

    return grid


def write_sudoku(file, *grids):
    """
    Writes the given sudoku grids into the given file as a text representation.
    You may deserialize this grid by calling readSudoku
    """
    with open(file, "w") as fi:
        for i in grids:
            fi.write(__fromgrid(i))


def __fromgrid(grid):
    """
    Creates the text associated to a SudokuGrid. This function is used to serialize the sudoku grid.
    This function is used internally and should not be called outside this class.
    """
    text = ""

    for i in grid.entries:
        if i is None:
            text += "."
        else:
            text += str(i)

    return text
