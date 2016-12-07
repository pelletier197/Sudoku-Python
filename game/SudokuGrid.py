#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a Sudoku grid class that has utils to access
the elements contained in the grid and to ensure the content of the grid is valid
"""
__auteur__ = "SUPEL55"
__date__ = "2016-10-24"
__coequipiers__ = "RABOU264", "ANMIG8"

from game import Grid


class SudokuGrid(Grid.Grid):
    """
    Container class created from a Grid object. It uses to contain values contained in the range [1, 9]
    and None values, where None specifies and empty entry.
    """

    def __init__(self):
        """Initializes a Sudoku grid containing only None values in it."""
        super().__init__(9, 9)

    def get_square(self, number):
        """
        Returns the numbers associated to the given square number in the Sudoku grid.
        The grid is represented this way :

        _ _ _|_ _ _|_ _ _
        _ 0 _|_ 1 _|_ 2 _
        _ _ _|_ _ _|_ _ _

        _ _ _|_ _ _|_ _ _
        _ 3 _|_ 4 _|_ 5 _
        _ _ _|_ _ _|_ _ _

        _ _ _|_ _ _|_ _ _
        _ 6 _|_ 7 _|_ 8 _
        _ _ _|_ _ _|_ _ _

        and the returned value is a list of the 9 elements ocontained in the square, where None is inserted on empty cases
        """
        if number < 0 or number > 8:
            raise IndexError()

        # Finds the top left number in the square
        start_x = (number % 3) * 3
        start_y = (number // 3) * 3

        index = start_y * self.width + start_x
        index2 = index + 9
        index3 = index + 18

        lis = self.entries[index:index + 3] + self.entries[index2:index2 + 3] + self.entries[index3:index3 + 3]

        return lis

    def __setitem__(self, index, item):
        """
        Used to set the entry at the index(line, column) in the given tab.
        The value must either be contained between [1, 9] or be a None value, or an error is raised
        """
        line, col = index

        if line < 0 or col < 0 or line >= self.height or col >= self.width:
            raise IndexError()
        if isinstance(item, int) and (item < 0 or item > 9):
            raise ValueError()
        elif item is not None and not isinstance(item, int):
            raise ValueError()

        self.entries[line * self.width + col] = item

    def set_entries(self, entries):
        """
        Sets all the entries of the Sudoku grid, where all the entries are either between[1 , 9] or are None.
        The length of the entries must be of 81
        """
        assert len(entries) == self.width * self.height

        for i in entries:
            if isinstance(i, int) and (i < 0 or i > 9):
                raise ValueError()
            elif i is not None and not isinstance(i, int):
                raise ValueError()

        self.entries = entries

    def copy(self):
        """
        Copies the current grid and returns it as a new sudoku grid object.
        This will copy all its entries into 2 different grids
        """
        new = self.entries[:]
        grid = SudokuGrid()
        grid.set_entries(new)

        return grid

    @staticmethod
    def get_square_number(line, col):
        """
        Returns the square number that can be used in getsquare method
        for the given live and column in the grid.
        """
        if line < 0 or line > 9 or col < 0 or col > 9:
            raise IndexError()

        return (line // 3) * 3 + (col // 3)

    def __str__(self):
        """
        Returns the grid as a String representation with
        line and columns indicated, and where None values are replaces with spaces.
        """
        total = '''
    1 2 3   4 5 6   7 8 9
    ---------------------
 1 |{0} {1} {2} | {3} {4} {5} | {6} {7} {8}|
 2 |{9} {10} {11} | {12} {13} {14} | {15} {16} {17}|
 3 |{18} {19} {20} | {21} {22} {23} | {24} {25} {26}|
   |---------------------|
 4 |{27} {28} {29} | {30} {31} {32} | {33} {34} {35}|
 5 |{36} {37} {38} | {39} {40} {41} | {42} {43} {44}|
 6 |{45} {46} {47} | {48} {49} {50} | {51} {52} {53}|
   |---------------------|
 7 |{54} {55} {56} | {57} {58} {59} | {60} {61} {62}|
 8 |{63} {64} {65} | {66} {67} {68} | {69} {70} {71}|
 9 |{72} {73} {74} | {75} {76} {77} | {78} {79} {80}|
    ---------------------
    '''
        for i, obj in enumerate(self.__tostring()):
            cur = "{" + str(i) + "}"
            total = total.replace(cur, obj)

        return total

    def __tostring(self):
        """
        Turns the grid into a tuple containing . for empty entries and the number as a string for the others.
        This method should never be called from outside this function.
        """
        str_elem = []

        for i in self.entries:
            if i is None:
                str_elem.append(".")
            else:
                str_elem.append(str(i))

        return tuple(str_elem)
