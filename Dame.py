from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir

#création d'une classe
class Dame(Pions):
    #constructeur avec les paramètre de position
    def __init__(self,id:str,x:int,y:int,couleur:str):
        self.id = id
        self.coordonnees_X = x
        self.coordonnees_Y = y
        self.couleur = couleur
        self.vivant = True