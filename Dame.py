
#création d'une classe
class Dame(Pions):
    #constructeur avec les paramètre de position
    def __init__(self, str id, int x, int y, str couleur):
        self.id = id
        self.coordonnees_X = x
        self.coordonnees_Y = y
        self.couleur = couleur
        self.vivant = True
        
    #constructeur sans les paramètre de position
    def __init_(self, str id, str couleur):
        self.id = id
        self.couleur = couleur
        self.vivant = True

    #constructeur à partir d'un pion
    def __init_(self, Pions p):
        self.id = p.id
        self.couleur = p.couleur
        self.coordonnees_X = p.coordonnees_X
        self.coordonnees_Y = p.coordonnees_Y
        self.vivant = True
