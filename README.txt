SAE 4 - Concevoir une application informatique complète
Par KHALED Sara et THOMAS Johann
Musique : Chill beats Curated by PixabayAlbum 

I) Introduction :

Le produit présenté concerne le projet de conception d'un Jeu de Dame du sixième semestre de licence de l'UPJV. 
Ce produit a été réalisé par KHALED Sara et THOMAS Johann, il vise à concevoir une application informatique complète à partir de l'analyse jusqu'au développement.

II) Présentation :

Le jeu présenté consiste en une implémentation du jeux de dame, ainsi l'utilisateur peut jouer au Dame contre une IA codée selon l'algorithme MTD (Method Test Drive).
Ce jeu implémente donc les règles de bases du jeux de Dame, permet de sauvegarder et charger une partie et configurer les options d'une partie.
Le jeu dispose d'une partie pré-enregistrée nommée "Partie1".

III) Installation :

Le jeu est compatible sur Linux et Ubuntu.
Pour jouer à ce jeu, il est nécessaire de disposer de Python3 d'installé sur sa machine ainsi que de la librairie Pygame en 2.4.1 minimum et de la librairie numpy.
Afin d'installer et de lancer le jeu, il est nécessaire de disposer de tous les éléments fournis dans un même dossier selon l'arborescence du ZIP fournis.
Enfin, veuillez taper la commande suivante dans un terminal:
    -> python3 main.py

IV) Utilisation :

Le jeu dispose d'un lanceur d'accueil faisant références aux développeur et à l'organisme pour lequel travaille les développeurs.
Lorsque l'utilisateur clique sur start, il arrive sur un menu, à partir de là, il est possible soit de charger une partie précédente soit d'en créer une nouvelle.
Dans le cas où l'utilisateur charge une partie, il arrive sur le plateau de jeu et peut jouer.
Dans le cas où celui-ci créer une nouvelle partie, il arrive sur une fenêtre l'invitant à choisir une couleur et une difficultée.
Ainsi il a le choix entre une IA agressive et une IA défensive. L'IA agressive est plus forte que l'IA défensive
Une fois ce choix effectué, l'utilisateur doit entrer un nom de partie valide et non utilisé pour pouvoir sauvegarder sa partie (S'il le souhaite au cours de la partie).
Quoiqu'il en soit le joueur arrivera sur le damier et pourra soit retourner au menu, soit changer les options telles que le niveau de difficulté ou l'activation du son. Enfin il peut également consulter les règles du jeu.
Le joueur peut charger une autre partie ou sauvegarder la partie courrante sachant que toute action faisant quitter la partie actuelle fera intervenir une fenêtre proposant au joueur de sauvegarder sa partie.
Dans chaque page se trouve un bouton "exit" qui permet de revenir à la page précédente.