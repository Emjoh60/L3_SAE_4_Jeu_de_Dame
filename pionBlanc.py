from Pions import Pions
import pionNoir

#création d'une classe
class pionBlanc(Pions):
    #constructeur avec la position
    def __init__(self,id:str,x:int,y:int):
        super().__init__(id, x, y, "blanc")

    #fonction pour vérifier le déplacement en diagonale
    def checkRegleDeDeplacement(self,x:int,y:int):
        if(self.coordonnees_X+1 == x and self.coordonnees_Y+1 == y):
            return True
        elif(self.coordonnees_X-1 == x and self.coordonnees_Y+1 == y):
            return True
        else:
            return False

    #fonction pour capturer un pion
    def capturerPion(p:Pions):
        if(p.couleur=="noir"):
            p.vivant = False
        

