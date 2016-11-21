import argparse

import Troll
import game.SudokuGenerator
from game import FileManager
from game.SudokuSolver import SudokuSolver

"python C:/Users/sunny/PycharmProjects/game/sudoku.py --mode manuel C:/Users/sunny/PycharmProjects/game/game/yomama.txt"
"python C:/Users/sunny/PycharmProjects/game/sudoku.py --mode manuel C:/Users/sunny/PycharmProjects/game/game/tester.txt"

def graphic_manuel():
    pass


def graphic_auto():
    print("\nCe mode n'est pas supporté. Passez en affichage graphique pour le mode automatique")


def textuel_auto():
    # enter auto mode
    print()
    grids = FileManager.read_sudoku(args.file)
    for grid in grids:
        print("Calcul...")
        print(solver.solve(grid))
    print("Terminé !")



def textuel_manuel():
    print("\nInitialisation... ")
    grid = FileManager.read_sudoku(args.file)[0]
    solution = solver.solve(grid)
    while None in grid.entries:

        print(grid)
        print("\n" + "-" * 30 + "\n")
        val = input("Entrez une [ligne (1 à 9)], [colonne(1 à 9)], [valeur (1 à 9)] : ")
        print()
        val = val.split(",")
        try:
            line, col, val = int(val[0]) - 1, int(val[1]) - 1, int(val[2])
            if grid[line, col] is not None:
                print("Cette entrée est déjà vérifiée. Choisissez en une autre")
                continue

            grid[line, col] = val

            # If the input matches the solution, we accept it
            if grid[line, col] != solution[line, col]:

                # Check if the solution is valid (in case of multiple valid grid)
                tempsol = solver.solve(grid)
                if tempsol is not None:
                    solution = tempsol
                    continue
                # Else, the grid is not valid, so remove the input and notify user
                grid[line, col] = None
                print("Erreur ! Ce n'est pas le bon chiffre")
                continue

            print("Vous avez entré la bonne valeur !")
        except Exception:
            print("Entrée invalide !")

    Troll.troll()


#
#
#
# Main application code
#
#
# Sudoku solver and generator
solver = SudokuSolver()
gener = game.SudokuGenerator.SudokuGenerator()

parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["manuel", "auto"],
                    help="Entrez cette commande pour entrer en mode manuel ou auto", type=str)
parser.add_argument("--affichage", choices=["textuel", "graphique"],
                    help="Entrez cette commande pour séléctioner l'affichage textuel ou graphique", type=str)
parser.add_argument("file", help="Le fichier à specifier pour lire la grille", type=str)

args = parser.parse_args()

mode = "manuel"
display = "textuel"

if args.mode is not None:
    mode = args.mode
if args.affichage is not None:
    display = args.affichage

if mode == "manuel" and display == "textuel":
    textuel_manuel()
elif mode == "auto" and display == "textuel":
    textuel_auto()
elif mode == "manuel" and display == "graphique":
    graphic_manuel()
elif mode == "auto" and display == "graphique":
    graphic_auto()

