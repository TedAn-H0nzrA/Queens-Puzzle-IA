import pygame
from Models.Constant import WIDTH, HEIGHT, WHITE, GREY

class Board:
    def __init__(self):
        self.rows = 8
        self.cols = 8
        self.square_size = WIDTH // self.cols
        self.queens = []  # Stocke les positions des reines (x, y)

    def draw_board(self, surface):
        """Dessine l'échiquier."""
        for row in range(self.rows):
            for col in range(self.cols):
                color = WHITE if (row + col) % 2 == 0 else GREY
                pygame.draw.rect(surface, color, 
                                 (col * self.square_size, row * self.square_size, 
                                  self.square_size, self.square_size))

        # Dessiner les reines placées
        for (x, y) in self.queens:
            pygame.draw.circle(surface, (255, 0, 0), 
                               (x * self.square_size + self.square_size // 2, 
                                y * self.square_size + self.square_size // 2), 
                               self.square_size // 3)

    def is_valid_move(self, x, y):
        """Vérifie si une reine peut être placée à la position (x, y)."""
        for qx, qy in self.queens:
            if qx == x or qy == y:  # Même colonne ou même ligne
                return False
            if abs(qx - x) == abs(qy - y):  # Même diagonale
                return False
        return True

    def place_queen(self, pos):
        """Ajoute une reine si la case est valide."""
        x, y = pos[0] // self.square_size, pos[1] // self.square_size
        if self.is_valid_move(x, y):  # Vérifie avant d'ajouter
            self.queens.append((x, y))
