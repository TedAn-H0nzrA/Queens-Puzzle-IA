import pygame   
# Les variables constants du jeu

WIDTH, HEIGHT = 800, 600
SCALE = (WIDTH, HEIGHT)
TITRE = "Le Jeu des 8 Dames"

# Gestion Frame
FPS = 60
clock = pygame.time.Clock()
CLOCK = clock.tick(FPS)



# Color
GREY = (128, 128, 128)
WHITE = (255, 255, 255)