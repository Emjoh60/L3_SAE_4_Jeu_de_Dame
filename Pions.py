from abc import ABC,abstractmethod
import functools
import Pions

@functools.total_ordering
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
    def capturerPion(p:Pions):
        pass
    
    #fonctions de comparaison
    def __eq__(self, other):
        if(type(other)==Pions):
            return (self.id==other.id) or ((self.x==other.x)and(self.y==other.y))
        else:
            return False

    def __ne__(self, other):
        if(type(other)==Pions):
            return self.id!=other.id
        else:
            return True
    
    def __le__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            if(self.x==other.x):
                if(self.y==other.y):
                    return False
                else:
                    return self.y<=other.y
            else:
                return self.x<=other.x

    
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            if(self.x==other.x):
                if(self.y==other.y):
                    return False
                else:
                    return self.y<other.y
            else:
                return self.x<other.x
    
    def __ge__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            if(self.x==other.x):
                if(self.y==other.y):
                    return False
                else:
                    return self.y>=other.y
            else:
                return self.x>=other.x
    
    def __gt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        else:
            if(self.x==other.x):
                if(self.y==other.y):
                    return False
                else:
                    return self.y>=other.y
            else:
                return self.x>=other.x
