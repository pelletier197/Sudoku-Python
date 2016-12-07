#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module is used to display a graphical interface in a window.
"""
__auteur__ = "ANMIG8"
__date__ = "2016-11-24"
__coequipiers__ = "RABOU264", "SUPEL55"

import winsound
from tkinter.filedialog import *
from tkinter.messagebox import *

from game import FileManager
from game import SudokuGenerator
from game import SudokuSolver

# Global variables
margin = 20
side = 50
width = height = margin * 2 + side * 9


class GraphicInterface(Frame):
    """This class constructs the graphical interface and display the game respecting the rules"""

    def __init__(self, parent, grid):
        """Initializes the parameters for every new charged game"""
        self.grid = grid
        self.original = grid.copy()
        solver = SudokuSolver.SudokuSolver()
        self.solution = solver.solve(grid)

        if self.solution is None:
            raise Exception("Cette grille n'a aucune solution possible")

        self.parent = parent
        Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        # call the function that initializes the window
        self.__init_graphic()

    def __init_graphic(self):
        """Creation of the window. Calls the functions that are essential to the game."""
        # Defines the title, the size and the window's parameters
        self.parent.title("Sudoku par Team Pizza Power")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=500, height=500, bg="#333333", highlightthickness=0)
        self.canvas.pack(fill=BOTH, side=TOP)
        # Creates the grid
        self.__draw_grid()
        self.__create_numbers()
        # Function that handle click and keypressed events
        self.canvas.bind("<Button-1>", self.__click_cell)
        self.canvas.bind("<Key>", self.__key)

    def __draw_grid(self):
        """Draw the grid in function of the parameters"""
        # Determines the color of the rows
        for i in range(10):
            # The light blue for the borders, dark blue for the intern lines
            color = "#81c9d5" if i % 3 == 0 else "#577275"
            # Defines the coordinates of the vertical lines
            x0 = margin + i * side
            y0 = margin
            x1 = margin + i * side
            y1 = height - margin
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=2)
            # and for the horizontal lines
            x0 = margin
            y0 = margin + i * side
            x1 = width - margin
            y1 = margin + i * side
            self.canvas.create_line(x0, y0, x1, y1, fill=color, width=2)

    def __create_numbers(self):
        """Places the numbers in the grid. This function is called every time the grid is modified"""
        # Removes he previous numbers
        self.canvas.delete("numbers")
        # Call functions of the other classes to get the solution of the grid
        solution = self.solution
        solver = SudokuSolver.SudokuSolver()
        wrongs = solver.get_rules_not_respected(self.grid)
        # Loop to find out what number is already in the grid or added to the grid
        for i in range(9):
            y = margin + i * side + side / 2
            for j in range(9):
                sol = solution[i, j]
                x = margin + j * side + side / 2
                original = self.original[i, j]
                # Blue if they are in the original grid, else gray
                color = "#629da7" if sol == original else "#adadad"
                self.canvas.create_text(x, y, text=self.grid[i, j], tags="numbers", fill=color, font=("Arial", 18))
                # If we are in the "clue" mode, right numbers are green, wrong are red
                if self.clue == OK and sol != original:
                    color = "#be3c3c" if (i, j) in wrongs and self.original[i, j] is None else "#3cbe42""#be3c3c"
                    self.canvas.create_text(x, y, text=self.grid[i, j], tags="numbers", fill=color, font=("Arial", 18))

    def __clear_numbers(self):
        """Clears the game and starts a new game with a new sudoku grid"""
        generator = SudokuGenerator.SudokuGenerator()
        gen = generator.generate_grid()
        self.grid = gen[0]
        self.solution = gen[1]
        self.original = self.grid.copy()
        self.canvas.delete("win")
        self.__create_numbers()

    def __click_cell(self, event):
        """Called when the window is clicked"""
        x, y = event.x, event.y
        # The click must be inside the grid
        if margin < x < width - margin and margin < y < height - margin:
            self.canvas.focus_set()
            # Computes line and columns in fuction of the click
            row, col = int((y - margin) / side), int((x - margin) / side)
            # If it is already clicked, we deselect it
            if self.original[row, col] is None:
                self.row, self.col = row, col
        # Highlights the selected case
        self.__selection_click()

    def __selection_click(self):
        """Highlights the selected cell"""
        # Cleares the previously selected cell
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = margin + self.col * side + 1
            y0 = margin + self.row * side + 1
            x1 = margin + (self.col + 1) * side - 1
            y1 = margin + (self.row + 1) * side - 1
            # Creates the rectangle
            self.canvas.create_rectangle(x0, y0, x1, y1, outline="#00bfff", tags="cursor")

    def __key(self, event):
        """Called when a key is pressed"""
        # Filter the input
        if self.row >= 0 and self.col >= 0 and event.char in "123456789":
            self.grid[self.row, self.col] = int(event.char)
            self.row, self.col = -1, -1
            self.__create_numbers()
            self.__selection_click()
            solver = SudokuSolver.SudokuSolver()
            wrongs = solver.get_rules_not_respected(self.grid)
            # Check if the player succeded completing the grid. The second condition checks in case a grid would have
            # more than one solution. If it has no error and its full, then the player won.
            if self.grid.entries == self.solution.entries or len(wrongs) == 0 and None not in self.grid.entries:
                self.__achieve()
        elif event.keycode == 8:
            self.grid[self.row, self.col] = None
            # Regenerate the grid
            self.__create_numbers()
            self.__selection_click()

    def __achieve(self):
        """Called when the player won the game"""
        # Centers the text
        x = y = margin + 4 * side + side / 2
        self.canvas.create_text(x, y, text="    Félicitations !\nVous avez réussi !",
                                tags="win", fill="white", font=("Lucida Calligraphy", 32, "bold"))
        path = sys.path[0]
        # Applause sound
        winsound.PlaySound(path + "/applaudissements.wav", winsound.SND_ASYNC)

    # Functions of the menu bar. Each function call an other function or display a dialog box

    def new(self):

        """
        Function which asks if the player whats to create a new game
        """
        if askyesno("Nouveau", "Etes-vous sûr de vouloir faire une nouvelle partie ?"):
            self.__clear_numbers()
            # Stop the music
            winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_LOOP)
            self.sound()

    def exit_(self):
        """Function which asks if the player wants to exit the game"""
        if askyesno("Quitter", "Etes-vous sûr de vouloir quitter le jeu ?"):
            self.parent.destroy()

    def rules(self):
        """Function which displays the rules of the game"""
        showinfo("Règles", "Le but du jeu est de remplir la grille avec une "
                           "série de chiffres allant de 1 à 9 tous "
                           "différents, qui ne se trouvent jamais plus d’une fois sur une "
                           "même ligne, dans une même colonne "
                           "ou dans une même sous-grille.\nSource : Wikipédia")

    def howto(self):
        """Function which displays how to play"""
        showinfo("Comment jouer",
                 "Cliquez sur une cellule du jeu et entrez une chiffre au clavier compris entre 1 et 9. "
                 "Une fois la grille juste et complétée, vous aurez gagné le jeu. Vous pouvez afficher des "
                 "indices en cliquant sur le menu en haut.  Vous pouvez à tout moment "
                 "quitter le jeu, commencer une nouvelle partie, sauvegarder votre partie ou en ouvrir une.")

    def about(self):
        """Function which displays what about this game"""
        showinfo("À propos...", "Sudoku crée par la Team Pizza Power (TPP).\n"
                                "Toutes les images et les sons sont libres de droits ou crées par la TPP.")

    def clue_t(self):
        """Function which displays what is the "clue" mode"""
        showinfo("Que fait indice ?",
                 "L'indice vous dit si le nombre que vous avez rentré est"
                 " valide pour la ligne, la colonne et le carré "
                 "en vérifiant s'ils y est déjà présent. Le chiffre sera "
                 "vert si votre nombre est valide, et rouge sinon.")

    def clue(self):
        """Set the self.clue depending of the player"""
        if self.checked.get() == 1:
            self.clue = OK
        else:
            self.clue = None
        self.__create_numbers()

    def sound(self):
        """Set the sound mode"""
        if self.soun.get() == 1:
            path = sys.path[0]
            winsound.PlaySound(path + "/jeu.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
        else:
            winsound.PlaySound(None, winsound.SND_ASYNC | winsound.SND_LOOP)

    def open_game(self):
        """To open a game previously saved"""
        file = askopenfilename(defaultextension="sdk", filetypes=[("Fichiers Sudoku", "*.sdk")],
                               title="Choisissez le fichier à ouvrir")
        try:
            grids = FileManager.read_sudoku(file)
            self.grid = grids[0]
            self.original = grids[1]
            self.solution = grids[2]
            self.__create_numbers()
        except FileNotFoundError:
            pass

    def save(self):
        """To save a game"""
        file = asksaveasfilename(defaultextension="sdk", filetypes=[("Fichiers Sudoku", "*.sdk")],
                                 title="Choisissez le fichier à ouvrir")
        try:
            FileManager.write_sudoku(file, self.grid, self.original, self.solution)
        except FileNotFoundError:
            pass

    def open(self):
        """Create the menu bar and call respective functions"""
        # Makes it not resizable
        self.parent.resizable(width=False, height=False)
        self.menubar = Menu(self.parent)
        self.parent['menu'] = self.menubar
        self.game_menu = Menu(self.menubar, tearoff=0, bg="#333333", fg="#adadad", activebackground="#707070", bd=0)

        self.menubar.add_cascade(label="Jeu", menu=self.game_menu)
        self.game_menu.add_command(label="Nouveau", command=self.new)
        self.game_menu.add_command(label="Ouvrir", command=self.open_game)
        self.game_menu.add_command(label="Sauvegarder", command=self.save)
        self.game_menu.add_command(label="Quitter", command=self.exit_)

        self.settings_menu = Menu(self.menubar, tearoff=0, bg="#333333", fg="#adadad", activebackground="#707070")
        self.menubar.add_cascade(label="Paramètres", menu=self.settings_menu)
        # Can be checked
        self.checked = IntVar(self.parent)
        self.settings_menu.add_checkbutton(label="Indices", onvalue=1, offvalue=0, variable=self.checked,
                                           command=self.clue, selectcolor="#adadad")
        self.soun = IntVar(self.parent)
        self.settings_menu.add_checkbutton(label="Son", onvalue=1, offvalue=0, variable=self.soun, command=self.sound,
                                           selectcolor="#adadad")

        self.help_menu = Menu(self.menubar, tearoff=0, bg="#333333", fg="#adadad", activebackground="#707070")
        self.menubar.add_cascade(label="Aide", menu=self.help_menu)
        self.help_menu.add_command(label="Règles", command=self.rules)
        self.help_menu.add_command(label="Comment jouer", command=self.howto)
        self.help_menu.add_command(label="Indice ?", command=self.clue_t)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="À propos", command=self.about)

        self.parent.config(menu=self.menubar)
        # Creates the window
        self.parent.mainloop()
