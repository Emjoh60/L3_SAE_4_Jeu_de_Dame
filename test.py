from Partie import Partie

partie = Partie("Test","Aucun")
partie.afficherListePion()
x=partie.getPionPos(3,1)
if x:
    print("Pion en 1:1 -> "+x.id)
else :
    print("Pas de pion")
partie.effectuerDeplacement(7,9,partie.getPion("B11"))
partie.afficherListePion()
partie.effectuerDeplacement(10,6,partie.getPion("B11"))
partie.afficherListePion()
partie.effectuerDeplacement(8,8,partie.getPion("B11"))
partie.afficherListePion()