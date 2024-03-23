from Partie import Partie
from mtd import MTD

partie = Partie("Test","Aucun")
partie.afficherListePion()
play=True
while play:
    name=input("Selectionnez un pion (Entrez \"Fin\" pour arrêter le test):\n")
    if partie.getPion(name):
        listeDep=partie.getDeplacement(partie.getPion(name))
        listeCap=partie.getCapture(partie.getPion(name))
        if(listeCap):
            print("Capture possible : "+str(partie.getCapture(partie.getPion(name))))
            x=input("Coordonnées X :\n")
            y=input("Coordonnées Y :\n")
            partie.effectuerDeplacement(int(x),int(y),partie.getPion(name))
            partie.damier.afficher_matrice()
        elif(listeDep):
            print("Déplacement possible : "+str(partie.getDeplacement(partie.getPion(name))))
            x=input("Coordonnées X :\n")
            y=input("Coordonnées Y :\n")
            partie.effectuerDeplacement(int(x),int(y),partie.getPion(name))
            partie.damier.afficher_matrice()
        else:
            print("Pas de déplacement possible pour "+name)
    elif name=="Fin":
        play=False
    x=MTD(partie,"noir",5,0)
    y=x[1]
    print("Meilleur coup pour les noirs : "+str(y))
    partie.effectuerDeplacement(y[0],y[1],partie.getPion(y[2]))
    partie.damier.afficher_matrice()
    partie.afficherListePion()