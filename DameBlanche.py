
#création d'une classe
class DameBlanche(Dame):
    #constructeur avec la position
    def __init__(self, str id, int x, int y):
        super().__init__(id, x, y, "blanc")
    #constructeur sans la position
    def __init__(self, str id):
        super().__init__(id, "blanc")

    #fonction pour vérifier le déplacement en diagonale
    def checkRegleDeDeplacement(int x, int y):
        if(self.coordonnees_X+1 == x and self.coordonnees_Y-1 == y):
            return True
        elif(self.coordonnees_X-1 == x and self.coordonnees_Y-1 == y):
            return True
        else:
            return False

    #constructeur à partir d'un pion
    def __init_(self, pionBlanc p):
        self.id = p.id
        self.couleur = p.couleur
        self.coordonnees_X = p.coordonnees_X
        self.coordonnees_Y = p.coordonnees_Y
        self.vivant = True
