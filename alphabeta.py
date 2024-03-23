# La profondeur est initialisée à 0 et elle sera incrémentée, ceci nous permettra de savoir en fonction de si elle est paire ou impaire s'il s'agit d'un noeud MAX ou MIN
# Alpha est la valeur minimal initialisée et beta la valeur maximale
import sys
import math
from Partie import Partie
import constants
from copy import deepcopy
from evaluation import pionNonDefendu,getDame

COULEURMAX = "noir"
COULEURMIN = "blanc"

def feuille(n):
    return n.checkWin()

def evaluation(n,color):
    if n.checkWin():
        if(n.winner==COULEURMAX):
            return (10000,None)
        else:
            return (-10000,None)
    else:
        cpt=0
        for pion in n.listePion:
            if pion.couleur==color:
                cpt=cpt+len(n.getDeplacement(pion))
                cpt=cpt+(3*len(n.getCapture(pion)))
        cpt=cpt-3*pionNonDefendu(n,COULEURMAX)
        cpt=cpt+2*getDame(n,COULEURMAX)
        return (cpt,None)


def estMax(color):
    return color==COULEURMAX

def nombreFils(n,color):
    cpt=0
    for pion in n.listePion:
        if pion.couleur==color:
            cpt=cpt+len(n.getCapture(pion))
    if(cpt==0):
        for pion in n.listePion:
            if pion.couleur==color:
                cpt=cpt+len(n.getDeplacement(pion))
    return cpt

def getListeMouvement(n,color):
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

def min(m,alphabeta):
    if m<alphabeta:
        return m
    else:
        return alphabeta

def max(m,alphabeta):
    if m>alphabeta:
        return m
    else:
        return alphabeta

def alphabeta(n,color,prof,alpha,beta):
    if feuille(n) or prof==0:
        return evaluation(n,color)
    else:
        if estMax(color):
            m=-math.inf
            nbr=nombreFils(n,color)
            listeTampon=getListeMouvement(n,color)
            cpt=0
            f=None
            while(m<beta and not nbr==cpt):
                f=listeTampon[cpt]
                partie=deepcopy(n)
                partie.effectuerDeplacement(f[0],f[1],partie.getPion(f[2]))
                res=alphabeta(partie,COULEURMIN,prof-1,alpha,beta)
                m=max(m,res[0])
                alpha=max(alpha,m)
                cpt=cpt+1
        else:
            m=math.inf
            nbr=nombreFils(n,color)
            listeTampon=getListeMouvement(n,color)
            cpt=0
            f=None
            while(m>alpha and not nbr==cpt):
                f=listeTampon[cpt]
                partie=deepcopy(n)
                partie.effectuerDeplacement(f[0],f[1],partie.getPion(f[2]))
                res=alphabeta(partie,COULEURMAX,prof-1,alpha,beta)
                m=min(m,res[0])
                beta=min(beta,m)
                cpt=cpt+1
        return (m,f)

    
