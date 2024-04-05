from Partie import Partie
import math
from copy import deepcopy
from evaluation import pionNonDefendu,getDame

# Classe du joueur IA
class AutoPlayer:
    # Constructeur de l'IA
    def __init__(self,couleur:str,partie:Partie,levelDifficulte:str):
        self.couleur=couleur
        self.partie=partie
        self.levelDifficulte=levelDifficulte

    # Fonction permettant de récupérer la couleur oposée (utile pour affecter la couleur à l'adversaire)
    def getCouleurOppose(self):
        if self.couleur=="blanc":
            return "noir"
        elif self.couleur=="noir":
            return "blanc"
        else:
            return False

    # Fonction indiquant si on a atteint une feuille
    def feuille(self,n):
        return n.checkWin()

    # Fonction d'évaluation pour l'IA agressive
    def evaluationAgressive(self,n,color):
        # En cas de victoire
        if n.checkWin():
            if(n.winner==self.couleur):
                return (10000,None)
            else:
                return (-10000,None)
        # Sinon on prend en compte plusieurs éléments avec un score différent
        else:
            cpt=0
            for pion in n.listePion:
                if pion.couleur==color:
                    cpt=cpt+len(n.getDeplacement(pion))
                    cpt=cpt+(5*len(n.getCapture(pion)))
            cpt=cpt-5*pionNonDefendu(n,self.couleur)
            cpt=cpt+6*getDame(n,self.couleur)
            return (cpt,None)

    # Fonction d'évaluation pour l'IA défensive
    def evaluationDefensive(self,n,color):
        # En cas de victoire
        if n.checkWin():
            if(n.winner==self.couleur):
                return (10000,None)
            else:
                return (-10000,None)
        # Sinon on prend en compte plusieurs éléments avec un score différent
        else:
            cpt=0
            for pion in n.listePion:
                if pion.couleur==color:
                    cpt=cpt+len(n.getDeplacement(pion))
                    cpt=cpt+(2*len(n.getCapture(pion)))
            cpt=cpt-3*pionNonDefendu(n,self.couleur)
            cpt=cpt+2*getDame(n,self.couleur)
            return (cpt,None)

    # Fonction permettant d'identifier noeud MAX/MIN
    def estMax(self,color):
        return color=="noir"

    # Fonction permettant de compter le nombre de fils (déplacement)
    def nombreFils(self,n,color):
        cpt=0
        # Si une capture est possible, on ne récupère que les captures
        for pion in n.listePion:
            if pion.couleur==color:
                cpt=cpt+len(n.getCapture(pion))
        # Si aucune capture est possible, on récupère les déplacements
        if(cpt==0):
            for pion in n.listePion:
                if pion.couleur==color:
                    cpt=cpt+len(n.getDeplacement(pion))
        return cpt

    # Fonction permettant de récupérer les mouvements
    def getListeMouvement(self,n,color):
        listeMouvement=[]
        capt=False
        # Si une capture est possible, on ne récupère que les captures
        for pion in n.listePion:
            if pion.couleur==color:
                for couple in n.getCapture(pion):
                    listeMouvement.append((couple[1],couple[2],pion.id))
                    capt=True
        # Si aucune capture est possible, on récupère les déplacements
        if(not capt):
            for pion in n.listePion:
                if pion.couleur==color:
                    for couple in n.getDeplacement(pion):
                        listeMouvement.append((couple[0],couple[1],pion.id))
        return listeMouvement

    # Fonction de comparaison du minimum
    def min(self,m,alphabeta):
        if m<alphabeta:
            return m
        else:
            return alphabeta

    # Fonction de comparaison du maximum
    def max(self,m,alphabeta):
        if m>alphabeta:
            return m
        else:
            return alphabeta

    # Algorithme récursif alphabeta
    def alphabeta(self,n,color,prof,alpha,beta):
        # Dans le cas d'une feuille, on évalue
        if self.feuille(n) or prof==0:
            if(self.levelDifficulte==1):
                return self.evaluationAgressive(n,color)
            elif(self.levelDifficulte==2):
                return self.evaluationDefensive(n,color)
        else:
            # Dans le cas d'un noeud max
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
            # Dans le cas d'un noeud min
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
    
    # Algorithme de la fonction MTD
    def MTD(self,n,color,prof,init_g):
        g=init_g
        haut=math.inf
        bas=-math.inf
        while(haut>bas):
            if g==bas:
                beta=g+1
            else:
                beta=g
            # On étudie l'arbre en plus grande profondeur selon la difficultée
            if(self.levelDifficulte==1):
                res=self.alphabeta(n,color,prof+2,beta-1,beta)
            else:
                res=self.alphabeta(n,color,prof,beta-1,beta)
            g=res[0]
            if g<beta:
                haut=g
            else:
                bas=g
        return res