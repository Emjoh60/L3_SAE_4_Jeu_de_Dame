from Partie import Partie
from AutoPlayer import AutoPlayer
from pickle import load, dump
from os import path
import csv 

class Menu:
    def __init__(self,levelDifficulte:int,levelSon:int,couleurJoueur:str):
        self.levelDifficulte = levelDifficulte
        self.levelSon = levelSon
        self.couleurJoueur=couleurJoueur
        self.ia=AutoPlayer(self.getCouleurOppose(self.couleurJoueur),None,self.levelDifficulte)
        self.listePartie=[]
        if(path.exists("Save/save.csv")):
            with open("Save/save.csv",'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    self.listePartie.append((row[0],row[1],row[2]))
            file.close()

    def getParametre(self,id:str):
        retour=()
        for partie in self.listePartie:
            if partie[0]==id:
                retour=(partie[1],partie[2])
        return retour

    def getCouleurOppose(self):
        if self.couleur=="blanc":
            return "noir"
        elif self.couleur=="noir":
            return "blanc"
        else:
            return False

    def creerNouvellePartie(self,idPartie:str,levelSon,couleurJoueur):
        self.partieActive=Partie(idPartie,"")
        self.levelSon = levelSon
        self.couleurJoueur=couleurJoueur
        self.listePartie.append(idPartie)
        self.ajouterSave(idPartie)
        self.ia.couleur=self.getCouleurOppose(self.couleurJoueur)
        self.ia.levelDifficulte=self.levelDifficulte
        self.ia.partie=self.partieActive
        return True
    
    def supprimerPartie(self,idPartie:str):
        if not self.partieActive.id==idPartie:
            self.listePartie.remove(idPartie)
            self.removeSave(idPartie)
            return True
        else:
            return False
    
    def choisirDifficulte(self,niveau:int):
        self.levelDifficulte=niveau
        self.ia.levelDifficulte=self.levelDifficulte

    def choisirCouleur(self,couleur:str):
        self.couleurJoueur=couleur
        self.ia.couleur=self.getCouleurOppose(self.couleurJoueur)

    def afficherRegles(self):
        # Lecture des règles écrites dans un fichier
        print("En cours d'écriture")
        
    def changerVolume(self,niveau:int):
        self.levelSon=niveau
    
    def ajouterSave(self,id:str):
        with open("Save/save.csv",'a+',newline=' ') as file:
           writer=writer(file)
           writer.writerow([id,self.couleurJoueur,self.levelDifficulte])
        file.close()

    def removeSave(self,id:str):
        updatedlist=[]
        with open("Save/save.csv","r",newline="") as file:
            reader=csv.reader(file)
            for row in reader:                     
                if row[0]!=id:
                    updatedlist.append(row)
        file.close()
        print(updatedlist)
        with open("Save/save.csv","w+",newline="") as file:
            Writer=csv.writer(file)
            Writer.writerows(updatedlist)
        file.close()

    def sauvegarderPartie(self):
        fSave = open("Save/"+self.partieActive.id+".save",'wb')
        if(fSave):
            reseau = dump(reseau,fSave)
        fSave.close()
        
    def chargerPartie(self,id:str):
        if(path.exists("Save/"+id+".save")):
            fSave = open("Save/"+id+".save",'rb')
            self.partieActive = load(fSave)
            param=self.getParametre(id)
            self.couleurJoueur=param[0]
            self.levelDifficulte=param[1]
            self.ia.couleur=self.getCouleurOppose(self.couleurJoueur)
            self.ia.levelDifficulte=self.levelDifficulte
            self.ia.partie=self.partieActive

    def quitterPartie(self):
        # Demande de sauvegarde
        self.partieActive=None
