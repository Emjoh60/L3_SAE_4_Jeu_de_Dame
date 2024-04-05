from Partie import Partie
from AutoPlayer import AutoPlayer
from pickle import load, dump
import os
import csv 

# Classe Menu
class Menu:
    # Constructeur de la classe
    def __init__(self,levelDifficulte:int,levelSon:int,couleurJoueur:str):
        self.levelDifficulte = levelDifficulte
        self.levelSon = levelSon
        self.couleurJoueur=couleurJoueur
        # Initialisation de l'IA
        self.ia=AutoPlayer(self.getCouleurOppose(),None,self.levelDifficulte)
        self.listePartie=[]
        # Récupération des parties précédentes
        if(os.path.exists("Save/save.csv")):
            with open("Save/save.csv",'r') as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    self.listePartie.append((row[0],row[1],row[2]))
            file.close()

    # Récupération des paramètres d'une partie
    def getParametre(self,id:str):
        retour=()
        for partie in self.listePartie:
            if partie[0]==id:
                retour=(partie[1],partie[2])
        return retour

    # Récupération de la couleur oposé d'un joueur
    def getCouleurOppose(self):
        if self.couleurJoueur=="blanc":
            return "noir"
        elif self.couleurJoueur=="noir":
            return "blanc"
        else:
            return False

    # Création d'une nouvelle partie
    def creerNouvellePartie(self,idPartie:str,levelSon,couleurJoueur):
        self.partieActive=Partie(idPartie,"")
        self.levelSon = levelSon
        self.couleurJoueur=couleurJoueur
        self.listePartie.append((idPartie,couleurJoueur,self.levelDifficulte))
        self.ajouterSave(idPartie)
        # Mise à jours des paramètres de l'IA
        self.ia.couleur=self.getCouleurOppose()
        self.ia.levelDifficulte=self.levelDifficulte
        self.ia.partie=self.partieActive
        return True
    
    # Suppression d'une partie selon l'ID, dans la liste de partie et sur le disque
    def supprimerPartie(self,idPartie:str):
        if not self.partieActive or not self.partieActive.id==idPartie:
            self.removeSave(idPartie)
            self.listePartie=[]
            if(os.path.exists("Save/save.csv")):
                with open("Save/save.csv",'r') as file:
                    csvreader = csv.reader(file)
                    for row in csvreader:
                        self.listePartie.append((row[0],row[1],row[2]))
                file.close()
            if(os.path.exists("Save/"+idPartie+".save")):
                os.remove("Save/"+idPartie+".save")
            return True
        else:
            return False
    
    # Choix du niveau de difficulté
    def choisirDifficulte(self,niveau:int):
        self.levelDifficulte=niveau
        self.ia.levelDifficulte=self.levelDifficulte

    # Choix de la couleur
    def choisirCouleur(self,couleur:str):
        self.couleurJoueur=couleur
        self.ia.couleur=self.getCouleurOppose()
        
    # Choix du volume
    def changerVolume(self,niveau:int):
        self.levelSon=niveau
    
    # Ajout d'une sauvegarde dans le fichier de sauvegarde
    def ajouterSave(self,id:str):
        with open("Save/save.csv",'a+',newline='') as file:
           writer=csv.writer(file)
           writer.writerow([id,self.couleurJoueur,self.levelDifficulte])
        file.close()

    # Suppression d'une sauvegarde dans le fichier de sauvegarde
    def removeSave(self,id:str):
        updatedlist=[]
        with open("Save/save.csv","r",newline="") as file:
            reader=csv.reader(file)
            for row in reader:                     
                if row[0]!=id:
                    updatedlist.append(row)
        file.close()
        with open("Save/save.csv","w+",newline="") as file:
            Writer=csv.writer(file)
            Writer.writerows(updatedlist)
        file.close()

    # Vérification qu'une sauvegarde existe
    def checkSave(self,save:str):
        var=False
        for triplet in self.listePartie:
            if(save==triplet[0]):
                var=True
        return var

    # Sauvegarde / Sérialisation d'une partie
    def sauvegarderPartie(self):
        fSave = open("Save/"+self.partieActive.id+".save",'wb')
        if(fSave):
            dump(self.partieActive,fSave)
        fSave.close()
    
    # Chargement / Désérialisation d'une partie
    def chargerPartie(self,id:str):
        if(os.path.exists("Save/"+id+".save")):
            fSave = open("Save/"+id+".save",'rb')
            self.partieActive = load(fSave)
            if(not self.partieActive):
                return False
            param=self.getParametre(id)
            self.couleurJoueur=param[0]
            self.levelDifficulte=int(param[1])
            # Mise à jours des paramètres de l'IA
            self.ia.couleur=self.getCouleurOppose()
            self.ia.levelDifficulte=self.levelDifficulte
            self.ia.partie=self.partieActive
            return True
        return False

    # Quitter une partie Active
    def quitterPartie(self):
        self.partieActive=None
