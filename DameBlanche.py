from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame

#création d'une classe
class DameBlanche(Dame):
    #constructeur avec la position
    def __init__(self,id:str,x:int,y:int):
        super().__init__(id, x, y, "blanc")

    #constructeur à partir d'un pion
    def __init_(self,p:pionBlanc):
        self.id = p.id
        self.couleur = p.couleur
        self.coordonnees_X = p.coordonnees_X
        self.coordonnees_Y = p.coordonnees_Y
        self.vivant = True

    #fonction pour capturer un pion
    def capturerPion(self,x:int,y:int,p:Pions):
        if(p.couleur=="noir"):
            p.vivant = False
            if((p.coordonnees_X in range(self.coordonnees_X,x) or (p.coordonnees_X in range(x,self.coordonnees_X))) and (p.coordonnees_Y in range(self.coordonnees_Y,y) or (p.coordonnees_Y in range(y,self.coordonnees_Y)))):
                self.coordonnees_X=x
                self.coordonnees_Y=y 
            else:
                return False
        else:
            return False