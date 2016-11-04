class Grid:
    entries = None
    height = 0
    width = 0

    # Initializes the game grid with the given height and width.
    # h and w parameters must be > than 0, or an AssertionError is raised
    def __init__(self, h, w):

        assert h > 0 and w > 0

        self.entries = [None for i in range(h * w)]
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

    def setEntries(self, entries):

        assert len(entries) == self.width * self.height

        for i in entries:
            assert type(i) == int or i == " "

        self.entries = entries

    def getLine(self, line):

        if line < 0 or line >= self.height:
            raise IndexError()

        start = line * self.width

        return self.entries[start:start + self.width]

    def getColumn(self, col):

        if col < 0 or col >= self.width:
            raise IndexError()

        start = col

        return self.entries[col::self.width]

    def __str__(self):

        total = ""

        for i in range(self.height):
            for j in range(self.width):
                item = self[i, j]
                if item == None:
                    total += " |"
                else:
                    total += str(item) + "|"
            total = total[0:len(total) - 1]+"\n"


        return total

