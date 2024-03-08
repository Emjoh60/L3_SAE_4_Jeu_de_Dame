from Partie import Partie

partie = Partie("Test","Aucun")
partie.afficherListePion()
play=True
while play:
    name=input("Selectionnez un pion (Entrez \"Fin\" pour arrêter le test):\n")
    if partie.getPion(name):
        x=input("Coordonnées X :\n")
        y=input("Coordonnées Y :\n")
        partie.effectuerDeplacement(int(x),int(y),partie.getPion(name))
        partie.afficherListePion()
    elif name=="Fin":
        play=False
