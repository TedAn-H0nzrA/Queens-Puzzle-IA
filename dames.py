import tkinter as tk
from tkinter import messagebox
import time

class EightQueens:

    def __init__(self, master):
        self.master = master
        master.title("Jeu des 8 Reines")

        self.board_size = 8
        self.cell_size = 50

        self.canvas = tk.Canvas(master, width=self.board_size * self.cell_size, height=self.board_size * self.cell_size)
        self.canvas.pack()

        self.queens = []  # Positions initiales des reines
        self.create_board()

        self.play_button = tk.Button(master, text="Jouer", command=self.solve_game)
        self.play_button.pack()

        self.moves_label = tk.Label(master, text="Nombre de coups : 0")
        self.moves_label.pack()

        self.time_label = tk.Label(master, text="Temps de résolution : 0.00 s")
        self.time_label.pack()

        self.solving = False
        self.solution_found = False

    def create_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                color = "white" if (i + j) % 2 == 0 else "grey"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        self.canvas.bind("<Button-1>", self.place_queen)

    def place_queen(self, event):
        if self.solving:
            return

        x = event.x // self.cell_size
        y = event.y // self.cell_size

        if (x, y) not in self.queens:
            if len(self.queens) < 8:
                self.queens.append((x, y))
                self.draw_queen(x, y)
            else:
                messagebox.showinfo("Attention", "Vous avez déjà placé 8 reines.")
        else:
            self.canvas.delete("queen" + str(self.queens.index((x, y))))
            self.queens.remove((x, y))

    def draw_queen(self, x, y):
        x1 = x * self.cell_size + 10
        y1 = y * self.cell_size + 10
        x2 = x1 + self.cell_size - 20
        y2 = y1 + self.cell_size - 20
        self.canvas.create_oval(x1, y1, x2, y2, fill="red", tags="queen" + str(len(self.queens) - 1))

    def solve_game(self):
        if len(self.queens) != 8:
            messagebox.showinfo("Attention", "Veuillez placer exactement 8 reines.")
            return

        self.solving = True
        self.solution_found = False
        self.moves_made = 0

        # Vérifier si la position initiale est déjà une solution valide
        if self.check_initial_positions() and len(self.queens) == 8:
            self.solving = False
            messagebox.showinfo("Information", "La position initiale est déjà une solution valide.")
            self.moves_label.config(text="Nombre de coups : 0")
            self.time_label.config(text="Temps de résolution : 0.00 s")
            return  # Pas besoin de lancer l'algorithme de résolution

        start_time = time.time()
        self.backtracking()
        end_time = time.time()

        self.solving = False

        if self.solution_found:
            self.moves_label.config(text="Nombre de coups : " + str(self.moves_made))
            self.time_label.config(text="Temps de résolution : {:.2f} s".format(end_time - start_time))
        else:
            messagebox.showinfo("Attention", "Aucune solution trouvée.")

    def check_initial_positions(self):
        # Vérifier si toutes les reines sont sur des lignes différentes
        lignes = set()
        for x, y in self.queens:
            if y in lignes:
                return False
            lignes.add(y)

        # Vérifier si les reines ne s'attaquent pas
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i][0] == self.queens[j][0] or \
                   self.queens[i][1] == self.queens[j][1] or \
                   abs(self.queens[i][0] - self.queens[j][0]) == abs(self.queens[i][1] - self.queens[j][1]):
                    return False
        return True

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def backtracking(self):
        board = [-1] * self.board_size

        def solve(row):
            if not self.solving:
                return False

            if row == self.board_size:
                self.solution_found = True
                return True

            initial_col = -1
            for queen in self.queens:
                if queen[1] == row:
                    initial_col = queen[0]
                    break

            if initial_col != -1:
                if self.is_safe(board, row, initial_col):
                    board[row] = initial_col
                    self.draw_queen_animated(row, initial_col)
                    if solve(row + 1):
                        return True
                    self.undraw_queen(row)
                    board[row] = -1
                else:
                    # Essayer de déplacer la reine initiale
                    for col in range(self.board_size):
                        if self.is_safe(board, row, col):
                            # Déplacer la reine initiale vers une position sûre
                            self.queens[self.queens.index((initial_col, row))] = (col, row)
                            board[row] = col
                            self.draw_queen_animated(row, col)
                            if solve(row + 1):
                                return True
                            self.undraw_queen(row)
                            board[row] = -1
                            # Restaurer la position initiale d'origine
                            self.queens[self.queens.index((col, row))] = (initial_col, row)
                    return False  # Aucune solution trouvée pour cette ligne
            else:
                for col in range(self.board_size):
                    if self.is_safe(board, row, col):
                        board[row] = col
                        self.draw_queen_animated(row, col)
                        if solve(row + 1):
                            return True

                        self.undraw_queen(row)
                        board[row] = -1
            return False

        solve(0)

    def draw_queen_animated(self, row, col):
        x = col * self.cell_size + 10
        y = row * self.cell_size + 10
        x2 = x + self.cell_size - 20
        y2 = y + self.cell_size - 20

        tag = "queen_anim" + str(row)
        self.canvas.create_oval(x, y, x2, y2, fill="blue", tags=tag)

        self.master.update()
        time.sleep(0.1)

        self.moves_made += 1

    def undraw_queen(self, row):
        tag = "queen_anim" + str(row)
        self.canvas.delete(tag)
        self.master.update()
        time.sleep(0.1)


root = tk.Tk()
game = EightQueens(root)
root.mainloop()