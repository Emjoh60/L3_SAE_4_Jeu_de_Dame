from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame
from DameBlanche import DameBlanche

#création d'une classe
class DameNoire(Dame):
    #constructeur avec la position
    def __init__(self,id:str,x:int,y:int):
        super().__init__(id, x, y, "noir")

    #fonction pour vérifier le déplacement en diagonale
    def checkRegleDeDeplacement(self,x:int,y:int):
        if(self.coordonnees_X+1 == x and self.coordonnees_Y-1 == y):
            return True
        elif(self.coordonnees_X-1 == x and self.coordonnees_Y-1 == y):
            return True
        else:
            return False
        
    #constructeur à partir d'un pion
    def __init_(self,p : pionNoir):
        self.id = p.id
        self.couleur = p.couleur
        self.coordonnees_X = p.coordonnees_X
        self.coordonnees_Y = p.coordonnees_Y
        self.vivant = True
