import pygame
import webbrowser

# Fonction qui permet de savoir si un elt est cliquer
def checkClique(pos):
    global running
    if (startButton.rect.collidepoint(pos)):
        print("start")
    elif (exitButton.rect.collidepoint(pos)):
        running=False
    elif (githuButton.rect.collidepoint(pos)):
        webbrowser.open("https://github.com/Emjoh60/L3_SAE_4_Jeu_de_Dame")

def checkMotion(pos):
    if (startButton.rect.collidepoint(pos) and not startButton.motion):
        startButton.motion = True
    elif (not startButton.rect.collidepoint(pos) and startButton.motion):
        startButton.motion = False
    if (exitButton.rect.collidepoint(pos) and not exitButton.motion):
        exitButton.motion = True
    elif (not exitButton.rect.collidepoint(pos) and exitButton.motion):
        exitButton.motion = False
    if (githuButton.rect.collidepoint(pos) and not githuButton.motion):
        githuButton.motion = True
    elif (not githuButton.rect.collidepoint(pos) and githuButton.motion):
        githuButton.motion = False
        

# Initialisation de pygame
pygame.init()

# Création d'une fenêtre
pygame.display.set_caption("Jeu de Dame")
screen = pygame.display.set_mode((850, 478))

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

class Button1:
    def __init__(self, x, y, image, imageCover):
        self.image = image
        self.imageCover = imageCover
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.motion = False
        
    def redraw(self):
        if not self.motion :
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else :
            screen.blit(self.imageCover, (self.rect.x, self.rect.y))
        
class Button2:
    def __init__(self, x, y, image, imageCover):
        self.image = image
        self.imageCover = imageCover
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)
        self.motion = False
        
    def redraw(self):
        if not self.motion :
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else :
            screen.blit(self.imageCover, (self.rect.x, self.rect.y))
        
        
class Button3:
    def __init__(self, x, y, image, imageCover):
        self.image = image
        self.imageCover = imageCover
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)
        self.motion = False
        
    def redraw(self):
        if not self.motion :
            screen.blit(self.image, (self.rect.x, self.rect.y))
        else :
            screen.blit(self.imageCover, (self.rect.x, self.rect.y))
        
class Button4:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottomright = (x, y)
        
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
# Création de boutton
startButton = Button1(425, 239, startImg, startImgClicked)
exitButton = Button2(825, 10, exitImg, exitImgClicked)
githuButton = Button3(25, 468, logoGitHub, logoGitHubClicked)
npButton = Button4(825, 468, npIcone)



# Affichage de la fenêtre
running = True
while running:
    screen.blit(background, (0, 0))
    startButton.redraw()
    exitButton.redraw()
    githuButton.redraw()
    npButton.draw()
    pygame.display.flip()
        
    # Boucle pour défénir une action faite par l'utilisateur
    for event in pygame.event.get(): 
        # Si personne fait une action on demande de quitter le jeu
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            checkClique(event.pos)
        if event.type == pygame.MOUSEMOTION:
            checkMotion(event.pos)
pygame.quit()
        
        