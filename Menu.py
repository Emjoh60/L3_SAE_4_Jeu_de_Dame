from Partie import Partie
from pickle import load, dump
from os import path
import csv 

class Menu:
    def __init__(self,levelDifficulte:int,levelSon:int,couleurJoueur:str):
        self.levelDifficulte = levelDifficulte
        self.levelSon = levelSon
        self.couleurJoueur=couleurJoueur
        self.listePartie=[]
        if(path.exists("Save/save.csv")):
            with open("Save/save.csv",'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    self.listePartie.append(row[0])
            file.close()

    def creerNouvellePartie(self,idPartie:str):
        self.partieActive=Partie(idPartie,"")
        self.listePartie.append(idPartie)
        self.ajouterSave(idPartie)
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

    def choisirCouleur(self,couleur:str):
        self.couleurJoueur=couleur

    def afficherRegles(self):
        # Lecture des règles écrites dans un fichier
        print("En cours d'écriture")
        
    def changerVolume(self,niveau:int):
        self.levelSon=niveau
    
    def ajouterSave(self,id:str):
        with open("Save/save.csv",'a+',newline=' ') as file:
           writer=writer(file)
           writer.writerow([id])
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

    def quitterPartie(self):
        # Demande de sauvegarde
        self.partieActive=None