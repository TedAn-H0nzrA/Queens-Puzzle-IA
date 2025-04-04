# ai/backtracking.py
# Implémentation de l'algorithme de backtracking

import time
import psutil
import numpy as np
from models.constants import BOARD_SIZE

class Backtracking:
    def __init__(self, board):
        self.board = board
        self.solution = []
        self.steps = 0
        self.start_time = 0
        self.end_time = 0
        self.start_memory = 0
        self.end_memory = 0
        self.solution_found = False
    
    def reset_stats(self):
        """Réinitialise les statistiques de l'algorithme"""
        self.steps = 0
        self.start_time = 0
        self.end_time = 0
        self.start_memory = 0
        self.end_memory = 0
        self.solution_found = False
        self.solution = []
    
    def is_safe(self, board_state, row, col):
        """Vérifie si une dame peut être placée à la position (row, col)"""
        # Vérifier la ligne
        for i in range(col):
            if board_state[row][i] == 1:
                return False
        
        # Vérifier la diagonale supérieure gauche
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board_state[i][j] == 1:
                return False
        
        # Vérifier la diagonale inférieure gauche
        for i, j in zip(range(row, BOARD_SIZE), range(col, -1, -1)):
            if board_state[i][j] == 1:
                return False
        
        return True
    
    def solve_util(self, board_state, col, callback=None):
        """Fonction récursive pour résoudre le problème des N dames"""
        # Incrémenter le compteur d'étapes
        self.steps += 1
        
        # Si toutes les dames sont placées, on a trouvé une solution
        if col >= BOARD_SIZE:
            self.solution_found = True
            return True
        
        # Considérer cette colonne et essayer de placer une dame dans chaque ligne
        for row in range(BOARD_SIZE):
            # Vérifier si une dame peut être placée à cette position
            if self.is_safe(board_state, row, col):
                # Placer la dame
                board_state[row][col] = 1
                self.solution.append((row, col))
                
                # Appeler la fonction de callback si elle est fournie
                if callback and self.steps % 10 == 0:  # Appeler toutes les 10 étapes
                    callback(board_state.copy(), col + 1)
                
                # Récursivement placer le reste des dames
                if self.solve_util(board_state, col + 1, callback):
                    return True
                
                # Si placer une dame à (row, col) ne mène pas à une solution,
                # retirer la dame et essayer une autre position
                board_state[row][col] = 0
                self.solution.pop()
        
        # Si aucune dame ne peut être placée dans cette colonne, retourner False
        return False
    
    def solve(self, callback=None):
        """Résout le problème des N dames en utilisant le backtracking"""
        # Réinitialiser les statistiques
        self.reset_stats()
        
        # Enregistrer le temps et la mémoire de départ
        self.start_time = time.time()
        self.start_memory = psutil.Process().memory_info().rss / (1024 * 1024)  # En MB
        
        # Créer un échiquier vide
        board_state = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
        
        # Obtenir les positions des dames déjà placées
        current_positions = self.board.get_queen_positions()
        
        # Placer les dames existantes sur l'échiquier
        for row, col in current_positions:
            board_state[row][col] = 1
        
        # Déterminer la colonne à partir de laquelle commencer le backtracking
        start_col = 0
        
        # Trouver la colonne la plus à droite qui contient une dame
        for row, col in current_positions:
            start_col = max(start_col, col + 1)
        
        # Résoudre le problème en commençant par cette colonne
        self.solve_util(board_state, start_col, callback)
        
        # Enregistrer le temps et la mémoire de fin
        self.end_time = time.time()
        self.end_memory = psutil.Process().memory_info().rss / (1024 * 1024)  # En MB
        
        # Appliquer la solution trouvée à l'échiquier
        if self.solution_found:
            solution_positions = []
            
            # Récupérer les positions des dames déjà placées
            for row in range(BOARD_SIZE):
                for col in range(start_col):
                    if board_state[row][col] == 1:
                        solution_positions.append((row, col))
            
            # Ajouter les positions des dames placées par le backtracking
            solution_positions.extend(self.solution)
            
            # Trier les positions par colonne
            solution_positions.sort(key=lambda pos: pos[1])
            
            # Appliquer la solution à l'échiquier
            self.board.set_queen_positions(solution_positions)
        
        return self.solution_found, self.solution
    
    def get_stats(self):
        """Retourne les statistiques de l'exécution de l'algorithme"""
        return {
            "steps": self.steps,
            "time": self.end_time - self.start_time,
            "memory": self.end_memory - self.start_memory,
            "solution_found": self.solution_found
        }