import pygame
from Models.Constant import SCALE, TITRE, BG
from Models.Board import Board
from AI.annealing_backtracing import solve_n_queens_annealing, solve_n_queens_with_backtracking
pygame.init()
ecran = pygame.display.set_mode(SCALE)
pygame.display.set_caption(TITRE)

# Initialisation du plateau et de l'IA
board = Board()
ia_active = False
message = ""
mode = "annealing" # mode par défaut

# Fonction principale du jeu
def main():
    global ia_active, message, mode
    run = True

    while run:
        ecran.fill(BG)
        board.draw_board(ecran, message)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ia_active:
                    board.place_queen(pygame.mouse.get_pos())
            
            if event.type == pygame.KEYDOWN:
                # Activer l'IA après 1 ou 2 dames placées
                if event.key == pygame.K_RETURN and len(board.queens) >= 1:
                    ia_active = True
                    if mode == "annealing":
                        solution = solve_n_queens_annealing(board.queens)
                    else:
                        solution = solve_n_queens_with_backtracking(board.queens)
                        
                    if solution:
                        board.queens = solution
                        message = "Solution trouvée !"
                    else:
                        message = "Aucune solution trouvée. Réessayez."
                        ia_active = False
                
                # Réinitialiser le plateau
                if event.key == pygame.K_r:
                    board.reset()
                    ia_active = False
                    message = ""

                # Changer de mode d'IA
                if event.key == pygame.K_s:
                    mode = "annealing"
                    message = "Mode : Simulated Annealing"
                if event.key == pygame.K_b:
                    mode = "backtracking"
                    message = "Mode : Backtracking"
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()