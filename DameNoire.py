from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame

#création d'une classe
class DameNoire(Dame):
    #constructeur avec la position
    def __init__(self,id:str,x:int,y:int):
        super().__init__(id, x, y, "noir")
        
    #fonction pour capturer un pion
    def capturerPion(self,x:int,y:int,p:Pions):
        if(p.couleur=="blanc"):
            p.vivant = False
            p.coordonnees_X=-1
            p.coordonnees_Y=-1
            self.coordonnees_X=x
            self.coordonnees_Y=y
        else:
            return False  
