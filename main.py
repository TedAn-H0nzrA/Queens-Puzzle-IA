import pygame
from Models.Constant import WIDTH, HEIGHT, SCALE, TITRE, WHITE
from Models.Board import Board
from AI.annealing import solve_n_queens

pygame.init()
ecran = pygame.display.set_mode(SCALE)
pygame.display.set_caption(TITRE)

# Initialisation du plateau et de l'IA
board = Board()
ia_active = False

# Fonction principale du jeu

def main():
    run = True
    global ia_active

    # Boucle principale du jeu
    while run:
        ecran.fill(WHITE)
        board.draw_board(ecran)

        # Gestion des touches
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not ia_active:
                    board.place_queen(pygame.mouse.get_pos())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(board.queens) >= 2:
                    ia_active = True
                    solution = solve_n_queens(board.queens)  # Lancer l’IA
                    board.queens = solution


        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()