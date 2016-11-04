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

    def getSquare(self, number):

        if number < 0 or number > 8:
            raise IndexError()

        col = number % 3
        line = number // 3

        # Finds the top left number in the square
        startX = line * 3
        startY = col * 3

        list = []

        # Find the element in the square
        for i in range(startX, startX + 3):
            for j in range(startY, startY + 3):
                list.append(self[i, j])

        return list

    def getSquareNumber(self, l, c):

        if l < 0 or l > 9 or c < 0 or c > 9:
            raise IndexError()

        return (l // 3) * 3 + (c // 3)

