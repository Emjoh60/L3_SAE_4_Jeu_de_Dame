from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame
from DameBlanche import DameBlanche
from DameNoire import DameNoire
from Damier import Damier
import constants as const
from math import log

# Classe Partie
class Partie:
    # Constructeur
    def __init__(self,id:str,winner:str):
        self.id = id
        self.winner = winner
        self.damier=Damier("1",const.PLATEAU)

        # Initialisation de la liste de pions
        self.listePion=[]
        cpt=1

        # Génération des pions blancs
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

        # Génération des pions noirs
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

    # Fonction d'affichage de la liste de pion
    def afficherListePion(self):
        for i in self.listePion :
            print("Pions :"+str(i.id)+" Type :"+str(i)+" Couleur : "+str(i.couleur)+" X : "+str(i.coordonnees_X)+" Y : "+str(i.coordonnees_Y))
        self.damier.afficher_matrice()

    # Fonction d'ajout d'un pion à la liste de pion
    def addPion(self,pion:Pions):
        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y,pion.id)
        self.listePion.append(pion)

    # Fonction de suppression d'un pion à la liste de pion
    def removePion(self,pion:Pions):
        if(pion.vivant):
            self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y," ")
        self.listePion.remove(pion)

    # Fonction de récupération d'un pion selon un id dans la liste de pion
    def getPion(self,id:str):
        for p in self.listePion:
            if(p.id==id):
                return p

    # Fonction de récupération d'un pion selon une position dans la liste de pion
    def getPionPos(self,posX:int, posY:int):
        if(posX>0 and posX<=self.damier.nbCase and posY>0 and posY<=self.damier.nbCase ):
            x=str(self.damier.plateau[posX-1,posY-1])
            if x:
                return self.getPion(x)
            else:
                return False
        else:
                return False

    # Fonction de récupération d'un pion selon un index dans la liste de pion
    def getPionIndex(self,index:int):
        return self.listePion[index]

    # Fonction de récupération d'un vainqueur sur une partie
    def checkWin(self):
        cptWhite=0
        cptBlack=0
        # S'il n'existe plus de pion d'une couleur alors cette couleur a perdue
        for pion in self.listePion:
            if pion.couleur=="blanc" and pion.vivant:
                cptWhite=cptWhite+1
            elif pion.couleur=="noir" and pion.vivant:
                cptBlack=cptBlack+1
        if cptWhite>0 and cptBlack>0:
            return False
        elif cptWhite>0 and cptBlack==0:
            self.winner="blanc"
            return "blanc"
        elif cptWhite==0 and cptBlack>0:
            self.winner="noir"
            return "noir"

    # Fonction de vérification si une capture est possible pour un pion
    def checkCapture(self,pion):
        if(isinstance(pion, pionNoir)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>2):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    return True
            if(pion.coordonnees_X>2 and pion.coordonnees_Y<self.damier.nbCase-1): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X>2 and pion.coordonnees_Y>2): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    return True
            return False
        elif(isinstance(pion, pionBlanc)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>2):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    return True
            if(pion.coordonnees_X>2 and pion.coordonnees_Y<self.damier.nbCase-1):     
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    return True
            if(pion.coordonnees_X>2 and pion.coordonnees_Y>2):    
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    return True
            return False
        elif(isinstance(pion, DameNoire)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y+1)):
                    return True
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x+1,y+1)) :
                    y=0
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y-1)):
                    return True
                elif (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire)) or (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and (self.getPionPos(x+1,y-1)) : 
                     y=0
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>1 and y<self.damier.nbCase:
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
            while x<self.damier.nbCase and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y+1)):
                    return True
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x+1,y+1)):
                     x=self.damier.nbCase
                x=x+1
                y=y+1
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            while x<self.damier.nbCase and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y-1)):
                    return True
                elif (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche)) or (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and (self.getPionPos(x+1,y-1)):
                     x=self.damier.nbCase
                x=x+1
                y=y-1
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            while x>1 and y<self.damier.nbCase:
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
        
    # Fonction de récupération des captures possible pour un pion
    def getCapture(self,pion):
        # On initialise une liste vide
        listePosition=[]
        # Pour les pions, on ne regarde que devant eux, en diagonal sur 2 cases
        if(isinstance(pion, pionNoir)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>2):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y-2))
            if(pion.coordonnees_X>2 and pion.coordonnees_Y<self.damier.nbCase-1): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X>2 and pion.coordonnees_Y>2): 
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y-2))
        elif(isinstance(pion, pionBlanc)):
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y<self.damier.nbCase-1):
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X<self.damier.nbCase-1 and pion.coordonnees_Y>2):    
                pAutour=self.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X+2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X+2,pion.coordonnees_Y-2))
            if(pion.coordonnees_X>2 and pion.coordonnees_Y<self.damier.nbCase-1):     
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y+2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y+2))
            if(pion.coordonnees_X>2 and pion.coordonnees_Y>2):    
                pAutour=self.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y-1)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(pion.coordonnees_X-2,pion.coordonnees_Y-2)):
                    listePosition.append((pAutour,pion.coordonnees_X-2,pion.coordonnees_Y-2))
        # Pour les dames, on regarde sur les diagonales
        elif(isinstance(pion, DameNoire)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            while x<self.damier.nbCase and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y+1)):
                    listePosition.append((pAutour,x+1,y+1))
                    x=x+2
                    y=y+2
                    # On récupère toutes les positions derrière un pion pour une dame
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
            while x<self.damier.nbCase and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x+1,y-1)):
                    listePosition.append((pAutour,x+1,y-1))
                    x=x+2
                    y=y-2
                    # On récupère toutes les positions derrière un pion pour une dame
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
            while x>1 and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionBlanc) or isinstance(pAutour, DameBlanche) )and not(self.getPionPos(x-1,y+1)):
                    listePosition.append((pAutour,x-1,y+1))
                    x=x-2
                    y=y+2
                    # On récupère toutes les positions derrière un pion pour une dame
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
                    # On récupère toutes les positions derrière un pion pour une dame
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
            while x<self.damier.nbCase and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y+1)):
                    listePosition.append((pAutour,x+1,y+1))
                    x=x+2
                    y=y+2
                    # On récupère toutes les positions derrière un pion pour une dame
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
            while x<self.damier.nbCase and y>1:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x+1,y-1)):
                    listePosition.append((pAutour,x+1,y-1))
                    x=x+2
                    y=y-2
                    # On récupère toutes les positions derrière un pion pour une dame
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
            while x>1 and y<self.damier.nbCase:
                pAutour=self.getPionPos(x,y)
                if (isinstance(pAutour, pionNoir) or isinstance(pAutour, DameNoire) )and not(self.getPionPos(x-1,y+1)):
                    listePosition.append((pAutour,x-1,y+1))
                    x=x-2
                    y=y+2
                    # On récupère toutes les positions derrière un pion pour une dame
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
                    # On récupère toutes les positions derrière un pion pour une dame
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
    
    # Fonction de vérfication d'un déplacement
    def checkDeplacement(self,pion:Pions, X:int, Y:int):
        # Si un pion n'est pas sur les coordonnées
        if not(self.getPionPos(X,Y)):
            # On vérifie que les coordonnées sont cohérentes
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
    
    # Fonction de récupération des positions de déplacement
    def getDeplacement(self,pion:Pions):
        # Initialisation d'une liste
        listePosition=[]
        # Pour chaque pion, on récupère les coordonnées en diagonales, si aucun pion ne se trouve dessus
        if(isinstance(pion, pionNoir)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            if (not(self.getPionPos(x,y)) and x<=self.damier.nbCase and y>0):
                listePosition.append((x,y))
            x=pion.coordonnees_X-1
            if (not(self.getPionPos(x,y)) and x>0 and y>0):
                listePosition.append((x,y))
        elif(isinstance(pion, pionBlanc)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            if (not(self.getPionPos(x,y)) and x<=self.damier.nbCase and y<=self.damier.nbCase):
                listePosition.append((x,y))
            x=pion.coordonnees_X-1
            if (not(self.getPionPos(x,y)) and x>0 and y<=self.damier.nbCase):
                listePosition.append((x,y))
        # Pour chaque dame, on récupère les coordonnées en diagonales, si aucun pion ne bloque le passage        
        elif(isinstance(pion, DameNoire) or isinstance(pion, DameBlanche)):
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y+1
            valuable=True
            while x<=self.damier.nbCase and y<=self.damier.nbCase and valuable:
                if not(self.getPionPos(x,y)):
                    listePosition.append((x,y))
                    x=x+1
                    y=y+1
                else:
                    valuable=False
            x=pion.coordonnees_X+1
            y=pion.coordonnees_Y-1
            valuable=True
            while x<=self.damier.nbCase and y>=1 and valuable:
                if not(self.getPionPos(x,y)):
                    listePosition.append((x,y))
                    x=x+1
                    y=y-1
                else:
                    valuable=False
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y+1
            valuable=True
            while x>=1 and y<=self.damier.nbCase and valuable:
                if not(self.getPionPos(x,y)):
                    listePosition.append((x,y))
                    x=x-1
                    y=y+1
                else:
                    valuable=False
            x=pion.coordonnees_X-1
            y=pion.coordonnees_Y-1
            valuable=True
            while x>=1 and y>=1 and valuable:
                if not(self.getPionPos(x,y)):
                    listePosition.append((x,y))
                    x=x-1
                    y=y-1
                else:
                    valuable=False
        return listePosition

    # Fonction permettant d'effectuer un déplacement
    def effectuerDeplacement(self,x:int,y:int,pion:Pions):
        # Vérification des coordonnées et du statut du pion
        if(pion.vivant) and (x>0 and x<=self.damier.nbCase) and (y>0 and y<=self.damier.nbCase):
            # Si aucune capture n'est répertoriée
            if(not self.checkCapture(pion)):
                # Si les coordonnées sont correctes, on effectue les modifications nécessaires
                if(self.checkDeplacement(pion,x,y)):
                    self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y," ")
                    pion.se_deplacer(x,y)
                    tampon=pion.id
                    if self.checkDame(pion):
                        pion=self.getPion(tampon)
                    self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y,pion.id)
                    return True
                else:
                    return False
            # Sinon, on vérifie que les cordonnées correspondent à une capture
            else:
                val=False
                for i in self.getCapture(pion):
                    # Si les coordonnées correspondent, on effectue les modifications nécessaires
                    if x==i[1] and y==i[2]:
                        val=True
                        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y," ")
                        self.damier.modifier(i[0].coordonnees_X,i[0].coordonnees_Y," ")
                        pion.capturerPion(i[1],i[2],i[0])
                        self.removePion(i[0])
                        tampon=pion.id
                        if self.checkDame(pion):
                            pion=self.getPion(tampon)
                        self.damier.modifier(pion.coordonnees_X,pion.coordonnees_Y,pion.id)
                return val    
        else:
            return False

    # Fonction permettant de vérifier que les conditions de transformation en dame sont réunies
    def checkDame(self,pion:Pions):
        if(isinstance(pion, pionNoir)):
            # Si le pion a atteint la limite du damier
            if(pion.coordonnees_Y==1):
                self.addPion(DameNoire(pion.id,pion.coordonnees_X,pion.coordonnees_Y))
                self.removePion(pion)
                return True
            else:
                return False
        elif(isinstance(pion, pionBlanc)):
            # Si le pion a atteint la limite du damier
            if(pion.coordonnees_Y==self.damier.nbCase):
                self.addPion(DameBlanche(pion.id,pion.coordonnees_X,pion.coordonnees_Y))
                self.removePion(pion)
                return True
            else:
                return False
        else:
            return False
        
    # Fonction de récupération des pions dont le déplacement est possible pour une couleur
    def checkAvaillable(self,color):
        listeCapture=[]
        # Si des captures sont possibles, on ne récupère que les captures
        for pion in self.listePion:
            if(pion.couleur==color and self.checkCapture(pion)):
                listeCapture.append(pion.id)
        if listeCapture:
            return listeCapture
        # Sinon on récupère les autres pions
        else:
            for pion in self.listePion:
                if(pion.couleur==color):
                    listeCapture.append(pion.id)
