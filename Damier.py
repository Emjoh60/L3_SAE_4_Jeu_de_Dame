import numpy as np

class Damier:
    #constructeur d'un damier
    def __init__(self,id:str,nbCase:int):
        self.id = id
        self.nbCase = nbCase
        self.plateau=np.empty((self.nbCase,self.nbCase),dtype='U50')
        for x in range(self.nbCase):
            for y in range(self.nbCase):
                self.plateau[x-1,y-1]=" "
    
    def modifier(self,x:int,y:int,pion:str):
        self.plateau[x-1,y-1]=pion

    def afficher_matrice(self):
        for ligne in self.plateau:
            for element in ligne:
                print(f"+------+", end=" ")
            print()

            for element in ligne:
                print(f"|  {element.center(4)}  ", end="")
            print("|")

        # Afficher la dernière ligne des bordures inférieures
        for _ in self.plateau[0]:
            print("+------+", end=" ")
        print()