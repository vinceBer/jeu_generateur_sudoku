from random import seed
from random import randint

# https://www.youtube.com/watch?v=O2pcNxzlL0Q
class SudokuGrid:
    def __init__(self):
        # initialisation de la seed des nombres aléatoires en fonction de l'heure
        seed(None)
        # self.grid : grille initiale
        # self.final: grille solution
        # self.copygrid: grille temporaire en cas de plusieurs solutions
        self.grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.final = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.copygrid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

        # initialisation du nombre de zeros et du nombre de solutions
        self.nbZeros = 0
        self.found = 0

    def affiche(self):
        print("self.grid")
        nbzero=0
        #pour connaitre le nombre de 0 présents dans la grille self.grid
        #et l'afficher dans le terminal
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                print(self.grid[i][j], end=" ")
                if self.grid[i][j] == 0:
                    nbzero += 1
            print()
        print(nbzero)
        print()

        #pour connaitre le nombre de 0 présents dans la grille self.final
        #et l'afficher dans le terminal
        nbzero=0
        print("self.final")
        for i in range(0, len(self.final)):
            for j in range(0, len(self.final)):
                print(self.final[i][j], end=" ")
                if self.final[i][j] == 0:
                    self.nbZeros += 1
            print()
        print("nbzero",self.nbZeros)
        print()

    # On regarde si le nombre n peut convenir sur la grille
    def n_valide(self, y, x, n):
        # On determine si le nombre est valide sur sa ligne
        for x0 in range(len(self.grid)):
            if self.grid[y][x0] == n:
                return False
        # On determine si le nombre est valide sur sa colonne
        for y0 in range(len(self.grid)):
            if self.grid[y0][x] == n:
                return False
        # On determine si le nombre est valide dans sa sous grille
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for i in range(0, 3):
            for j in range(0, 3):
                if self.grid[y0 + i][x0 + j] == n:
                    return False
        return True

    # Résolution complete grille Sudoku
    def solve(self):
        # On recherche les solutions uniques
        if self.found > 1:
            return

        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid)):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self.n_valide(y, x, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return

        # on recopie la solution dans la grille self.final
        for i in range(0, len(self.grid)):
            for j in range(0, len(self.grid)):
                self.final[i][j] = self.grid[i][j]
        self.found = self.found + 1

    # Création grille avec une diagonale 3x3 non vide et valide
    def start(self):
        self.found = 0

        for k in range(0, 3):
            # Génération d'un tableau aléatoire de taille 9 avec les nombres 1 à 9 qui ne se repetent pas
            myarray = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            for l in range(0, 9):
                value = randint(1, 9)
                while (value in myarray):
                    value = randint(1, 9)
                myarray[l] = value
            # Remplissage des 3 sous grilles 3x3 en diagonal
            l = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    self.grid[k * 3 + i][k * 3 + j] = myarray[l]
                    l = l + 1

    # Création d'une grille de Sudoku avec xx trous
    def create(self, nbEmptyCells):
        # On recopie la grille solution dans la grille initiale
        if self.found == 0:
            return

        # On tire aléatoirement nbEmptyCells valeurs pour faire des trous dans la grille
        # l: nombre de trous
        # nbTours: nombre de tirages aléaroires (max = 100)
        l = 0
        nbTour = 0

        while l < nbEmptyCells and nbTour < 100:
            self.found = 0
            nbTour += 1

            # on recopie dans self.gris et self.copygrid la deniere matrice de self.final
            for i in range(0, len(self.grid)):
                for j in range(0, len(self.grid)):
                    self.grid[i][j] = self.final[i][j]
                    self.copygrid[i][j] = self.final[i][j]

            # Identification d'une cellule aleatoire de la matrice
            value = randint(0, 80)
            x0 = (value // 9)
            y0 = (value - x0 * 9)

            originalValue = self.grid[x0][y0]
            if originalValue != 0:
                self.grid[x0][y0] = 0
                self.solve()
                # Il recomplète la grile pour s'assurer qu'il y ait une solution
#                print("nbTour:%d", nbTour)
#                self.affiche()
#                print("self.found:%d",self.found)
                # cas une solution unique trouvee
                if self.found == 1:
                    for i in range(0, len(self.grid)):
                        for j in range(0, len(self.grid)):
                            self.final[i][j] = self.grid[i][j]
                    l = l + 1
                else:
                    for i in range(0, len(self.grid)):
                        for j in range(0, len(self.grid)):
                            self.final[i][j] = self.copygrid[i][j]

        # self.grid contient les zeros et a une unique solution
        # on recalcule self.final pour avoir la grille solution
        self.found = 0
        self.solve()

    # Pour recuperer la grille avec les zeros
    def getGrid(self):
        return self.grid

    # Pour recuperer la grille solution
    def getFinalGrid(self):
        return self.final

    def getNbZeros(self):
        return self.nbZeros

    # Pour initilaiser le jeu avec nbEmptyCells zeros (difficile d'avoir une solution unique au dela de 55 cellules vides)
    def reset(self, nbEmptyCells):
        # Creation d'une grille avec la diagonlae 3x3 remplie
        self.start()
        # On résoud la grille complète de Sudoku
        self.solve()
        self.create(nbEmptyCells)
        self.affiche()

"""    def main():
        toto=SudokuGrid()
        toto.reset()"""
