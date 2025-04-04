# main.py
# Point d'entrée du programme

import pygame
import threading
import os
from models.constants import *
from models.board import Board
from ai.annealing import SimulatedAnnealing
from ai.backtracking import Backtracking

# Initialiser Pygame
pygame.init()

# Créer la fenêtre
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jeu des 8 Dames - IA")

# Charger les polices
pygame.font.init()
FONT = pygame.font.SysFont(None, FONT_SIZE)
TITLE_FONT = pygame.font.SysFont(None, TITLE_FONT_SIZE)
INFO_FONT = pygame.font.SysFont(None, INFO_FONT_SIZE)

# Créer le répertoire pour les ressources s'il n'existe pas
os.makedirs("assets/images", exist_ok=True)

# Créer l'échiquier
board = Board()

# Créer les algorithmes d'IA
annealing = SimulatedAnnealing(board)
backtracking = Backtracking(board)

# Variables
running = True
solving = False
algorithm_thread = None
info_text = ""

def update_board(positions, energy_or_col, temp_or_none=None):
    """Met à jour l'échiquier avec les positions actuelles (callback pour les algorithmes)"""
    global info_text
    board.set_queen_positions(positions)
    if temp_or_none is not None:  # Simulated Annealing
        info_text = f"Énergie: {energy_or_col} | Température: {temp_or_none:.2f}"
    else:  # Backtracking
        info_text = f"Colonnes résolues: {energy_or_col}"

def run_algorithm(algorithm):
    """Exécute l'algorithme dans un thread séparé"""
    global solving, info_text
    solving = True
    if isinstance(algorithm, SimulatedAnnealing):
        success, state, energy = algorithm.solve(callback=update_board)
        stats = algorithm.get_stats()
        info_text = f"Solution trouvée: {success} | Énergie: {energy} | Étapes: {stats['steps']} | Temps: {stats['time']:.2f}s"
    elif isinstance(algorithm, Backtracking):
        success, solution = algorithm.solve(callback=update_board)
        stats = algorithm.get_stats()
        info_text = f"Solution trouvée: {success} | Étapes: {stats['steps']} | Temps: {stats['time']:.2f}s"
    solving = False

# Boucle principale
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == KEY_QUIT:  # 'q' pour quitter
                running = False
            elif event.key == KEY_RESET and not solving:  # 'r' pour réinitialiser
                board.clear()
                info_text = "Échiquier réinitialisé"
            elif event.key == KEY_ANNEALING and not solving:  # 'a' pour recuit simulé
                algorithm_thread = threading.Thread(target=run_algorithm, args=(annealing,))
                algorithm_thread.start()
                info_text = "Recuit simulé en cours..."
            elif event.key == KEY_BACKTRACKING and not solving:  # 'b' pour backtracking
                algorithm_thread = threading.Thread(target=run_algorithm, args=(backtracking,))
                algorithm_thread.start()
                info_text = "Backtracking en cours..."
        
        elif event.type == pygame.MOUSEBUTTONDOWN and not solving:
            # Convertir les coordonnées de la souris en position sur l'échiquier
            pos = pygame.mouse.get_pos()
            col = (pos[0] - BOARD_X) // SQUARE_SIZE
            row = (pos[1] - BOARD_Y) // SQUARE_SIZE
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
                board.select(row, col)
                info_text = f"Case sélectionnée: ({row}, {col})"

    # Dessiner l'échiquier
    board.draw(WIN)

    # Afficher le titre
    title = TITLE_FONT.render("Jeu des 8 Dames", True, WHITE)
    WIN.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 20))

    # Afficher les informations
    info = INFO_FONT.render(info_text, True, WHITE)
    WIN.blit(info, (10, SCREEN_HEIGHT - 30))

    # Afficher les instructions
    instructions = INFO_FONT.render("a: Recuit | b: Backtracking | r: Réinitialiser | q: Quitter", True, WHITE)
    WIN.blit(instructions, (10, SCREEN_HEIGHT - 50))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Nettoyer et quitter
if algorithm_thread and algorithm_thread.is_alive():
    algorithm_thread.join()
pygame.quit()