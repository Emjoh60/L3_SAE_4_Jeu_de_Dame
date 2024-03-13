import pygame
import webbrowser
import constants

WINDOW_LONG=850
WINDOW_LARG=480

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

def checkMotion(pos,listBouton):
    for bouton in listBouton:
        if (bouton.rect.collidepoint(pos) and not bouton.motion):
            bouton.motion = True
        elif (not bouton.rect.collidepoint(pos) and bouton.motion):
            bouton.motion = False
        
def start():
    # Initialisation de pygame
    pygame.init()

    # Création d'une fenêtre
    pygame.display.set_caption("Jeu de Dame")
    screen = pygame.display.set_mode((WINDOW_LONG, WINDOW_LARG))

    # Charger une image
    background = pygame.image.load('ressources/bkgrd.jpg')
    background.convert()

    # Télécharger les boutons d'images
    startImg = pygame.image.load('ressources/start.png').convert_alpha()
    exitImg = pygame.image.load('ressources/exit.png').convert_alpha()
    logoGitHub = pygame.image.load('ressources/github.png').convert_alpha()
    npIcone = pygame.image.load('ressources/np.png').convert_alpha()
    startImgClicked = pygame.image.load('ressources/startClicked.png').convert_alpha()
    exitImgClicked = pygame.image.load('ressources/exitClicked.png').convert_alpha()
    logoGitHubClicked = pygame.image.load('ressources/githubClicked.png').convert_alpha()

    listButton=[]

    # Création de boutton
    startButton = Button(WINDOW_LONG/3,WINDOW_LARG/3,startImg,startImgClicked)
    exitButton = Button(WINDOW_LONG-exitImg.get_width(),10, exitImg,exitImgClicked)
    githuButton = Button(25,WINDOW_LARG-logoGitHub.get_height(),logoGitHub,logoGitHubClicked)
    npButton = Button(WINDOW_LONG-npIcone.get_width(),WINDOW_LARG-npIcone.get_height(),npIcone,npIcone)

    listButton.append(startButton)
    listButton.append(exitButton)
    listButton.append(githuButton)
    listButton.append(npButton)

    # Fonction qui permet de savoir si un elt est cliquer
    def checkClique(pos):
        global running
        if(startButton.rect.collidepoint(pos)):
            print("start")
        elif(exitButton.rect.collidepoint(pos)):
            running=False
        elif(githuButton.rect.collidepoint(pos)):
            webbrowser.open("https://github.com/Emjoh60/L3_SAE_4_Jeu_de_Dame")

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
                checkClique(listButton,event.pos)
            if event.type == pygame.MOUSEMOTION:
                checkMotion(listButton,event.pos)
    pygame.quit()