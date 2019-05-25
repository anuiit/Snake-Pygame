import pygame, random, time
from moviepy.editor import *
from colors import snakeGradient_color

size = width, height = 640, 320

pygame.init()

###############  Sounds  ####################

pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=512)
pygame.mixer.init()

_sounds = ['resources/game_menu_music.wav', 'resources/game_loop_music.wav', 'resources/unpause_sound.wav', 'resources/pause_sound.wav',
'resources/game_start.wav', 'resources/choice_gameover.wav', 'resources/death.wav', 'resources/eat_apple.wav', 'resources/sfx_sound_neutral8.wav']

pygame.mixer.music.set_volume(0.05)

unpause_snd = pygame.mixer.Sound(file =_sounds[2])
unpause_snd.set_volume(0.1)

pause_snd = pygame.mixer.Sound(file =_sounds[3])
pause_snd.set_volume(0.1)

gameStart_snd = pygame.mixer.Sound(file =_sounds[4])
gameStart_snd.set_volume(0.08)

deathChoice_snd = pygame.mixer.Sound(file =_sounds[5])
deathChoice_snd.set_volume(0.1)

gameOver_snd = pygame.mixer.Sound(file =_sounds[6])
gameOver_snd.set_volume(0.1)

eatApple_snd = pygame.mixer.Sound(file =_sounds[7])
eatApple_snd.set_volume(0.05)

menuSelect2_snd = pygame.mixer.Sound(file =_sounds[8])
menuSelect2_snd.set_volume(0.05)

pygame.mixer.music.load(_sounds[0])

############### Couleurs #####################

white = (255, 255, 255)
black = (0, 0, 0)
red = apple_color = (214, 69, 65)
green = (46, 204, 113)
orange = (230, 126, 34)
yellow = (244, 208, 63)
purple = (155, 89, 182)

apple_colors = [red, green, orange, yellow, purple]

############### Variables #####################

global block_size

block_size = 10

FPS = 20

font = pygame.font.SysFont(None, 30)

clock = pygame.time.Clock()  # Crée la variable clock avec la fonction de clock de pygame

# --------------------------------------------#

# On pose la taille et le titre de la fenêtre
gameDisplay = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

############### Fonctions #####################

# Fonction pour afficher un texte au centre de la fenêtre
def message_to_screen_center(text, font, size, color):
    font_object = pygame.font.SysFont(font, size)           # text : le texte affiché
    text_surface = font_object.render(text, True, color)    # font : la police utilisée
    text_rectangle = text_surface.get_rect()                # size : la taille de la police
    text_rectangle.center = (width/2), (height/2)           # color : couleur du texte
    
    gameDisplay.blit(text_surface, text_rectangle)          

# Même fonction qu'au dessus sauf qu'il y a la possibilité de choisir la position du texte
def message_to_screen(text, font, size, color, x, y):
    font_object = pygame.font.SysFont(font, size)
    text_surface = font_object.render(text, True, color)
    text_rectangle = text_surface.get_rect()
    text_rectangle.center = x, y

    gameDisplay.blit(text_surface, text_rectangle)

# Fonction pour afficher le serpent
def snake(block_size, snakeList):
    i = 0
    reverse = False

    for segment in snakeList: # "segment" prend une valeur entre 0 et le dernier élément de la liste
        
        if reverse == False:
            pygame.draw.rect(gameDisplay, snakeGradient_color[i], [segment[0], segment[1], block_size, block_size]) # ensuite on affiche le carré grâce à segment[0]
            i += 1
            print(i)
            if i == 15:
                reverse = True

        if reverse == True and i != 1:
            pygame.draw.rect(gameDisplay, snakeGradient_color[i], [segment[0], segment[1], block_size, block_size]) # ensuite on affiche le carré grâce à segment[0]
            i -= 1
            print(i)

            if i == 1:
                reverse = False

        # if square < 8 :
        #     snake_colors = (i, j, k)
        #     pygame.draw.rect(gameDisplay, snake_colors, [segment[0], segment[1], block_size, block_size]) # ensuite on affiche le carré grâce à segment[0]
        #     a += 12
        #     square += 1
        # elif square >= 8 and square < 18 :
        #     snake_colors = (0, b, c)
        #     pygame.draw.rect(gameDisplay, snake_colors, [segment[0], segment[1], block_size, block_size]) # ensuite on affiche le carré grâce à segment[0]
        #     b += 12                                                                                        # et segment[1] qui vont chercher les positions x et y du carré 
        #     c += 12
        #     square += 1
        # elif square >= 18 and square < 28 :
        #     snake_colors = (0, d, f)
        #     pygame.draw.rect(gameDisplay, snake_colors, [segment[0], segment[1], block_size, block_size]) # ensuite on affiche le carré grâce à segment[0]
        #     d += 12
        #     f += 12
        #     square += 1 
        # elif square == 28 :
        #     snake_colors = (0, g, h)
        #     pygame.draw.rect(gameDisplay, snake_colors, [segment[0], segment[1], block_size, block_size]) # ensuite on affiche le carré grâce à segment[0]
        #     g += 12
        #     h += 12 

# Fonction pour le début du jeu, il faut choisir entre 'Jouer' et 'Quitter'
def gameMenu():
    gameMenu = True

    pygame.mixer.music.play(-1)

    # On pose pos_arrow qui contient deux listes qui correspondent aux positions x et y de la flèche
    # i servira de choix entre la position 0 et 1
    i = 0
    pos_arrow = [[150, 215], [360,215]]

    while gameMenu == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if i != 0:
                        menuSelect2_snd.play()
                    # Si on appuie sur la flèche de gauche on choisit la liste 0
                    i = 0
                elif event.key == pygame.K_RIGHT:
                    if i != 1:
                        menuSelect2_snd.play()
                    # Si on appuie sur la flèche de gauche on choisit la liste 1
                    i = 1  
                # Ici on vérifie l'emplacement de i et si le joueur appuie sur espace
                # Dans ce cas-là soit on lance le joue soit on quitte le jeu
                elif event.key == pygame.K_SPACE and i == 0:
                    gameMenu = False
                    pygame.mixer.music.fadeout(0)
                    gameStart_snd.play()
                elif event.key == pygame.K_SPACE and i == 1:
                    pygame.quit()      
                         
        gameDisplay.fill(black)

        # On affiche les trois textes aux positions souhaitées
        message_to_screen("Jouer", 'orange_juice', 35, white, 210, 230)
        message_to_screen("Quitter", 'orange_juice', 35, white, 430, 228)
        message_to_screen("Snake", 'orange_juice', 60, green, 320, 140)
        message_to_screen("ESPACE pour continuer", 'none', 15, white, 320, 300)
        
        # Ici on affiche le symbole '>'
        text = font.render(">", 10, yellow)
        textpos = pos_arrow[i] # On choisit quelle liste parmi pos_arrow est utilisée grâce à i
        gameDisplay.blit(text, textpos) # On affiche la flèche aux positions de pos_arrow

        pygame.display.update()

# Cette fonction aura pour but de faire tourner le jeu en continu
def gameLoop():
    
    pygame.mixer.music.stop()
    pygame.mixer.music.load(_sounds[1])
    pygame.mixer.music.play(-1)

    gameExit = False
    gameOver = False

    direction_up = 1
    direction_down = 2
    direction_left = 3
    direction_right = 4
    direction = 0

    # On chosit la position de départ du serpent en fonction de la taille de la fenêtre
    pos_x = width/2
    pos_y = height/2

    # Vu plus loin
    pos_x_modif = 0
    pos_y_modif = 0

    # Choisit une variable dans la liste "apple_colors"
    apple_random = random.choice(apple_colors)
    appleThickness = 10

    # On génère aléatoirement la position x et y de la pomme
    spawn_x = round(random.randrange(block_size, width - block_size) / 10.0) * 10.0
    spawn_y = round(random.randrange(block_size, height - block_size) / 10.0) * 10.0

    # On crée une liste vide "snakeList" et on établit la longueur 
    # de base du serpent à 2 blocs
    snakeList = []
    snakeLength = 2

    # Variable pour gérer le score du joueur
    global playerScore
    playerScore = 0

    gameDisplay.fill(white)

    pygame.display.update()

    while gameExit == False:
        while gameOver == True:
            exitMenu()

        if gameExit == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    # On vérifie si le joueur appuie sur une touche, si oui alors le serpent change de position
                if event.type == pygame.KEYDOWN:  # Dès qu'une flèche est appuyée on ajoute le vecteur à la
                    # variable pos_x_modif ou pos_y_modif
                    if event.key == pygame.K_LEFT and direction != direction_right:
                        direction = direction_left
                        pos_x_modif = -block_size
                        pos_y_modif = 0     # on met ici = 0 pour que le carré ne se déplace pas dans deux directions           # à la fois, autrement dit en diagonale.
                    elif event.key == pygame.K_RIGHT and direction != direction_left:
                        direction = direction_right
                        pos_x_modif = block_size
                        pos_y_modif = 0
                    elif event.key == pygame.K_DOWN and direction != direction_up:
                        direction = direction_down
                        pos_y_modif = block_size
                        pos_x_modif = 0
                    elif event.key == pygame.K_UP and direction != direction_down:
                        direction = direction_up
                        pos_y_modif = -block_size
                        pos_x_modif = 0 
                        
                    elif event.key == pygame.K_UP and pygame.K_LEFT or event.key == pygame.K_UP and pygame.K_RIGHT:
                        direction = direction_up

                    elif event.key == pygame.K_DOWN and pygame.K_LEFT or event.key == pygame.K_DOWN and pygame.K_RIGHT:
                        direction = direction_down
                    # Si le joueur appuie sur espace, la fonction pauseMenu() se lance
                    elif event.key == pygame.K_SPACE:
                        pause_snd.play()
                        pygame.mixer.music.stop()

                        pauseMenu()

                        unpause_snd.play()
                        pygame.mixer.music.play(-1)

            # On vérifie si la tête du serpent touche une bordure
            if pos_x >= width - block_size * 3/4 or pos_x < 0 or pos_y >= height - block_size * 3/4 or pos_y < 0:
                # On vérifie la position du carré pour savoir si il touche une bordure
                gameOver_snd.play()
                gameOver = True
                pygame.mixer.music.stop()

            # On ajoute à la position du serpent la variable pos_x_modif qui est en fait la vitesse du serpent
            pos_x += pos_x_modif
            pos_y += pos_y_modif

            gameDisplay.fill(black)

            # On vérifie si la position de la tête du serpent est égale à la position de la pomme
            if pos_x == spawn_x and pos_y == spawn_y:
                eatApple_snd.play()

                playerScore += 1
                snakeLength += 1

                # On choisit une couleur aléatoirement parmi la liste "apple_colors"
                apple_random = random.choice(apple_colors)

                # On regénère la position de la pomme aléatoirement sur la fenêtre
                spawn_x = round(random.randrange(block_size, width - block_size) / 10.0) * 10.0
                spawn_y = round(random.randrange(block_size, height - block_size) / 10.0) * 10.0

            # On crée une liste vide qui contiendra 2 élements, la position x et y de la tête    
            snakeHead = []
            snakeHead.append(pos_x)
            snakeHead.append(pos_y)

            # On ajoute cette liste de deux éléments à la liste 'snakeList'
            snakeList.append(snakeHead)

            # On vérifie si la liste de segments du serpent n'est pas supérieure à la longueur du serpent
            if len(snakeList) > snakeLength:
                # Si oui alors on supprime le premier élément
                del snakeList[0]

            # On choisit 2 pour ne pas que le joueur meurt instantannément car il commence avec une 
            # longeur de 2    
            if snakeLength > 2:
                for eachSegment in snakeList[:-1]:  # Pour chaque segment dans 'snakeList' à partir du 2ème
                    if eachSegment == snakeHead:    # on vérifie si le segment a la même postion que la tête
                        gameOver = True 
                        gameOver_snd.play()

            # On dessine chaque segment du serpent grâce à snakeList et la fonction snake()
            snake(block_size, snakeList)

            # On dessine la pomme à sa nouvelle position et avec la nouvelle couleur
            pygame.draw.rect(gameDisplay, apple_random, [spawn_x, spawn_y, appleThickness, appleThickness])

            # On affiche le score du joueur
            message_to_screen("Score : " + str(playerScore), 'none', 25, white, block_size*4.5, block_size*1.5)
            pygame.display.update()

            clock.tick(FPS)  # On décide d'afficher 30 images/seconde

# Fonction pause du jeu
def pauseMenu():
    pause = True

    surf_aplha = pygame.Surface((1000,750))  # La taille de la surface
    surf_aplha.set_alpha(220)                # alpha level
    surf_aplha.fill(white)                   # Remplit entièrement la surface de blanc
    gameDisplay.blit(surf_aplha, (0,0))      # Affiche la surface au point (0,0)

    message_to_screen_center("PAUSE", 'none', 35, red) # On affiche un texte au centre

    pygame.display.update()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = False
                    
# Fonction de choix en fin de partie
def exitMenu():
    gameDisplay.fill(white)

    pygame.mixer.music.stop()

    message_to_screen("Game Over", 'none', 40, red, width/2, height/3)
    message_to_screen("Appuyez sur ESPACE pour recommencer ou ÉCHAP pour quitter", 'none', 25, black, width/2, height/1.5)
    message_to_screen_center("Score : " + str(playerScore), 'none', 35, black)

    pygame.display.update()

    exitMenu = True

    while exitMenu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exitMenu = False
                    gameExit = True
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    deathChoice_snd.play()
                    exitMenu = False
                    gameLoop()

# -------------------------------------------------#

gameMenu()
gameLoop()
quit()