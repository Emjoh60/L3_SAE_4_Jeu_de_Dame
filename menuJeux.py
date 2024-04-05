import pygame
import webbrowser
import constants
import sys
import os
import csv 
from Menu import Menu
from pionBlanc import pionBlanc
from pionNoir import pionNoir
from Dame import Dame
from DameBlanche import DameBlanche
from DameNoire import DameNoire

# Variables globales
global screen
global menu

# Classe représentant les boutons cliquables
class Button:
    def __init__(self, x, y, image, imageCover):
        self.image = image
        self.imageCover = imageCover
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.motion = False
        
    def redraw(self):
        global screen
        if not self.motion :
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else :
            screen.blit(self.imageCover, (self.rect.x, self.rect.y))

# Classe représentant les panneaux contenant des composants  
class Pannel:
    def __init__(self, x, y, image, long, larg):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (long, larg))
        self.long = long
        self.larg = larg
        self.rect = pygame.Rect(x,y,long,larg)
        self.rect.topleft = (x, y)
        
    def redraw(self):
        global screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

# Classe représentant les cases du damier
class Case:
    def __init__(self, id:str, x, y, color:str, coordonneeX, coordonneeY, tailleCase):
        self.id = id
        self.x = x
        self.y = y 
        self.color = color
        self.coordonneeX = coordonneeX
        self.coordonneeY = coordonneeY
        self.tailleCase = tailleCase
        self.rect = pygame.Rect(x,y,tailleCase,tailleCase)
        self.rect.topleft = (x, y)
        self.pionN = False
        self.dameN = False
        self.pionB = False
        self.dameB = False
        # Une case blanche ne contient pas de pions dessus
        if color == "blanc":
            self.caseNormal = pygame.transform.scale(pygame.image.load('ressources/caseB.png').convert_alpha(), (self.tailleCase, self.tailleCase))
        # Une case noire peut contenir des pions
        elif color == "noir":
            self.caseNormal = pygame.transform.scale(pygame.image.load('ressources/caseN.png').convert_alpha(), (self.tailleCase, self.tailleCase))
            self.casePionNoir = pygame.transform.scale(pygame.image.load('ressources/casePN.png').convert_alpha(), (self.tailleCase, self.tailleCase))
            self.caseDameNoire = pygame.transform.scale(pygame.image.load('ressources/dameNcaseN.png').convert_alpha(), (self.tailleCase, self.tailleCase))
            self.casePionBlanc = pygame.transform.scale(pygame.image.load('ressources/casePB.png').convert_alpha(), (self.tailleCase, self.tailleCase))
            self.caseDameBlanche = pygame.transform.scale(pygame.image.load('ressources/dameBcaseN.png').convert_alpha(), (self.tailleCase, self.tailleCase))
            
    def redraw(self):
        global screen
        if self.pionN :
            screen.blit(self.casePionNoir, (self.rect.x, self.rect.y))
        elif self.pionB :
            screen.blit(self.casePionBlanc, (self.rect.x, self.rect.y))
        elif self.dameB :
            screen.blit(self.caseDameBlanche, (self.rect.x, self.rect.y))
        elif self.dameN :
            screen.blit(self.caseDameNoire, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.caseNormal, (self.rect.x, self.rect.y))

# FONCTIONS D'INTERFACE GRAPHIQUE #

# Fonction permettant d'afficher les règles du jeu
def reglesJeu():
    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()

    # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    fondImg = pygame.image.load('ressources/fondRules.png').convert_alpha()

    listButton=[]

    # Création de boutton
    exitButton = Button(screen.get_width()-exitImg.get_width(),10, exitImg,exitImgClicked)
    fondButton = Button(screen.get_width()/3,screen.get_height()/5, fondImg,fondImg)

    listButton.append(exitButton)
    listButton.append(fondButton)
    

    # Affichage de la fenêtre
    running = True
    while running:
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        pygame.display.flip()
            
        # Boucle pour défénir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT: 
                running = False
            # Gestion des actions de l'utilisateur
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(exitButton.rect.collidepoint(event.pos)):
                    running=False
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                        bouton.motion = True
                    elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                        bouton.motion = False

# Fonction permettant de modifier les options au cours d'une partie       
def fenetreOption():
    
    global menu

    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()

    # Télécharger les boutons d'images
    fenPopImg = pygame.image.load('ressources/popupWindowBtnopt.png').convert_alpha()  
    agressBImg = pygame.image.load('ressources/AgressBtnPopup.png').convert_alpha()    
    agressBCImg = pygame.image.load('ressources/AgressBtnPopupClicked.png').convert_alpha()  
    defenssBImg = pygame.image.load('ressources/DefenssBtnPopup.png').convert_alpha()    
    defenssBCImg = pygame.image.load('ressources/DefenssBtnPopupClicked.png').convert_alpha()    
    volumeBImg = pygame.image.load('ressources/sonBtn.png').convert_alpha()   
    volumeBCImg = pygame.image.load('ressources/sonBtnClicked.png').convert_alpha() 
    croixImg = pygame.image.load('ressources/croix.png').convert_alpha()    
    croixCImg = pygame.image.load('ressources/croixClicked.png').convert_alpha()
    okImg = pygame.image.load('ressources/okBtn.png').convert_alpha()       
    okCImg = pygame.image.load('ressources/okBtnClicked.png').convert_alpha() 
    rulesImg = pygame.image.load('ressources/bookRules.png').convert_alpha()      

    listButton=[]
    
    width=screen.get_width()/4
    height=screen.get_height()/4

    # Création de boutton
    fenPopOptButton = Button(width,height, fenPopImg,fenPopImg)
    agressButton = Button(width/0.93,height/0.75, agressBImg,agressBCImg)
    defenssButton = Button(width/0.93,height/0.55, defenssBImg,defenssBCImg)
    volumeButton = Button(width+fenPopOptButton.rect.width/1.5,height/0.6, volumeBImg,volumeBCImg)
    croixButton = Button(width+fenPopOptButton.rect.width/1.1,height/1.1, croixImg,croixCImg)
    okButton = Button(width+fenPopOptButton.rect.width/2.55,height/0.48, okImg,okCImg)
    rulesButton = Button(width+fenPopOptButton.rect.width/1.5,height/0.85, rulesImg,rulesImg)

    listButton.append(fenPopOptButton)
    listButton.append(agressButton)
    listButton.append(defenssButton)
    listButton.append(volumeButton)
    listButton.append(croixButton)
    listButton.append(okButton)
    listButton.append(rulesButton)

    # Affichage de la fenêtre
    running = True
    son=True
    while running:
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        pygame.display.flip()
        difficulte=menu.levelDifficulte
        # Boucle pour défénir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT: 
                running = False
            # Gestion des actions de l'utilisateur
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(croixButton.rect.collidepoint(event.pos)):
                    running=False
                elif(rulesButton.rect.collidepoint(event.pos)):
                    reglesJeu()
                elif(okButton.rect.collidepoint(event.pos)):
                    menu.choisirDifficulte(difficulte)
                    running=False
                elif(defenssButton.rect.collidepoint(event.pos)):
                    difficulte=2
                elif(agressButton.rect.collidepoint(event.pos)):
                    difficulte=1
                elif(volumeButton.rect.collidepoint(event.pos)):
                    if son:
                        son=False
                        pygame.mixer.music.pause()
                    else:
                        son=True
                        pygame.mixer.music.unpause()
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                        bouton.motion = True
                    elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                        bouton.motion = False

# Fonction permettant de demander la sauvegade d'une partie            
def fenetre():
    
    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()

    # Télécharger les boutons d'images
    fenPopUpImg = pygame.image.load('ressources/popupWindowB.png').convert_alpha()  
    croixImg = pygame.image.load('ressources/croix.png').convert_alpha()  
    croixCImg = pygame.image.load('ressources/croixClicked.png').convert_alpha()
    yesBtnImg = pygame.image.load('ressources/yesBtn.png').convert_alpha() 
    yesBtnCImg = pygame.image.load('ressources/yesBtnClicked.png').convert_alpha()  
    noBtnImg = pygame.image.load('ressources/noBtn.png').convert_alpha()  
    noBtnCImg = pygame.image.load('ressources/noBtnClicked.png').convert_alpha()    

    listButton=[]
    
    width=screen.get_width()/4
    height=screen.get_height()/4

    # Création de boutton
    fenPopMenuButton = Button(width,height, fenPopUpImg,fenPopUpImg)
    croixButton = Button(width+fenPopMenuButton.rect.width/1.1,height/1.1, croixImg,croixCImg)
    yesButton = Button(width+fenPopMenuButton.rect.width/3.5,height+fenPopMenuButton.rect.height/1.4, yesBtnImg,yesBtnCImg)
    noButton = Button(width+fenPopMenuButton.rect.width/1.96,height+fenPopMenuButton.rect.height/1.4, noBtnImg,noBtnCImg)

    listButton.append(fenPopMenuButton)
    listButton.append(croixButton)
    listButton.append(yesButton)
    listButton.append(noButton)
    

    # Affichage de la fenêtre
    running = True
    while running:
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        pygame.display.flip()
            
        # Boucle pour défénir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT: 
                running = False
            # Gestion des actions de l'utilisateur
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(croixButton.rect.collidepoint(event.pos)):
                    running=False
                    return 0
                if(noButton.rect.collidepoint(event.pos)):
                    running=False
                    return -1
                if(yesButton.rect.collidepoint(event.pos)):
                    running=False
                    return 1
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if(isinstance(bouton,Button)):
                        if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                            bouton.motion = True
                        elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                            bouton.motion = False

# Fonction de gestion d'une partie active            
def valider():
    global menu
    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()
    
   # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    caseNImg = pygame.image.load('ressources/caseN.png').convert_alpha()
    caseBImg = pygame.image.load('ressources/caseB.png').convert_alpha()
    cadreImg = pygame.image.load('ressources/bois.jpg').convert_alpha()
    menuImg = pygame.image.load('ressources/OptionMPartie.png').convert_alpha()
    chargeImg = pygame.image.load('ressources/chargerBtn.png').convert_alpha()
    optImg = pygame.image.load('ressources/optionBtn.png').convert_alpha()
    mImg = pygame.image.load('ressources/menuBtn.png').convert_alpha()
    saveImg = pygame.image.load('ressources/sauvegarderBtn.png').convert_alpha()
    
    listButton=[]

    # Création de boutton
    exitButton = Button(screen.get_width()-exitImg.get_width(),10, exitImg,exitImgClicked)
    caseNButton = Button(screen.get_width()/6, screen.get_height()/5, caseNImg,caseNImg)
    caseBButton = Button(screen.get_width(),10, caseBImg,caseBImg)
    cadrePannel = Pannel(screen.get_width()/7,screen.get_height()/5,cadreImg, screen.get_height()/1.5, screen.get_height()/1.5)
    menuOptnButton = Button(screen.get_width()/1.6, screen.get_height()/5, menuImg,menuImg)
    mImgButton = Button(screen.get_width()/1.35, screen.get_height()/3, mImg,mImg)
    OptButton = Button(screen.get_width()/1.35, screen.get_height()/2.3, optImg,optImg)
    ChargeButton = Button(screen.get_width()/1.35, screen.get_height()/1.86, chargeImg,chargeImg)
    SaveButton = Button(screen.get_width()/1.35, screen.get_height()/1.6, saveImg,saveImg)

    listButton.append(exitButton)
    listButton.append(caseNButton)
    listButton.append(caseBButton)
    listButton.append(menuOptnButton)
    listButton.append(mImgButton)
    listButton.append(OptButton)
    listButton.append(ChargeButton)
    listButton.append(SaveButton)

    listCases=[]
    
    # Méthode de rafraichissement de la liste de case
    def refreshCase():
        global menu
        if(menu.couleurJoueur=="noir"):
            for case in listCases:
                pion=menu.partieActive.getPionPos(case.coordonneeX,case.coordonneeY)
                if(pion):
                    if(isinstance(pion,pionBlanc)):
                        case.pionB=False
                        case.pionN=True
                        case.dameB=False
                        case.dameN=False
                    elif(isinstance(pion,pionNoir)):
                        case.pionB=True
                        case.pionN=False
                        case.dameB=False
                        case.dameN=False
                    elif(isinstance(pion,DameBlanche)):
                        case.pionB=False
                        case.pionN=False
                        case.dameB=False
                        case.dameN=True
                    elif(isinstance(pion,DameNoire)):
                        case.pionB=False
                        case.pionN=False
                        case.dameB=True
                        case.dameN=False
                else:
                    case.pionB=False
                    case.pionN=False
                    case.dameB=False
                    case.dameN=False
        else:
            # Par soucis pratique, on ne change pas la nature des pions mais on change leur représentation
            for case in listCases:
                pion=menu.partieActive.getPionPos(case.coordonneeX,case.coordonneeY)
                if(pion):
                    if(isinstance(pion,pionBlanc)):
                        case.pionB=True
                        case.pionN=False
                        case.dameB=False
                        case.dameN=False
                    elif(isinstance(pion,pionNoir)):
                        case.pionB=False
                        case.pionN=True
                        case.dameB=False
                        case.dameN=False
                    elif(isinstance(pion,DameBlanche)):
                        case.pionB=False
                        case.pionN=False
                        case.dameB=True
                        case.dameN=False
                    elif(isinstance(pion,DameNoire)):
                        case.pionB=False
                        case.pionN=False
                        case.dameB=False
                        case.dameN=True
                else:
                    case.pionB=False
                    case.pionN=False
                    case.dameB=False
                    case.dameN=False

    posX=cadrePannel.x+cadrePannel.long*0.025
    posY=cadrePannel.y+cadrePannel.long*0.025
    long=cadrePannel.long-cadrePannel.long*0.1
    taille=long/(constants.PLATEAU)
    cpt=0
    color="blanc"

    # Génération du damier
    for y in range(constants.PLATEAU,0,-1):
        for x in range(1,constants.PLATEAU+1):
            id="CASE"+str(cpt) 
            case = Case(id, posX, posY, color, x, y, taille)
            listCases.append(case)
            if(color=="noir"):
                color="blanc"
            elif(color=="blanc"):
                color="noir"
            cpt=cpt+1
            posX=posX+taille
        if(color=="noir"):
            color="blanc"
        elif(color=="blanc"):
            color="noir"
        posY=posY+taille
        posX=cadrePannel.x+cadrePannel.long*0.025

    refreshCase()

    
    # Affichage de la fenêtre
    running = True
    select=None # Sélection d'un pion
    checkReplay=False # Indique si le joueur doit rejouer un coup ou non
    tourJoueur=True # Indique le tour
    # Tant que la partie n'a pas de vainqueur
    while running and not menu.partieActive.checkWin():
        # Dessin des composants
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        cadrePannel.redraw()
        for case in listCases:
            case.redraw()
        pygame.display.flip()
            
        # Boucle pour défénir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT:
                ret=fenetre()
                if(ret!=0):
                    if(ret==1):
                        menu.sauvegarderPartie()
                        menu.quitterPartie()
                    else:
                        x=menu.partieActive.id
                        if(os.path.exists("Save/"+x+".save")):
                            menu.quitterPartie()
                        else:
                            menu.quitterPartie()
                            menu.supprimerPartie(x)
                    running=False
            # Gestion des actions        
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Si le joueur veut quitter on lui demande de sauvegarder
                if(exitButton.rect.collidepoint(event.pos)):
                    ret=fenetre()
                    if(ret!=0):
                        if(ret==1):
                            menu.sauvegarderPartie()
                            menu.quitterPartie()
                        else:
                            x=menu.partieActive.id
                            if(os.path.exists("Save/"+x+".save")):
                                menu.quitterPartie()
                            else:
                                menu.quitterPartie()
                                menu.supprimerPartie(x)
                        running=False
                elif(mImgButton.rect.collidepoint(event.pos)):
                    # Si le joueur veut retourner au menu on lui demande de sauvegarder
                    ret=fenetre()
                    if(ret!=0):
                        if(ret==1):
                            menu.sauvegarderPartie()
                            menu.quitterPartie()
                        else:
                            x=menu.partieActive.id
                            if(os.path.exists("Save/"+x+".save")):
                                menu.quitterPartie()
                            else:
                                menu.quitterPartie()
                                menu.supprimerPartie(x)
                        running=False
                elif(SaveButton.rect.collidepoint(event.pos)):
                    # Gestion de la sauvegarde
                    ret=fenetre()
                    if(ret!=0):
                        if(ret==1):
                            menu.sauvegarderPartie()
                            menu.quitterPartie()
                        else:
                            x=menu.partieActive.id
                            if(os.path.exists("Save/"+x+".save")):
                                menu.quitterPartie()
                            else:
                                menu.quitterPartie()
                                menu.supprimerPartie(x)
                        running=False
                elif(OptButton.rect.collidepoint(event.pos)):
                    # Si le joueur clique sur le bouton d'option
                    fenetreOption()
                elif(ChargeButton.rect.collidepoint(event.pos)):
                    # Si le joueur souhaite charger une partie, on lui demande s'il veut sauvegarder
                    ret=fenetre()
                    if(ret!=0):
                        if(ret==1):
                            menu.sauvegarderPartie()
                            menu.quitterPartie()
                        else:
                            x=menu.partieActive.id
                            if(os.path.exists("Save/"+x+".save")):
                                menu.quitterPartie()
                            else:
                                menu.quitterPartie()
                                menu.supprimerPartie(x)
                    if chargement():
                        running=False
                        valider()
                elif (cadrePannel.rect.collidepoint(event.pos)):
                    # Si le joueur sélectionne une case
                    for case in listCases :
                        if case.rect.collidepoint(event.pos):
                            print(" Coordonnées x : "+str(case.coordonneeX)+" Coordonnées y : "+str(case.coordonneeY))
                            # Si le joueur sélectionne une case contenant un pion de sa couleur
                            if(not checkReplay and menu.partieActive.getPionPos(case.coordonneeX,case.coordonneeY) and isinstance(menu.partieActive.getPionPos(case.coordonneeX,case.coordonneeY),pionBlanc) or isinstance(menu.partieActive.getPionPos(case.coordonneeX,case.coordonneeY),DameBlanche)):
                                select=menu.partieActive.getPionPos(case.coordonneeX,case.coordonneeY)
                                if(menu.partieActive.checkAvaillable("blanc") and not select.id in menu.partieActive.checkAvaillable("blanc")):
                                    select=None
                            # Si le joueur a déjà sélectionné une case contenant un pion de sa couleur
                            elif(select):
                                capture=False
                                if(menu.partieActive.checkCapture(select)):
                                    capture=True
                                # On vérifie que le déplacement est cohérent
                                if(menu.partieActive.effectuerDeplacement(case.coordonneeX,case.coordonneeY,select)):
                                    # Tant que la capture est possible, on oblige le joueur à effectuer une capture
                                    if(capture and menu.partieActive.checkCapture(select)):
                                        checkReplay=True
                                    else:
                                        select=None
                                        checkReplay=False
                                        tourJoueur=False  
                                    refreshCase()

            # Gestion des évènements de passage sur un bouton
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                        bouton.motion = True
                    elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                        bouton.motion = False
            
            # Gestion du tour de l'IA
            if(not tourJoueur and not menu.partieActive.checkWin()):
                # Mise à jour de l'affichage
                print("IA is thinking...\n")
                screen.blit(background,(0, 0))
                for bouton in listButton:
                    bouton.redraw()
                cadrePannel.redraw()
                for case in listCases:
                    case.redraw()
                pygame.display.flip()
                # Calcule de l'IA
                x=menu.ia.MTD(menu.partieActive,"noir",4,0)
                y=x[1]
                capture=False
                if(menu.partieActive.checkCapture(menu.partieActive.getPion(y[2]))):
                    capture=True
                # Déplacement de l'IA
                menu.partieActive.effectuerDeplacement(y[0],y[1],menu.partieActive.getPion(y[2]))    
                refreshCase()
                # Tant que des captures sont effectuables
                while(capture and menu.partieActive.checkCapture(menu.partieActive.getPion(y[2]))):
                    # Mise à jour de l'affichage
                    screen.blit(background,(0, 0))
                    for bouton in listButton:
                        bouton.redraw()
                    cadrePannel.redraw()
                    for case in listCases:
                        case.redraw()
                    pygame.display.flip()
                    # Calcul de la position
                    x=menu.ia.MTD(menu.partieActive,"noir",4,0)
                    y=x[1]
                    # Effectuer le déplacement
                    menu.partieActive.effectuerDeplacement(y[0],y[1],menu.partieActive.getPion(y[2]))    
                    refreshCase()
                tourJoueur=True
                print("IA as finished\n")
    # Si un des joueurs a gagné, on quitte la partie
    if(menu.partieActive and menu.partieActive.checkWin()):
        print("Victoire des "+menu.partieActive.checkWin())
        x=menu.partieActive.id
        if(os.path.exists("Save/"+x+".save")):
            menu.quitterPartie()
        else:
            menu.quitterPartie()
            menu.supprimerPartie(x)

# Fonction permettant de choisir les options de création d'une nouvelle partie
def option():
    global menu
    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()
    
    # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    fondMenu = pygame.image.load('ressources/gameOption.png').convert_alpha()
    validerImg = pygame.image.load('ressources/valider.png').convert_alpha()
    refuserImg = pygame.image.load('ressources/refuser.png').convert_alpha()
    bAgressifImg = pygame.image.load('ressources/bAgressif.png').convert_alpha()
    bDefensifImg = pygame.image.load('ressources/bDefensif.png').convert_alpha()
    bAgressifCImg = pygame.image.load('ressources/bAgressidClicked.png').convert_alpha()
    bDefensifCImg = pygame.image.load('ressources/bDefensifClicked.png').convert_alpha()
    bPnoir = pygame.image.load('ressources/Pnoir.png').convert_alpha()
    bPblanc = pygame.image.load('ressources/Pblanc.png').convert_alpha()
    bPnoirC = pygame.image.load('ressources/PnoirClicked.png').convert_alpha()
    bPblancC = pygame.image.load('ressources/PblancClicked.png').convert_alpha()
    
    listButton=[]

    # Création de boutton
    exitButton = Button(screen.get_width()-exitImg.get_width(),10, exitImg,exitImgClicked)
    fondMenuButton = Button(screen.get_width()/3.5,screen.get_height()/7, fondMenu,fondMenu)
    validerImgButton = Button(screen.get_width()/2,screen.get_height()/1.4, validerImg,validerImg)
    refuserImgButton = Button(screen.get_width()/2.4,screen.get_height()/1.4, refuserImg,refuserImg)
    AgressifButton = Button(screen.get_width()/2.8,screen.get_height()/2.8, bAgressifImg,bAgressifCImg)
    DefensifButton = Button(screen.get_width()/2,screen.get_height()/2.8, bDefensifImg,bDefensifCImg)
    pNoirButton = Button(screen.get_width()/2.8,screen.get_height()/1.9, bPnoir,bPnoirC)
    pBlancButton = Button(screen.get_width()/2,screen.get_height()/1.9, bPblanc,bPblancC)

    listButton.append(exitButton)
    listButton.append(fondMenuButton)
    listButton.append(validerImgButton)
    listButton.append(refuserImgButton)
    listButton.append(AgressifButton)
    listButton.append(DefensifButton)
    listButton.append(pNoirButton)
    listButton.append(pBlancButton)
    
    # Affichage de la fenêtre
    running = True
    while running:
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        pygame.display.flip()
            
        # Boucle pour défénir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT: 
                running = False
            # Gestion des actions de l'utilisateur
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(exitButton.rect.collidepoint(event.pos)):
                    running=False
                elif(validerImgButton.rect.collidepoint(event.pos)):
                    if(pNoirButton.motion):
                        menu.couleurJoueur="noir"
                    else:
                        menu.couleurJoueur="blanc"
                    text=entrerNom()
                    while(not text or menu.checkSave(text)):
                        text=entrerNom()
                    menu.creerNouvellePartie(text,10,menu.couleurJoueur)
                    valider()
                    running=False
                elif(AgressifButton.rect.collidepoint(event.pos)):
                    AgressifButton.motion = True
                    DefensifButton.motion = False
                    menu.choisirDifficulte(1)
                elif(DefensifButton.rect.collidepoint(event.pos)):
                    DefensifButton.motion = True
                    AgressifButton.motion = False
                    menu.choisirDifficulte(2)
                elif(pNoirButton.rect.collidepoint(event.pos)):
                    pNoirButton.motion = True
                    pBlancButton.motion = False
                elif(pBlancButton.rect.collidepoint(event.pos)):
                    pNoirButton.motion = False
                    pBlancButton.motion = True
                elif(refuserImgButton.rect.collidepoint(event.pos)):
                    running=False

# Fonction pour demander à l'utilisateur un nom
def entrerNom():
    global menu
    global screen
    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Configuration de la police de caractères
    FONT_SIZE = 24
    font = pygame.freetype.Font(None, FONT_SIZE)

    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()

    # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    enterTxt = pygame.image.load('ressources/entrerTxt.png').convert_alpha()
    textArea = pygame.image.load('ressources/inputArea.png').convert_alpha()
    valider = pygame.image.load('ressources/validerTxt.png').convert_alpha()
    validerMotion = pygame.image.load('ressources/validerTxtMotion.png').convert_alpha()
    
    listButton=[]

    # Création de boutton
    exitButton = Button(screen.get_width()-exitImg.get_width(),10, exitImg,exitImgClicked)
    enterTxt = Pannel(screen.get_width()/3,screen.get_height()/5, enterTxt,screen.get_width()/3,screen.get_height()/5)
    textArea = Pannel(screen.get_width()/3,screen.get_height()/2, textArea,screen.get_width()/3,screen.get_height()/5)
    validerBtn = Button(screen.get_width()-valider.get_width(),screen.get_height()-valider.get_height()*1.1, valider,validerMotion)

    listButton.append(exitButton)
    listButton.append(validerBtn)
    listButton.append(textArea)
    listButton.append(enterTxt)

    text = ''

    # Boucle principale
    running = True
    while running:
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        # Afficher la barre de texte
        font.render_to(screen, (textArea.x + textArea.long/5, textArea.y + textArea.larg/5), text, WHITE)
        # Mettre à jour l'affichage
        pygame.display.flip()
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Appuyer sur Entrée pour effacer le texte
                    text = ''  # Effacer le texte de la barre
                elif event.key == pygame.K_BACKSPACE:  # Appuyer sur Retour arrière pour effacer un caractère
                    text = text[:-1]
                else:
                    text += event.unicode  # Ajouter le caractère saisi à la barre de texte
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if(exitButton.rect.collidepoint(event.pos)):
                    running=False
                elif(validerBtn.rect.collidepoint(event.pos)):
                    running=False
            elif event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if(isinstance(bouton,Button)):
                        if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                            bouton.motion = True
                        elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                            bouton.motion = False
    return text

# Fonction permettant de charger une partie
def chargement():
    global menu
    global screen
    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Configuration de la police de caractères
    FONT_SIZE = 35
    font = pygame.freetype.Font(None, FONT_SIZE)

    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()

    # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    fondCPImg = pygame.image.load('ressources/fondCP.png').convert_alpha()
    flecheGImg = pygame.image.load('ressources/flecheG.png').convert_alpha()
    flecheDImg = pygame.image.load('ressources/flecheD.png').convert_alpha()

    listButton=[]

    # Création de boutton
    exitButton = Button(screen.get_width()-exitImg.get_width(),10, exitImg,exitImgClicked)
    fondCPButton = Pannel(screen.get_width()/5,screen.get_height()/5,fondCPImg,screen.get_width()/2,screen.get_height()/2)
    flecheGButton = Button(screen.get_width()/3.5,screen.get_height()/1.2, flecheGImg,flecheGImg)
    flecheDButton = Button(screen.get_width()/2,screen.get_height()/1.2, flecheDImg,flecheDImg)

    listButton.append(exitButton)
    listButton.append(fondCPButton)
    listButton.append(flecheGButton)
    listButton.append(flecheDButton)
    

    # Affichage de la fenêtre
    running = True
    tailleListe=len(menu.listePartie)
    currentPartie=0
    retour=False
    while running and tailleListe>0:
        triple=menu.listePartie[currentPartie]
        if(triple[2]=="1"):
            diff="Agressive"
        else:
            diff="Défensive"
        text1="Partie Id: "+triple[0]
        text2="Couleur du joueur : "+triple[1]
        text3="Difficulté : "+diff
        
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        # Afficher la barre de texte
        font.render_to(screen, (fondCPButton.x + fondCPButton.long/5, fondCPButton.y + fondCPButton.larg/5),text1, BLACK)
        font.render_to(screen, (fondCPButton.x + fondCPButton.long/5, fondCPButton.y + fondCPButton.larg/4),text2, BLACK)
        font.render_to(screen, (fondCPButton.x + fondCPButton.long/5, fondCPButton.y + fondCPButton.larg/3),text3, BLACK)
        pygame.display.flip()
            
        # Boucle pour définir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(exitButton.rect.collidepoint(event.pos)):
                    running=False
                elif(fondCPButton.rect.collidepoint(event.pos)):
                    running=False
                    if menu.chargerPartie(triple[0]):
                        retour=True
                    else:
                        print("Erreur lors du chargement")
                elif(flecheGButton.rect.collidepoint(event.pos)):
                    if currentPartie==0:
                        currentPartie=tailleListe-1
                    else:
                        currentPartie=currentPartie-1
                elif(flecheDButton.rect.collidepoint(event.pos)):
                    if currentPartie==tailleListe-1:
                        currentPartie=0
                    else:
                        currentPartie=currentPartie+1
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if(isinstance(bouton,Button)):
                        if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                            bouton.motion = True
                        elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                            bouton.motion = False
    return retour
    
# Fonction d'affichage du menu
def start(optionMenu:Menu):
    # Initialisation de pygame
    pygame.init()
    pygame.mixer.music.load('ressources/music.mp3')
    pygame.mixer.music.play(-1)
    global menu
    menu=optionMenu
    # Création d'une fenêtre
    pygame.display.set_caption("Jeu de Dame")
    global screen
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()

    # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    logofond = pygame.image.load('ressources/fondRectM.png').convert_alpha()
    nPartieBtn = pygame.image.load('ressources/NPartieB.png').convert_alpha()
    nPartieBtnClicked = pygame.image.load('ressources/NPartieBClicked.png').convert_alpha()
    cPartieBtn = pygame.image.load('ressources/CPartieB.png').convert_alpha()
    cPartieBtnClicked = pygame.image.load('ressources/CPartieBClicked.png').convert_alpha()
    ligneImg = pygame.image.load('ressources/ligneC.png').convert_alpha()
    

    listButton=[]

    # Création de boutton
    exitButton = Button(screen.get_width()-exitImg.get_width(),10, exitImg,exitImgClicked)
    logofondButton = Button(screen.get_width()/3,screen.get_height()/5, logofond,logofond)
    nPartieButton = Button(screen.get_width()/2.45,screen.get_height()/2.9, nPartieBtn,nPartieBtnClicked)
    cPartieButton = Button(screen.get_width()/2.45,screen.get_height()/1.8, cPartieBtn,cPartieBtnClicked)
    ligneImgButton = Button(screen.get_width()/2.5,screen.get_height()/2.4, ligneImg,ligneImg)

    listButton.append(exitButton)
    listButton.append(logofondButton)
    listButton.append(nPartieButton)
    listButton.append(cPartieButton)
    listButton.append(ligneImgButton)
    

    # Affichage de la fenêtre
    running = True
    while running:
        screen.blit(background,(0, 0))
        for bouton in listButton:
            bouton.redraw()
        pygame.display.flip()
            
        # Boucle pour défénir une action faite par l'utilisateur
        for event in pygame.event.get(): 
            # Si personne fait une action on demande de quitter le jeu
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if(exitButton.rect.collidepoint(event.pos)):
                    running=False
                elif(nPartieButton.rect.collidepoint(event.pos)):
                    option()
                elif(cPartieButton.rect.collidepoint(event.pos)):
                    if chargement():
                        valider()
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                        bouton.motion = True
                    elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                        bouton.motion = False
    pygame.mixer.music.stop()
    pygame.quit()