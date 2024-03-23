# On définit init_g à la valeur de n
import sys
from alphabeta import alphabeta
from Partie import Partie
import math

def MTD(n,color,prof,init_g):
    g=init_g
    haut=math.inf
    bas=-math.inf
    while(haut>bas):
        if g==bas:
            beta=g+1
        else:
            beta=g
        res=alphabeta(n,color,prof,beta-1,beta)
        g=res[0]
        if g<beta:
            haut=g
        else:
            bas=g
    return res