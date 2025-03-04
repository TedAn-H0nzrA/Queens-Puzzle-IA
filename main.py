import pygame
from Models.Constant import WIDTH, HEIGHT, SCALE, TITRE, WHITE, GREY
from Models.Board import Board
from AI.annealing import solve_n_queens

pygame.init()
ecran = pygame.display.set_mode(SCALE)
pygame.display.set_caption(TITRE)

# Initialisation du plateau et de l'IA
board = Board()
ia_active = False
message = ""

# Fonction principale du jeu
def main():
    global ia_active, message
    run = True

    while run:
        ecran.fill(WHITE)
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
                    solution = solve_n_queens(board.queens)
                    
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

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()