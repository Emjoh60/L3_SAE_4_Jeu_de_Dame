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
        self.listePion=[]
        cpt=1
        for y in range(1,4):
            if (y % 2) == 0:
                for x in range(2,const.PLATEAU+1,2):
                    id="B"+str(cpt)
                    self.damier.modifier(x,y,id)
                    self.addPion(pionBlanc("B"+str(cpt),x,y))
                    cpt=cpt+1
            else:
                for x in range(1,const.PLATEAU,2):
                    id="B"+str(cpt)
                    self.damier.modifier(x,y,id)
                    self.addPion(pionBlanc("B"+str(cpt),x,y))
                    cpt=cpt+1

        cpt=1
        for y in range(const.PLATEAU-2,const.PLATEAU+1):
            if (y % 2) == 0:
                for x in range(2,const.PLATEAU+1,2):
                    id="N"+str(cpt)
                    self.damier.modifier(x,y,id)
                    self.addPion(pionNoir("N"+str(cpt),x,y))
                    cpt=cpt+1
            else:
                for x in range(1,const.PLATEAU,2):
                    id="N"+str(cpt)
                    self.damier.modifier(x,y,id)
                    self.addPion(pionNoir("N"+str(cpt),x,y))
                    cpt=cpt+1

    def afficherListePion(self):
        for i in self.listePion :
            print("Pions :"+str(i.id)+" Couleur : "+str(i.couleur)+" X : "+str(i.coordonnees_X)+" Y : "+str(i.coordonnees_Y))
        self.damier.afficher_matrice()

    def addPion(self,pion:Pions):
        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y,pion.id)
        self.listePion.append(pion)

    def removePion(self,pion:Pions):
        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y," ")
        self.listePion.remove(pion)

    def getPion(self,id:str):
        for p in self.listePion:
            if(p.id==id):
                return p

    def getPionPos(self,posX:int, posY:int):
        x=str(self.damier.plateau[posX-1,posY-1])
        print(x)
        if x:
            return self.getPion(x)
        else:
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


    def checkCapture(self,pion):
        if(isinstance(pion, pionNoir)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>1):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    return True
            if(pion.coordonnees_X>1 and pion.coordonnees_Y<self.damier.nbCase-1): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X>1 and pion.coordonnees_Y>1): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    return True
            return False
        elif(isinstance(pion, pionBlanc)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>1):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    return True
            if(pion.coordonnees_X>1 and pion.coordonnees_Y<self.damier.nbCase-1):     
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X>1 and pion.coordonnees_Y>1):    
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    return True
            return False
        elif(isinstance(pion, DameNoire)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase-1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y+1)):
                    return True
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x+1,y+1)) :
                    y=0
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase-1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y-1)):
                    return True
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x+1,y-1)) : 
                     y=0
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x-1,y+1)):
                    return True
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x-1,y+1)) :
                    x=0
                x=x-1
                y=y+1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            while x>1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x-1,y-1)):
                    return True
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x-1,y-1)) :
                     x=0
                x=x-1
                y=y-1
            return False
        elif(isinstance(pion, DameBlanche)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase-1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y+1)):
                    return True
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x+1,y+1)):
                     x=self.damier.nbCase
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase-1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y-1)):
                    return True
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x+1,y-1)):
                     x=self.damier.nbCase
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x-1,y+1)):
                    return True
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x-1,y+1)):
                     y=self.damier.nbCase
                x=x-1
                y=y+1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            while x>1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x-1,y-1)):
                    return True
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x-1,y-1)):
                     x=0
                x=x-1
                y=y-1
            return False
        
    def getCapture(self,pion):
        listePosition=[]
        if(isinstance(pion, pionNoir)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>1):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y-2))
            if(pion.coordonnees_X>1 and pion.coordonnees_Y<self.damier.nbCase-1): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X>1 and pion.coordonnees_Y>1): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y-2))
        elif(isinstance(pion, pionBlanc)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>1):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y-2))
            if(pion.coordonnees_X>1 and pion.coordonnees_Y<self.damier.nbCase-1):     
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X>1 and pion.coordonnees_Y>1):    
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y-2))
        elif(isinstance(pion, DameNoire)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase-1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y+1)):
                    listePosition.append((pAutour,x+1,y+1))
                    x=x+2
                    y=y+2
                    while x<=self.damier.nbCase and y<=self.damier.nbCase:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            y=self.damier.nbCase+1
                        x=x+1
                        y=y+1
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or ((isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x+1,y+1))) :
                    y=self.damier.nbCase
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase-1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y-1)):
                    listePosition.append((pAutour,x+1,y-1))
                    x=x+2
                    y=y-2
                    while x<=self.damier.nbCase and y>=0:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            y=-1
                        x=x+1
                        y=y-1
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or ((isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x+1,y-1))) : 
                    y=0
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x-1,y+1)):
                    listePosition.append((pAutour,x-1,y+1))
                    x=x-2
                    y=y+2
                    while x>=0 and y<=self.damier.nbCase:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            x=-1
                        x=x-1
                        y=y+1
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x-1,y+1)) :
                    x=0
                x=x-1
                y=y+1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            while x>1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x-1,y-1)):
                    listePosition.append((pAutour,x-1,y-1))
                    x=x-2
                    y=y-2
                    while x>=0 and y>=0:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            x=-1
                        x=x-1
                        y=y-1
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or ((isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x-1,y-1))) :
                    x=0
                x=x-1
                y=y-1
        elif(isinstance(pion, DameBlanche)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase-1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y+1)):
                    listePosition.append((pAutour,x+1,y+1))
                    x=x+2
                    y=y+2
                    while x<=self.damier.nbCase and y<=self.damier.nbCase:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            x=self.damier.nbCase+1
                        x=x+1
                        y=y+1
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or ((isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x+1,y+1))):
                     x=self.damier.nbCase
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase-1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y-1)):
                    listePosition.append((pAutour,x+1,y-1))
                    x=x+2
                    y=y-2
                    while x<=self.damier.nbCase and y>=0:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            x=self.damier.nbCase+1
                        x=x+1
                        y=y-1
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or ((isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x+1,y-1))):
                    x=self.damier.nbCase
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>1 and y<self.damier.nbCase-1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x-1,y+1)):
                    listePosition.append((pAutour,x-1,y+1))
                    x=x-2
                    y=y+2
                    while x>=0 and y<=self.damier.nbCase:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            x=-1
                        x=x-1
                        y=y+1
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or ((isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x-1,y+1))):
                     y=self.damier.nbCase
                x=x-1
                y=y+1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            while x>1 and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x-1,y-1)):
                    listePosition.append((pAutour,x-1,y-1))
                    x=x-2
                    y=y-2
                    while x>=0 and y>=0:
                        pAutourBis=self.getPionPos(x,y)
                        if not pAutourBis:
                            listePosition.append((pAutour,x,y))
                        else:
                            x=-1
                        x=x-1
                        y=y-1
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or ((isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x-1,y-1))):
                    x=0
                x=x-1
                y=y-1
        return listePosition
    

    def checkDeplacement(self,pion:Pions, X:int, Y:int):
        if not(self.getPionPos(X,Y)):
            if(isinstance(pion, pionNoir)):
                if(X==pion.coordonnees_X-1 or X==pion.coordonnees_X+1) and (Y==pion.coordonnees_Y-1):
                    return True
                else:
                    return False
            elif(isinstance(pion, pionBlanc)):
                if(X==pion.coordonnees_X-1 or X==pion.coordonnees_X+1) and (Y==pion.coordonnees_Y+1):
                    return True
                else:
                    return False   
            elif(isinstance(pion, DameNoire)):
                if(abs(X-pion.coordonnees_X)==abs(Y-pion.coordonnees_Y)):
                    for i in range(1,X-pion.coordonnees_X):
                        if (self.getPionPos(pion.coordonnees_X+i,pion.coordonnees_Y+i)):
                            return False
                    return True
                else:
                    return False
            elif(isinstance(pion, DameBlanche)):
                if(abs(X-pion.coordonnees_X)==abs(Y-pion.coordonnees_Y)):
                    for i in range(1,X-pion.coordonnees_X):
                        if (self.getPionPos(pion.coordonnees_X+i,pion.coordonnees_Y+i)):
                            return False
                    return True
                else:
                    return False
        else:
            return False
    
    def effectuerDeplacement(self,x:int,y:int,pion:Pions):
        if(pion.vivant) and  (x>0 and x<=self.damier.nbCase) and (y>0 and y<=self.damier.nbCase):
            print("Premier OK")
            if(not self.checkCapture(pion)):
                print("Pas capture OK")
                if(self.checkDeplacement(pion,x,y)):
                    print("Deplacement OK")
                    self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y," ")
                    pion.se_deplacer(x,y)
                    self.checkDame(pion)
                    self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y,pion.id)
                    return True
                else:
                    print("Deplacement pas OK")
                    return False
            else:
                print("Pas capture Non OK")
                val=False
                for i in self.getCapture(pion):
                    print(i[0])
                    if x==i[1] and y==i[2]:
                        print("Capture")
                        val=True
                        print("Deplacement OK")
                        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y," ")
                        self.damier.modifier(i[0].coordonnees_X,i[0].coordonnees_Y," ")
                        pion.capturerPion(i[1],i[2],i[0])
                        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y,pion.id)
                return val    
        else:
            return False

    def checkDame(self,pion:Pions):
        if(isinstance(pion, pionNoir)):
            if(pion.coordonnees_Y==1):
                self.addPion(DameNoire(pion.id,pion.coordonnees_X,pion.coordonnees_Y))
                self.removePion(pion)
        elif(isinstance(pion, pionBlanc)):
            if(pion.coordonnees_Y==self.damier.nbCase):
                self.addPion(DameBlanche(pion.id,pion.coordonnees_X,pion.coordonnees_Y))
                self.removePion(pion)