import pygame
import webbrowser
import constants

WINDOW_LONG=850
WINDOW_LARG=480

global screen

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

def option():
    # Charger une image
    background = pygame.image.load('ressources/fondM.jpg')
    background.convert()
    
    # Télécharger les boutons d'images
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    fondMenu = pygame.image.load('ressources/gameOption.png').convert_alpha()
    
    listButton=[]

    # Création de boutton
    exitButton = Button(WINDOW_LONG-exitImg.get_width(),10, exitImg,exitImgClicked)
    fondMenuButton = Button(WINDOW_LONG/3,WINDOW_LARG/8, fondMenu,fondMenu)

    listButton.append(exitButton)
    listButton.append(fondMenuButton)
    
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
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                        bouton.motion = True
                    elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                        bouton.motion = False

     
def start():
    # Initialisation de pygame
    pygame.init()

    # Création d'une fenêtre
    pygame.display.set_caption("Jeu de Dame")
    global screen
    screen = pygame.display.set_mode((WINDOW_LONG, WINDOW_LARG))

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
    exitButton = Button(WINDOW_LONG-exitImg.get_width(),10, exitImg,exitImgClicked)
    logofondButton = Button(WINDOW_LONG/3,WINDOW_LARG/7, logofond,logofond)
    nPartieButton = Button(WINDOW_LONG/2.45,WINDOW_LARG/3, nPartieBtn,nPartieBtnClicked)
    cPartieButton = Button(WINDOW_LONG/2.45,WINDOW_LARG/1.5, cPartieBtn,cPartieBtnClicked)
    ligneImgButton = Button(WINDOW_LONG/2.5,WINDOW_LARG/2, ligneImg,ligneImg)

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
            if event.type == pygame.MOUSEMOTION:
                for bouton in listButton:
                    if (bouton.rect.collidepoint(event.pos) and not bouton.motion):
                        bouton.motion = True
                    elif (not bouton.rect.collidepoint(event.pos) and bouton.motion):
                        bouton.motion = False
    pygame.quit()