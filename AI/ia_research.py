import random
import math

def solve_n_queens_annealing(initial_queens):
    def get_conflicts(board):
        # Compter les conflits entre les dames
        conflicts = 0
        n = len(board)
        for i in range(n):
            for j in range(i + 1, n):
                # Vérifier les colonnes et diagonales
                if (board[i] == board[j] or 
                    abs(board[i] - board[j]) == abs(i - j)):
                    conflicts += 1
        return conflicts

    def generate_neighbor(board):
        # Générer une configuration voisine
        new_board = board[:]
        row = random.randint(0, 7)
        new_col = random.randint(0, 7)
        new_board[row] = new_col
        return new_board

    # Initialiser le tableau avec les dames existantes
    board = [-1] * 8
    for x, y in initial_queens:
        board[x] = y
    
    # Remplir les colonnes vides
    for i in range(8):
        if board[i] == -1:
            board[i] = random.randint(0, 7)

    # Paramètres du recuit simulé
    temp = 1000
    cooling_rate = 0.99
    max_iterations = 10000

    for _ in range(max_iterations):
        # Vérifier si la solution est trouvée
        if get_conflicts(board) == 0:
            return [(i, board[i]) for i in range(8)]

        # Générer une configuration voisine
        new_board = generate_neighbor(board)
        
        # Calculer la différence de conflits
        delta = get_conflicts(new_board) - get_conflicts(board)
        
        # Critère de Metropolis
        if delta < 0 or math.exp(-delta / temp) > random.random():
            board = new_board
        
        # Refroidissement
        temp *= cooling_rate

    # Dernière vérification
    return [(i, board[i]) for i in range(8)] if get_conflicts(board) == 0 else None

def solve_n_queens_with_backtracking(initial_queens):
    def is_safe(board, row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(board, row):
        if row == 8:
            return [(i, board[i]) for i in range(8)]
        
        # Si des dames sont déjà placées, on commence après
        start_row = len(initial_queens)
        
        for col in range(8):
            if is_safe(board, row, col):
                board[row] = col
                result = backtrack(board, row + 1)
                if result:
                    return result
                board[row] = -1  # Annuler le placement
        return None

    board = [-1] * 8
    for x, y in initial_queens:
        board[x] = y

    return backtrack(board, len(initial_queens))