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
        self.partieActive
        if(path.exists("Save/save.csv")):
            with open("Save/save.csv",'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    self.listePartie.append(row[0])
            file.close()

    def creerNouvellePartie(self,idPartie:str):
        self.partieActive=Partie(idPartie,"")
        with open("Save/save.csv",'a+',newline=' ') as file:
           writer=writer(file)
           writer.writerow([idPartie])
        file.close()
        return True
    
    def choisirDifficulte(self,niveau:int):
        self.levelDifficulte=niveau

    def choisirCouleur(self,couleur:str):
        self.couleurJoueur=couleur

    def afficherRegles(self):
        # Lecture des règles écrites dans un fichier
        print("En cours d'écriture")
        
    def changerVolume(self,niveau:int):
        self.levelSon=niveau

    
