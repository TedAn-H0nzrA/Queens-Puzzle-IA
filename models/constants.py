# models/constants.py
# Constantes utilisées dans le projet

# Dimensions de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_SQUARE = (240, 217, 181)  # Couleur des cases claires
DARK_SQUARE = (181, 136, 99)    # Couleur des cases foncées
HIGHLIGHT = (255, 255, 0, 128)  # Couleur de surbrillance (jaune transparent)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensions de l'échiquier
BOARD_SIZE = 8  # Taille de l'échiquier (8x8)
SQUARE_SIZE = 60  # Taille d'une case en pixels

# Position de l'échiquier
BOARD_X = (SCREEN_WIDTH - BOARD_SIZE * SQUARE_SIZE) // 2
BOARD_Y = (SCREEN_HEIGHT - BOARD_SIZE * SQUARE_SIZE) // 2

# Paramètres de simulation pour le recuit simulé
INITIAL_TEMPERATURE = 100.0
COOLING_RATE = 0.995
MIN_TEMPERATURE = 0.01

# Textes
FONT_SIZE = 20
TITLE_FONT_SIZE = 32
INFO_FONT_SIZE = 16

# Touches
KEY_ANNEALING = 97  # 'a'
KEY_BACKTRACKING = 98  # 'b'
KEY_RESET = 114  # 'r'
KEY_QUIT = 113  # 'q'