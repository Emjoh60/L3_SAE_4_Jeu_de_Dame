from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame
from DameBlanche import DameBlanche
from DameNoire import DameNoire
from Damier import Damier
import constants as const
from math import log

class Partie:
    def __init__(self,id:str,winner:str):
        self.id = id
        self.winner = winner
        self.damier=Damier("1",const.PLATEAU)

        # Initialisation de la liste de pions
        self.listePion={}
        cpt=1
        for y in range(1,4):
            if (y % 2) == 0:
                for x in range(2,const.PLATEAU,2):
                    self.addPion(pionBlanc("B"+str(cpt),x,y))
            else:
                for x in range(1,const.PLATEAU,2):
                    self.addPion(pionBlanc("B"+str(cpt),x,y))
            cpt=cpt+1

        cpt=1
        for y in range(const.PLATEAU-2,const.PLATEAU+1):
            if (y % 2) == 0:
                for x in range(2,const.PLATEAU,2):
                    self.addPion(pionNoir("N"+str(cpt),x,y))
            else:
                for x in range(1,const.PLATEAU,2):
                    self.addPion(pionNoir("N"+str(cpt),x,y))
            cpt=cpt+1

    def addPion(self,pion:Pions):
        self.listePion.insert(pion)
        self.listePion.sort()

    def removePion(self,pion:Pions):
        self.listePion.remove(pion)
        self.listePion.sort()

    def getPion(self,id:str):
        for p in self.listePion:
            if(p.id==id):
                return p

    def getPionPos(self,posX:int, posY:int):
        nb:int
        min:int
        max:int
        max=self.listePion.__sizeof__()
        min=0
        while(debut!=fin):
            nb=(min+max)/2
            var=self.listePion[nb]
            if(var.x==posX):
                if(var.y==posY):
                    return var
                elif(var.y<posY):
                    debut=var
                    min=nb
                elif(var.y>posY):
                    fin=var
                    max=nb
            elif(var.x<posX):
                debut=var
                min=nb
            elif(var.x>posX):
                fin=var
                max=nb
        return False


    def getPionIndex(self,index:int):
        return self.listePion[index]

    def checkWin(self):
        cptWhite=0
        cptBlack=0
        for pion in self.listePion:
            if pion.couleur=="blanc" and pion.vivant:
                cptWhite=cptWhite+1
            elif pion.couleur=="noir" and pion.vivant:
                cptBlack=cptBlack+1
        if cptWhite>0 and cptBlack>0:
            return False
        elif cptWhite>0 and cptBlack==0:
            return "W"
        elif cptWhite==0 and cptBlack>0:
            return "B"


    def checkCapture(self,pion, POS_x:int, POS_y:int):
        if(type(pion)=="pionNoir.pionNoir"):
            pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
            if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                if (pion.coordonnees_X+2 == POS_x and pion.coordonnees_Y+2 == POS_y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
                    
            pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
            if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                if (pion.coordonnees_X+2 == POS_x and pion.coordonnees_Y-2 == POS_y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
            if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                if (pion.coordonnees_X-2 == POS_x and pion.coordonnees_Y+2 == POS_y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
            if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                if (pion.coordonnees_X-2 == POS_x and pion.coordonnees_Y-2 == POS_y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            return False

        elif(type(pion)=="pionBlanc.pionBlanc"):
            pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
            if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                if (pion.coordonnees_X+2 == POS_x and pion.coordonnees_Y+2 == POS_y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
            if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                if (pion.coordonnees_X+2 == POS_x and pion.coordonnees_Y-2 == y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
            if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                if (pion.coordonnees_X-2 == POS_x and pion.coordonnees_Y+2 == y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
            if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                if (pion.coordonnees_X-2 == POS_x and pion.coordonnees_Y-2 == POS_y):
                    if (pion.se_deplacer(POS_x,POS_y)):
                        pion.capturer(pAutour)
                        return True
            return False
        elif(type(pion)=="DameNoire.DameNoire"):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(x+1,y+1)):
                    return True
                elif(type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(x+1,y+1)):
                    
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase and y>0:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(x+1,y-1)):
                    return True
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>0 and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(x-1,y+1)):
                    return True
                x=x-1
                y=y+1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            while x>0 and y>0:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionBlanc.pionBlanc" or type(pAutour)=="DameBlanche.DameBlanche" )and not(self.getPionPos(x-1,y-1)):
                    return True
                x=x-1
                y=y-1
        elif(type(pion)=="DameBlanche.DameBlanche"):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(x+1,y+1)):
                    return True
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase and y>0:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(x+1,y-1)):
                    return True
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>0 and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(x-1,y+1)):
                    return True
                x=x-1
                y=y+1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            while x>0 and y>0:
                pAutour=self.getPionPos(x,y)
                if (type(pAutour)=="pionNoir.pionNoir" or type(pAutour)=="DameNoire.DameNoire" )and not(self.getPionPos(x-1,y-1)):
                    return True
                x=x-1
                y=y-1

    def checkDeplacement(self,pion:Pions, X:int, Y:int):
        if not(self.getPionPos(X,Y)):
            if(type(pion)=="pionNoir.pionNoir"):
                if(X==X-1 or X==X+1) and (Y==Y-1):
                    return True
                else:
                    return False

            elif(type(pion)=="pionBlanc.pionBlanc"):
                if(X==X-1 or X==X+1) and (Y==Y+1):
                    return True
                else:
                    return False
                
            elif(type(pion)=="DameNoire.DameNoire"):
                if(X-pion.coordonnees_X==Y-pion.coordonnees_Y):
                    for i in range(1,X-pion.coordonnees_X):
                        if (self.getPionPos(pion.coordonnees_X+i,pion.coordonnees_Y+i)):
                            return False
                    return True
                else:
                    return False
            elif(type(pion)=="DameBlanche.DameBlanche"):
                if(X-pion.coordonnees_X==Y-pion.coordonnees_Y):
                    for i in range(1,X-pion.coordonnees_X):
                        if (self.getPionPos(pion.coordonnees_X+i,pion.coordonnees_Y+i)):
                            return False
                    return True
                else:
                    return False
        else:
            return False
    
    def effectuerDeplacement(self,x:int,y:int,pion:Pions):
        if(pion.vivant) and  (x>0 and x<self.damier.nbCase) and (y>0 and y<self.damier.nbCase):
            if(not self.checkCapture(pion)):
                if(self.checkDeplacement(pion,x,y)):
                    pion.se_deplacer(x,y)
                else:
                    return False                
        else:
            return False