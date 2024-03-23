from Pions import Pions
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame
from DameBlanche import DameBlanche
from DameNoire import DameNoire
from Damier import Damier
from Partie import Partie
import constants as const
from math import log

def pionNonDefendu(partie:Partie,couleur:str):
    cpt=0
    for pion in partie.listePion:
        if pion.couleur==couleur:
            if(isinstance(pion, pionNoir) or isinstance(pion, DameNoire)):
                if(pion.coordonnees_X==1 or pion.coordonnees_X==partie.damier.nbCase):
                    pass
                elif not(partie.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)or partie.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)):
                        cpt=cpt+1
            elif(isinstance(pion, pionBlanc) or isinstance(pion, DameBlanche)):
                if(pion.coordonnees_X==1 or pion.coordonnees_X==partie.damier.nbCase):
                    pass
                elif not(partie.getPionPos(pion.coordonnees_X+1,pion.coordonnees_Y+1)or partie.getPionPos(pion.coordonnees_X-1,pion.coordonnees_Y+1)):
                        cpt=cpt+1             
    return cpt

def getDame(partie:Partie,couleur:str):
    cpt=0
    for pion in partie.listePion:
        if pion.couleur==couleur:
            if(isinstance(pion, DameBlanche) or isinstance(pion, DameNoire)):
                cpt=cpt+1
    return cpt