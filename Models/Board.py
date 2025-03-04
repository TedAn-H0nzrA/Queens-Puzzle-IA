import pygame
from Models.Constant import WIDTH, HEIGHT, CASE_CLAIRE, CASE_SOMBRE

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.square_size = min(WIDTH, HEIGHT) // self.cols
        self.queens = []
        self.board_offset_x = (WIDTH - (self.square_size * self.cols)) // 2
        self.board_offset_y = (HEIGHT - (self.square_size * self.rows)) // 2

    def reset(self):
        self.queens = []

    def draw_board(self, surface, message):
        # Dessiner l'échiquier
        for row in range(self.rows):
            for col in range(self.cols):
                # Alternance des couleurs
                color = CASE_CLAIRE if (row + col) % 2 == 0 else CASE_SOMBRE
                
                # Calculer la position réelle avec l'offset
                x = self.board_offset_x + col * self.square_size
                y = self.board_offset_y + row * self.square_size
                
                # Dessiner le carré
                pygame.draw.rect(surface, color, 
                                 (x, y, 
                                  self.square_size, self.square_size))
                
                # Dessiner les coordonnées (optionnel)
                if col == 0 or row == self.rows - 1:
                    font = pygame.font.Font(None, 24)
                    # Coordonnées de ligne (1-8)
                    if col == 0:
                        row_text = font.render(str(8 - row), True, (0, 0, 0))
                        surface.blit(row_text, (self.board_offset_x - 25, y + self.square_size // 3))
                    
                    # Coordonnées de colonne (A-H)
                    if row == self.rows - 1:
                        col_text = font.render(chr(65 + col), True, (0, 0, 0))
                        surface.blit(col_text, (x + self.square_size // 3, y + self.square_size + 5))

        # Dessiner les dames
        for (x, y) in self.queens:
            # Calculer la position réelle de la dame
            queen_x = self.board_offset_x + x * self.square_size + self.square_size // 2
            queen_y = self.board_offset_y + y * self.square_size + self.square_size // 2
            
            pygame.draw.circle(surface, (255, 0, 0), 
                               (queen_x, queen_y), 
                               self.square_size // 3)
        
        # Afficher le message
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 0, 0))
        surface.blit(text, (20, HEIGHT - 40))

    def is_valid_move(self, x, y):
        # Vérifier si la position est valide pour une dame
        for qx, qy in self.queens:
            # Vérifier les colonnes et diagonales
            if (qx == x or qy == y or 
                abs(qx - x) == abs(qy - y)):
                return False
        return True

    def place_queen(self, pos):
        # Ajuster les coordonnées avec l'offset
        x = (pos[0] - self.board_offset_x) // self.square_size
        y = (pos[1] - self.board_offset_y) // self.square_size

        # Vérifier les limites du plateau
        if (x < 0 or x >= 8 or y < 0 or y >= 8):
            return False

        # Vérifier si le placement est valide
        if self.is_valid_move(x, y):
            self.queens.append((x, y))
            return True
        
        return False