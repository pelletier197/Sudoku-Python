# A grid is a container used as a 2 dimensional array and where the entries of the given
# grid are only numbers or None values.
class Grid:
    # Initializes the game grid with the given height and width.
    # h and w parameters must be > than 0, or an AssertionError is raised
    def __init__(self, h, w):

        assert h > 0 and w > 0

        self.entries = [None in range(h * w)]
        self.width = w
        self.height = h

    # Use this method to get the item situated on the line and the column given
    # by the tuple item = (line, column).
    # If line >= height or column >= width, then an IndexError is raised. Same event occur if
    # line or column < 0
    def __getitem__(self, item):

        l, c = item

        if l < 0 or c < 0 or l >= self.height or c >= self.width:
            raise IndexError()

        return self.entries[l * self.width + c]

    # Use this method to set the item situated on the line and the column given
    # by the tuple item = (line, column) to the given value.
    # If line >= height or column >= width, then an IndexError is raised. Same event occur if
    # line or column < 0
    def __setitem__(self, item, value):

        l, c = item

        if l < 0 or c < 0 or l >= self.height or c >= self.width:
            raise IndexError()

        self.entries[l * self.width + c] = value

    # Sets the entries of the grid. The entries must either be int values or None value.
    # Also, the number of elements in entries parameter must be width * height. Use this function to set
    # all the entries of the grid
    def setentries(self, entries):

        assert len(entries) == self.width * self.height

        for i in entries:
            assert type(i) == int or i is None

        self.entries = entries

    # Returns the line of the grid associated to the given index,
    #  where line parameter is contained in range [0, width-1]
    def getline(self, line):

        if line < 0 or line >= self.height:
            raise IndexError()

        start = line * self.width

        return self.entries[start:start + self.width]

    # Returns the column of the grid associated to the given column index,
    # here col is contained in range [0,height-1]
    def getcolumn(self, col):

        if col < 0 or col >= self.width:
            raise IndexError()

        return self.entries[col::self.width]

    # Returns the grid in a string representation
    def __str__(self):

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
