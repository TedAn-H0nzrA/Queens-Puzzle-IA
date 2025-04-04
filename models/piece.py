# models/piece.py
# Classe représentant une pièce (dame)

import pygame
from models.constants import SQUARE_SIZE

class Piece:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.calc_pos()
        self.image = None
        self.load_image()
        
    def calc_pos(self):
        """Calcule la position en pixels de la pièce"""
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    def load_image(self):
        """Charge l'image de la dame ou crée une représentation simple"""
        try:
            self.image = pygame.image.load("assets/images/queen.png")
            # Redimensionner l'image pour qu'elle tienne dans la case
            size = int(SQUARE_SIZE * 0.8)  # 80% de la taille de la case
            self.image = pygame.transform.scale(self.image, (size, size))
        except pygame.error:
            # Si l'image n'est pas trouvée, on crée un cercle simple
            self.image = None
    
    def draw(self, win, offset_x=0, offset_y=0):
        """Dessine la pièce sur la fenêtre"""
        if self.image:
            # Calculer la position centrale et ajuster pour que l'image soit centrée
            rect = self.image.get_rect(center=(self.x + offset_x, self.y + offset_y))
            win.blit(self.image, rect)
        else:
            # Dessiner un cercle comme représentation alternative
            radius = int(SQUARE_SIZE * 0.4)  # 40% de la taille de la case
            pygame.draw.circle(
                win, 
                (255, 215, 0),  # Couleur dorée
                (self.x + offset_x, self.y + offset_y), 
                radius
            )
            # Dessiner un contour
            pygame.draw.circle(
                win, 
                (0, 0, 0),  # Contour noir
                (self.x + offset_x, self.y + offset_y), 
                radius, 
                2  # Épaisseur du contour
            )
            # Dessiner un symbole de couronne simple
            points = []
            for i in range(5):
                angle = (2 * i + 1) * 3.14159 / 5
                point_x = self.x + offset_x + int(radius * 0.7 * pygame.math.Vector2(0, -1).rotate(angle * 180 / 3.14159).x)
                point_y = self.y + offset_y + int(radius * 0.7 * pygame.math.Vector2(0, -1).rotate(angle * 180 / 3.14159).y)
                points.append((point_x, point_y))
            pygame.draw.polygon(win, (255, 215, 0), points)
    
    def move(self, row, col):
        """Déplace la pièce à la nouvelle position"""
        self.row = row
        self.col = col
        self.calc_pos()