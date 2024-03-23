from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame
from DameBlanche import DameBlanche
from DameNoire import DameNoire
from Damier import Damier
from Partie import Partie
import constants as const
import math
from copy import deepcopy
from evaluation import pionNonDefendu,getDame

class AutoPlayer:
    def __init__(self,couleur:str,partie:Partie,levelDifficulte:str):
        self.couleur=couleur
        self.partie=partie
        self.levelDifficulte=levelDifficulte

    def getCouleurOppose(self):
        if self.couleur=="blanc":
            return "noir"
        elif self.couleur=="noir":
            return "blanc"
        else:
            return False

    def feuille(n):
        return n.checkWin()

    def evaluation(self,n,color):
        if n.checkWin():
            if(n.winner==self.couleur):
                return (10000,None)
            else:
                return (-10000,None)
        else:
            cpt=0
            for pion in n.listePion:
                if pion.couleur==color:
                    cpt=cpt+len(n.getDeplacement(pion))
                    cpt=cpt+(3*len(n.getCapture(pion)))
            cpt=cpt-3*pionNonDefendu(n,self.couleur)
            cpt=cpt+2*getDame(n,self.couleur)
            return (cpt,None)


    def estMax(self,color):
        return color==self.couleur

    def nombreFils(self,n,color):
        cpt=0
        for pion in n.listePion:
            if pion.couleur==color:
                cpt=cpt+len(n.getCapture(pion))
        if(cpt==0):
            for pion in n.listePion:
                if pion.couleur==color:
                    cpt=cpt+len(n.getDeplacement(pion))
        return cpt

    def getListeMouvement(self,n,color):
        listeMouvement=[]
        capt=False
        for pion in n.listePion:
            if pion.couleur==color:
                for couple in n.getCapture(pion):
                    listeMouvement.append((couple[1],couple[2],pion.id))
                    capt=True
        if(not capt):
            for pion in n.listePion:
                if pion.couleur==color:
                    for couple in n.getDeplacement(pion):
                        listeMouvement.append((couple[0],couple[1],pion.id))
        return listeMouvement

    def min(self,m,alphabeta):
        if m<alphabeta:
            return m
        else:
            return alphabeta

    def max(self,m,alphabeta):
        if m>alphabeta:
            return m
        else:
            return alphabeta

    def alphabeta(self,n,color,prof,alpha,beta):
        if self.feuille(n) or prof==0:
            return self.evaluation(n,color)
        else:
            if self.estMax(color):
                m=-math.inf
                nbr=self.nombreFils(n,color)
                listeTampon=self.getListeMouvement(n,color)
                cpt=0
                f=None
                while(m<beta and not nbr==cpt):
                    f=listeTampon[cpt]
                    partie=deepcopy(n)
                    partie.effectuerDeplacement(f[0],f[1],partie.getPion(f[2]))
                    res=self.alphabeta(partie,self.getCouleurOppose(),prof-1,alpha,beta)
                    m=max(m,res[0])
                    alpha=max(alpha,m)
                    cpt=cpt+1
            else:
                m=math.inf
                nbr=self.nombreFils(n,color)
                listeTampon=self.getListeMouvement(n,color)
                cpt=0
                f=None
                while(m>alpha and not nbr==cpt):
                    f=listeTampon[cpt]
                    partie=deepcopy(n)
                    partie.effectuerDeplacement(f[0],f[1],partie.getPion(f[2]))
                    res=self.alphabeta(partie,self.couleur,prof-1,alpha,beta)
                    m=min(m,res[0])
                    beta=min(beta,m)
                    cpt=cpt+1
            return (m,f)
    
        
    def MTD(self,n,color,prof,init_g):
        g=init_g
        haut=math.inf
        bas=-math.inf
        while(haut>bas):
            if g==bas:
                beta=g+1
            else:
                beta=g
            res=self.alphabeta(n,color,prof,beta-1,beta)
            g=res[0]
            if g<beta:
                haut=g
            else:
                bas=g
        return res

    def getCoup(self):
        if(self.levelDifficulte=="agressif"):
            return self.MTD(self.partie,self.couleur,5,0)
        elif(self.levelDifficulte=="defensif"):
            return self.MTD(self.partie,self.couleur,5,0)