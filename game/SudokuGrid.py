from game import Grid


# Container class created from a Grid object. It uses to contain values contained in the range [1, 9]
# and None values, where None specifies and empty entry.
class SudokuGrid(Grid.Grid):
    # Initializes a Sudoku grid containing only None values in it.
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

    # Used to set the entry at the index(line, column) in the given tab.
    # The value must either be contained between [1, 9] or be a None value, or an error is raised
    def __setitem__(self, item, index):

        l, c = item

        if l < 0 or c < 0 or l >= self.height or c >= self.width:
            raise IndexError()
        if type(index) == int and (index < 0 or index > 9):
            raise ValueError()
        elif index is not None and type(index) != int:
            raise ValueError()

        self.entries[l * self.width + c] = index

    # Sets all the entries of the Sudoku grid, where all the entries are either between[1 , 9] or are None.
    # The length of the entries must be of 81
    def setentries(self, entries):

        assert len(entries) == self.width * self.height

        for i in entries:
            if type(i) == int and (i < 0 or i > 9):
                raise ValueError()
            elif i is not None and type(i) != int:
                raise ValueError()

        self.entries = entries

    # Returns the square number that can be used in getsquare method
    # for the given live and column in the grid.
    def get_square_number(self, l, c):

        if l < 0 or l > 9 or c < 0 or c > 9:
            raise IndexError()

        return (l // 3) * 3 + (c // 3)

    # Returns the grid as a String representation with
    # line and columns indicated, and where None values are replaces with spaces.
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
        for i, t in enumerate(self.__tostring()):
            cur = "{" + str(i) + "}"
            total = total.replace(cur, t)

        return total

    # Turns the grid into a tuple containing . for empty entries and the number as a string for the others.
    # This method should never be called from outside this function.
    def __tostring(self):

        strelem = []

        for i in self.entries:
            if i is None:
                strelem.append(".")
            else:
                strelem.append(str(i))

        return tuple(strelem)
