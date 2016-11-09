from game import Grid


class SudokuGrid(Grid.Grid):
    def __init__(self):
        super().__init__(9, 9)

    # Returns the numbers associated to the given square number in the Sudoku grid.
    # The grid is represented this way :
    #
    # _ _ _|_ _ _|_ _ _
    # _ 0 _|_ 1 _|_ 2 _
    # _ _ _|_ _ _|_ _ _
    #
    # _ _ _|_ _ _|_ _ _
    # _ 3 _|_ 4 _|_ 5 _
    # _ _ _|_ _ _|_ _ _
    #
    # _ _ _|_ _ _|_ _ _
    # _ 6 _|_ 7 _|_ 8 _
    # _ _ _|_ _ _|_ _ _
    #
    # and the returned value is a list of the 9 elements ocontained in the square, where None is inserted on empty cases

    def getsquare(self, number):

        if number < 0 or number > 8:
            raise IndexError()

        col = number % 3
        line = number // 3

        # Finds the top left number in the square
        startx = line * 3
        starty = col * 3

        lis = []

        # Find the element in the square
        for i in range(startx, startx + 3):
            for j in range(starty, starty + 3):
                lis.append(self[i, j])

        return lis

    def __setitem__(self, item, value):

        l, c = item

        if l < 0 or c < 0 or l >= self.height or c >= self.width:
            raise IndexError()
        if type(value) == int and (value < 0 or value > 9):
            raise ValueError()
        elif value is not None and type(value) != int:
            raise ValueError()

        self.entries[l * self.width + c] = value

    def setentries(self, entries):

        assert len(entries) == self.width * self.height

        for i in entries:
            if type(i) == int and (i < 0 or i > 9):
                raise ValueError()
            elif i is not None and type(i) != int:
                raise ValueError()

        self.entries = entries

    def get_square_number(self, l, c):

        if l < 0 or l > 9 or c < 0 or c > 9:
            raise IndexError()

        return (l // 3) * 3 + (c // 3)

    def __str__(self):

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
        for i, t in enumerate(self.tostring()):
            cur = "{" + str(i) + "}"
            total = total.replace(cur, t)

        return total

    def tostring(self):

        strelem = []

        for i in self.entries:
            if i is None:
                strelem.append(".")
            else:
                strelem.append(str(i))

        return tuple(strelem)
