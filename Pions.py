from abc import ABC,abstractmethod

#création d'une classe
class Pions:
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

    #fonction pour vérifier le déplacement en diagonale
    @abstractmethod
    def checkRegleDeDeplacement(int x, int y):
        pass

    #fonction pour déplacer le pion en diagonale
    def se_deplacer(int x, int y):
        try:
            self.coordonnees_X
            self.coordonnees_Y
            if(checkRegleDeDeplacement(x,y)):
                self.coordonnees_Y = y
                self.coordonnees_X = x
        except NameError:
            self.coordonnees_X = x
            self.coordonnees_Y = y

    #fonction pour capturer un pion
    @abstractmethod
    def capturerPion(Pions p):
        pass
