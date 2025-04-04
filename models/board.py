# models/board.py
# Classe représentant l'échiquier

import pygame
import numpy as np
from models.constants import *
from models.piece import Piece

class Board:
    def __init__(self):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.queens = []  # Liste des pièces sur l'échiquier
        self.selected_piece = None
        self.selected_row = -1
        self.selected_col = -1
        self.valid_solution = False
    
    def draw_squares(self, win):
        """Dessine les cases de l'échiquier"""
        win.fill(BLACK)
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                # Alternance des couleurs pour les cases
                color = LIGHT_SQUARE if (row + col) % 2 == 0 else DARK_SQUARE
                pygame.draw.rect(
                    win, 
                    color, 
                    (BOARD_X + col * SQUARE_SIZE, BOARD_Y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )
                
                # Afficher les coordonnées de la case (pour le débogage)
                font = pygame.font.SysFont(None, 15)
                text = font.render(f"{row},{col}", True, (100, 100, 100))
                win.blit(text, (BOARD_X + col * SQUARE_SIZE + 2, BOARD_Y + row * SQUARE_SIZE + 2))
    
    def draw(self, win):
        """Dessine l'échiquier complet avec les pièces"""
        self.draw_squares(win)
        
        # Dessiner la surbrillance pour la case sélectionnée
        if self.selected_row != -1 and self.selected_col != -1:
            s = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
            s.fill(HIGHLIGHT)
            win.blit(s, (BOARD_X + self.selected_col * SQUARE_SIZE, BOARD_Y + self.selected_row * SQUARE_SIZE))
        
        # Dessiner les pièces
        for piece in self.queens:
            piece.draw(win, BOARD_X, BOARD_Y)
        
        # Dessiner le contour de l'échiquier
        pygame.draw.rect(
            win, 
            BLACK, 
            (BOARD_X, BOARD_Y, BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE),
            2  # Épaisseur du contour
        )
        
    def add_piece(self, row, col):
        """Ajoute une pièce à la position spécifiée"""
        # Vérifier si la position est valide
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            # Vérifier si la case est vide
            if self.board[row][col] == 0:
                self.board[row][col] = 1
                new_piece = Piece(row, col)
                self.queens.append(new_piece)
                self.check_solution()  # Vérifier si la solution est valide
                return True
        return False
    
    def remove_piece(self, row, col):
        """Supprime une pièce de la position spécifiée"""
        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            if self.board[row][col] == 1:
                self.board[row][col] = 0
                # Trouver et supprimer la pièce de la liste
                for i, piece in enumerate(self.queens):
                    if piece.row == row and piece.col == col:
                        self.queens.pop(i)
                        break
                self.check_solution()  # Vérifier si la solution est valide
                return True
        return False
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        """Déplace une pièce d'une position à une autre"""
        if self.remove_piece(from_row, from_col):
            return self.add_piece(to_row, to_col)
        return False
    
    def select(self, row, col):
        """Sélectionne une case de l'échiquier"""
        # Si une pièce est déjà sélectionnée, on essaie de la déplacer
        if self.selected_piece is not None:
            result = self.move_piece(
                self.selected_piece.row, 
                self.selected_piece.col, 
                row, col
            )
            self.selected_piece = None
            self.selected_row = -1
            self.selected_col = -1
            return result
        
        # Sinon, on sélectionne une pièce si elle existe
        for piece in self.queens:
            if piece.row == row and piece.col == col:
                self.selected_piece = piece
                self.selected_row = row
                self.selected_col = col
                return True
        
        # Si on clique sur une case vide, on ajoute une pièce
        if len(self.queens) < BOARD_SIZE:  # Maximum 8 dames
            return self.add_piece(row, col)
        
        return False
    
    def get_queen_positions(self):
        """Retourne les positions des dames sous forme de liste de tuples (row, col)"""
        return [(queen.row, queen.col) for queen in self.queens]
    
    def set_queen_positions(self, positions):
        """Place les dames aux positions spécifiées"""
        self.clear()
        for row, col in positions:
            self.add_piece(row, col)
    
    def clear(self):
        """Efface toutes les pièces de l'échiquier"""
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        self.queens = []
        self.selected_piece = None
        self.selected_row = -1
        self.selected_col = -1
        self.valid_solution = False
    
    def is_under_attack(self, row, col):
        """Vérifie si une position est attaquée par une dame existante"""
        for queen in self.queens:
            # Ignorer la dame à la même position (utile pour vérifier si la solution actuelle est valide)
            if queen.row == row and queen.col == col:
                continue
                
            # Vérifier si la dame attaque horizontalement, verticalement ou en diagonale
            if (queen.row == row or  # Même ligne
                queen.col == col or  # Même colonne
                abs(queen.row - row) == abs(queen.col - col)):  # Diagonale
                return True
        return False
    
    def check_solution(self):
        """Vérifie si la solution actuelle est valide"""
        # Une solution valide doit avoir exactement 8 dames
        if len(self.queens) != BOARD_SIZE:
            self.valid_solution = False
            return False
        
        # Vérifier si aucune dame n'attaque une autre
        for queen in self.queens:
            # On retire temporairement la dame pour vérifier si elle est attaquée
            self.board[queen.row][queen.col] = 0
            is_attacked = self.is_under_attack(queen.row, queen.col)
            self.board[queen.row][queen.col] = 1
            
            if is_attacked:
                self.valid_solution = False
                return False
        
        self.valid_solution = True
        return True
    
    def get_conflicts(self):
        """Calcule le nombre de paires de dames qui s'attaquent mutuellement"""
        conflicts = 0
        queens_positions = self.get_queen_positions()
        
        for i in range(len(queens_positions)):
            row1, col1 = queens_positions[i]
            for j in range(i + 1, len(queens_positions)):
                row2, col2 = queens_positions[j]
                
                # Vérifier si les dames s'attaquent
                if (row1 == row2 or  # Même ligne
                    col1 == col2 or  # Même colonne
                    abs(row1 - row2) == abs(col1 - col2)):  # Diagonale
                    conflicts += 1
        
        return conflicts
    
    def get_all_conflicts(self):
        """Calcule un tableau des conflits pour chaque position"""
        conflicts_map = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        
        # Pour chaque position possible
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                # Si la case contient déjà une dame, elle ne peut pas être utilisée
                if self.board[row][col] == 1:
                    conflicts_map[row][col] = -1
                    continue
                    
                # Ajouter temporairement une dame et compter les conflits
                self.board[row][col] = 1
                temp_queen = Piece(row, col)
                self.queens.append(temp_queen)
                
                conflicts = self.get_conflicts()
                conflicts_map[row][col] = conflicts
                
                # Retirer la dame temporaire
                self.queens.pop()
                self.board[row][col] = 0
        
        return conflicts_map