import pygame
import time
import tracemalloc
from Models.Constant import SCALE, TITRE, BG
from Models.Board import Board
from AI.ia_research import solve_n_queens_annealing, solve_n_queens_with_backtracking
pygame.init()
ecran = pygame.display.set_mode(SCALE)
pygame.display.set_caption(TITRE)

# Initialisation du plateau et de l'IA
board = Board()
ia_active = False
message = ""
mode = "annealing" # mode par défaut
execution_time = 0
memory_usage = 0

# Fonction principale du jeu
def main():
    global ia_active, message, mode, execution_time, memory_usage
    run = True
    clock = pygame.time.Clock()

    while run:
        ecran.fill(BG)
        board.draw_board(ecran, message)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Limiter à 8 dames maximum
                if len(board.queens) < 8:
                    board.place_queen(pygame.mouse.get_pos())
            
            if event.type == pygame.KEYDOWN:
                # Activer l'IA après au moins 1 dame placée
                if event.key == pygame.K_RETURN and len(board.queens) >= 1:
                    # Préparer pour mesurer les performances
                    tracemalloc.start()
                    start_time = time.time()

                    # Compléter le reste des dames
                    if mode == "annealing":
                        solution = solve_n_queens_annealing(board.queens)
                    else:
                        solution = solve_n_queens_with_backtracking(board.queens)
                    
                    # Calculer le temps et la mémoire
                    execution_time = time.time() - start_time
                    memory_usage = tracemalloc.get_traced_memory()[1]
                    tracemalloc.stop()

                    if solution:
                        board.queens = solution
                        message = f"Solution trouvée ! Temps: {execution_time:.4f}s, Mémoire: {memory_usage/1024:.2f} Ko"
                    else:
                        message = "Aucune solution trouvée. Réessayez."
                        ia_active = False
                
                # Réinitialiser le plateau
                if event.key == pygame.K_r:
                    board.reset()
                    ia_active = False
                    message = ""
                    execution_time = 0
                    memory_usage = 0

                # Changer de mode d'IA
                if event.key == pygame.K_s:
                    mode = "annealing"
                    message = "Mode : Recuit Simulé"
                if event.key == pygame.K_b:
                    mode = "backtracking"
                    message = "Mode : Backtracking"
        
        pygame.display.update()
        clock.tick(60)  # Limiter à 60 FPS
    
    pygame.quit()

if __name__ == "__main__":
    main()