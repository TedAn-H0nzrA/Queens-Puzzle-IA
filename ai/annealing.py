# ai/annealing.py
# Implémentation de l'algorithme du recuit simulé

import random
import math
import time
import psutil
import numpy as np
from models.constants import BOARD_SIZE, INITIAL_TEMPERATURE, COOLING_RATE, MIN_TEMPERATURE

class SimulatedAnnealing:
    def __init__(self, board):
        self.board = board
        self.best_state = None
        self.best_energy = float('inf')
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
    
    def get_initial_state(self):
        """Obtient l'état initial à partir de l'échiquier actuel"""
        current_positions = self.board.get_queen_positions()
        
        # Si l'état initial n'a pas 8 dames, compléter aléatoirement
        if len(current_positions) < BOARD_SIZE:
            available_rows = list(range(BOARD_SIZE))
            available_cols = list(range(BOARD_SIZE))
            
            # Retirer les positions déjà occupées
            for row, col in current_positions:
                if row in available_rows:
                    available_rows.remove(row)
                if col in available_cols:
                    available_cols.remove(col)
            
            # Compléter avec des positions aléatoires
            while len(current_positions) < BOARD_SIZE:
                if available_rows and available_cols:
                    row = random.choice(available_rows)
                    col = random.choice(available_cols)
                    current_positions.append((row, col))
                    available_rows.remove(row)
                    available_cols.remove(col)
                else:
                    # Si pas assez de lignes/colonnes disponibles, placer aléatoirement
                    row = random.randint(0, BOARD_SIZE - 1)
                    col = random.randint(0, BOARD_SIZE - 1)
                    if (row, col) not in current_positions:
                        current_positions.append((row, col))
        
        return current_positions
    
    def calculate_energy(self, state):
        """Calcule l'énergie (nombre de conflits) d'un état"""
        conflicts = 0
        for i in range(len(state)):
            row1, col1 = state[i]
            for j in range(i + 1, len(state)):
                row2, col2 = state[j]
                
                # Vérifier si les dames s'attaquent
                if (row1 == row2 or  # Même ligne
                    col1 == col2 or  # Même colonne
                    abs(row1 - row2) == abs(col1 - col2)):  # Diagonale
                    conflicts += 1
        
        return conflicts
    
    def get_neighbor(self, state):
        """Génère un état voisin en déplaçant une dame aléatoirement"""
        neighbor = state.copy()
        
        # Choisir une dame aléatoire
        queen_idx = random.randint(0, BOARD_SIZE - 1)
        
        # Générer une nouvelle position pour cette dame
        new_row = random.randint(0, BOARD_SIZE - 1)
        new_col = random.randint(0, BOARD_SIZE - 1)
        
        # S'assurer que la nouvelle position n'est pas déjà occupée
        while (new_row, new_col) in neighbor:
            new_row = random.randint(0, BOARD_SIZE - 1)
            new_col = random.randint(0, BOARD_SIZE - 1)
        
        # Mettre à jour la position
        neighbor[queen_idx] = (new_row, new_col)
        
        return neighbor
    
    def solve(self, max_iterations=10000, callback=None):
        """Résout le problème en utilisant l'algorithme du recuit simulé"""
        # Réinitialiser les statistiques
        self.reset_stats()
        
        # Enregistrer le temps et la mémoire de départ
        self.start_time = time.time()
        self.start_memory = psutil.Process().memory_info().rss / (1024 * 1024)  # En MB
        
        # Obtenir l'état initial
        current_state = self.get_initial_state()
        current_energy = self.calculate_energy(current_state)
        
        # Initialiser la meilleure solution
        self.best_state = current_state.copy()
        self.best_energy = current_energy
        
        # Initialiser la température
        temperature = INITIAL_TEMPERATURE
        
        # Boucle principale du recuit simulé
        iteration = 0
        while temperature > MIN_TEMPERATURE and iteration < max_iterations:
            # Générer un état voisin
            neighbor_state = self.get_neighbor(current_state)
            neighbor_energy = self.calculate_energy(neighbor_state)
            
            # Calculer la différence d'énergie
            delta_energy = neighbor_energy - current_energy
            
            # Accepter le nouvel état selon la probabilité de Metropolis
            if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
                current_state = neighbor_state
                current_energy = neighbor_energy
                
                # Mettre à jour la meilleure solution si nécessaire
                if current_energy < self.best_energy:
                    self.best_state = current_state.copy()
                    self.best_energy = current_energy
                    
                    # Si on a trouvé une solution optimale, on arrête
                    if current_energy == 0:
                        self.solution_found = True
                        break
            
            # Refroidir la température
            temperature *= COOLING_RATE
            
            # Incrémenter le compteur d'itérations
            iteration += 1
            self.steps += 1
            
            # Appeler la fonction de callback si elle est fournie
            if callback and iteration % 10 == 0:  # Appeler toutes les 10 itérations
                # Mettre à jour l'échiquier avec la meilleure solution actuelle
                callback(self.best_state, self.best_energy, temperature)
        
        # Enregistrer le temps et la mémoire de fin
        self.end_time = time.time()
        self.end_memory = psutil.Process().memory_info().rss / (1024 * 1024)  # En MB
        
        # Appliquer la meilleure solution trouvée à l'échiquier
        self.board.set_queen_positions(self.best_state)
        
        return self.solution_found, self.best_state, self.best_energy
    
    def get_stats(self):
        """Retourne les statistiques de l'exécution de l'algorithme"""
        return {
            "steps": self.steps,
            "time": self.end_time - self.start_time,
            "memory": self.end_memory - self.start_memory,
            "solution_found": self.solution_found
        }