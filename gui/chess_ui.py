import tkinter as tk
import chess
from engine.game import Game
from engine.evaluation import evaluate_board

class ChessUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Engine GUI")
        self.canvas = tk.Canvas(root, width=480, height=480)
        self.canvas.pack()
        
        # Label skor heuristik
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack(pady=5)

        self.game = Game()
        self.square_size = 60
        self.draw_board()
        self.update_score()

        self.canvas.bind("<Button-1>", self.on_click)
        self.selected_square = None

    def draw_board(self):
        self.canvas.delete("all")
        colors = ["#EEEED2", "#769656"]
        for row in range(8):
            for col in range(8):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                color = colors[(row+col) % 2]
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Gambar bidak
        for square, piece in self.game.board.piece_map().items():
            row = 7 - (square // 8)
            col = square % 8
            x = col * self.square_size + self.square_size//2
            y = row * self.square_size + self.square_size//2
            self.canvas.create_text(x, y, text=piece.symbol(), font=("Arial", 24))

    def update_score(self):
        score = evaluate_board(self.game.board)
        self.score_label.config(text=f"Score: {score}")

    def on_click(self, event):
        col = event.x // self.square_size
        row = event.y // self.square_size
        square = (7-row)*8 + col

        if self.selected_square is None:
            self.selected_square = square
        else:
            move_uci = f"{chess.square_name(self.selected_square)}{chess.square_name(square)}"
            if self.game.player_move(move_uci):
                if not self.game.is_game_over():
                    self.game.ai_move()
            self.selected_square = None
            self.draw_board()
            self.update_score()
