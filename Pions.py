from abc import ABC,abstractmethod
import Pions

#création d'une classe
class Pions:
    #constructeur avec les paramètre de position
    def __init__(self,id:str,x:int,y:int,couleur:str):
        self.id = id
        self.coordonnees_X = x
        self.coordonnees_Y = y
        self.couleur = couleur
        self.vivant = True

    #fonction pour vérifier le déplacement en diagonale
    @abstractmethod
    def checkRegleDeDeplacement(self,x:int,y:int)->bool:
        pass

    #fonction pour déplacer le pion en diagonale
    def se_deplacer(self,x:int,y:int):
        if(self.checkRegleDeDeplacement(x,y)):
            self.coordonnees_Y = y
            self.coordonnees_X = x
            return True
        else:
            return False

    #fonction pour capturer un pion
    @abstractmethod
    def capturerPion(self,x:int,y:int,p:Pions):
        pass