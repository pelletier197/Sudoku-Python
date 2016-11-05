from game import SudokuGrid
from game import SudokuGenerator
from game import SudokuSolver


# Reads a sudoku grid into a given text file and return it as a SudokuGrid object
def readSudoku(file):
    with open(file, 'r') as fi:
        text = fi.read()
        text = text.replace(" ", "").replace("\n", "")

    return __toGrid(text)


# Converts the given text input into a grid of sudoku.
# This function should only be used internally and not be called from outside this class.
def __toGrid(text):
    grid = SudokuGrid.SudokuGrid()
    entries = []

    for i in text:
        if i == ".":
            entries.append(None)
        else:
            entries.append(int(i))
    grid.setEntries(entries)

    return grid


# Writes the given sudoku grid into the given file as a text representation.
# You may deserialize this grid by calling readSudoku
def writeSudoku(file, grid):
    with open(file, "w") as fi:
        fi.write(__fromGrid(grid))


# Creates the text associated to a SudokuGrid. This function is used to serialize the sudoku grid.
# This function is used internally and should not be called outside this class.
def __fromGrid(grid):
    text = ""

    for i in grid.entries:
        if i is None:
            text += "."
        else:
            text += str(i)

    return text


generator = SudokuGenerator.SudokuGenerator()
solver = SudokuSolver.SudokuSolver()

grids = generator.generateGrid()

print(str(grids[0]))
print(str(grids[1]))

print(solver.solve(grids[0]))

test = readSudoku("yomama.txt")
print(test)
