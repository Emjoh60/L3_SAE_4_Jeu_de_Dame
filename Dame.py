from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir

# Création d'une classe Dame
class Dame(Pions):
    # Constructeur avec les paramètre de position
    def __init__(self,id:str,x:int,y:int,couleur:str):
        self.id = id
        self.coordonnees_X = x
        self.coordonnees_Y = y
        self.couleur = couleur
        self.vivant = True

    # Fonction pour vérifier le déplacement en diagonale
    def checkRegleDeDeplacement(self,x:int,y:int):
        if(abs(x-self.coordonnees_X)==abs(y-self.coordonnees_Y)):
            return True
