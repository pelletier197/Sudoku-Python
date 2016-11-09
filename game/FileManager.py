from game import SudokuGrid


# Reads a list of soduku grids in a txt file and returns it as a list of sudoku grids
def read_sudoku(file):
    with open(file, 'r') as fi:
        text = fi.read()
        text = text.replace(" ", "").replace("\n", "")

    gridqty = len(text) // 81
    grids = []

    for t in range(gridqty):
        cur = text[t * 81:t * 81 + 81]
        grids.append(__togrid(cur))

    return grids


# Converts the given text input into a grid of sudoku.
# This function should only be used internally and not be called from outside this class.
def __togrid(text):
    grid = SudokuGrid.SudokuGrid()
    entries = []

    for i in text:
        if i == ".":
            entries.append(None)
        else:
            entries.append(int(i))
    grid.setentries(entries)

    return grid


# Writes the given sudoku grid into the given file as a text representation.
# You may deserialize this grid by calling readSudoku
def write_sudoku(file, grid):
    with open(file, "w") as fi:
        fi.write(__fromgrid(grid))


# Creates the text associated to a SudokuGrid. This function is used to serialize the sudoku grid.
# This function is used internally and should not be called outside this class.
def __fromgrid(grid):
    text = ""

    for i in grid.entries:
        if i is None:
            text += "."
        else:
            text += str(i)

    return text
