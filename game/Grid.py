#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module only contain a grid class that may be extended to have a m x n grid that contains anything.
"""
__auteur__ = "SUPEL55"
__date__ = "2016-10-24"
__coequipiers__ = "RABOU264", "ANMIG8"


class Grid:
    """
    A grid is a container used as a 2 dimensional array and where the entries of the given
    grid are only numbers or None values.
    """

    def __init__(self, h, w):
        """
        Initializes the game grid with the given height and width.
        h and w parameters must be > than 0, or an AssertionError is raised
        """
        assert h > 0 and w > 0

        self.entries = [None for i in range(h * w)]
        self.width = w
        self.height = h

    def __getitem__(self, item):
        """
        Use this method to get the item situated on the line and the column given
        by the tuple item = (line, column).
        If line >= height or column >= width, then an IndexError is raised. Same event occur if
        line or column < 0
        """
        line, col = item

        if line < 0 or col < 0 or line >= self.height or col >= self.width:
            raise IndexError()

        return self.entries[line * self.width + col]

    def __setitem__(self, item, value):
        """
        Use this method to set the item situated on the line and the column given
        by the tuple item = (line, column) to the given value.
        If line >= height or column >= width, then an IndexError is raised. Same event occur if
        line or column < 0
        """
        line, col = item

        if line < 0 or col < 0 or line >= self.height or col >= self.width:
            raise IndexError()

        self.entries[line * self.width + col] = value

    def set_entries(self, entries):
        """
        Sets the entries of the grid. The entries must either be int values or None value.
        Also, the number of elements in entries parameter must be width * height. Use this function to set
        all the entries of the grid
        """
        assert len(entries) == self.width * self.height

        for i in entries:
            assert isinstance(i, int) or i is None

        self.entries = entries

    def get_line(self, line):
        """
        Returns the line of the grid associated to the given index,
        where line parameter is contained in range [0, width-1]
        """
        if line < 0 or line >= self.height:
            raise IndexError()

        start = line * self.width

        return self.entries[start:start + self.width]

    def get_column(self, col):
        """
        Returns the column of the grid associated to the given column index,
        here col is contained in range [0,height-1]
        """
        if col < 0 or col >= self.width:
            raise IndexError()

        return self.entries[col::self.width]

    def __str__(self):
        """Returns the grid in a string representation"""
        total = ""

        for i in range(self.height):
            for j in range(self.width):
                item = self[i, j]
                if item is None:
                    total += " |"
                else:
                    total += str(item) + "|"
            total = total[0:len(total) - 1] + "\n"

        return total
