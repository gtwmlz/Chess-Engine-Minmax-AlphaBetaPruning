import chess
from .minmax import best_move

class Game:
    def __init__(self):
        self.board = chess.Board()

    def player_move(self, move_uci):
        """Terima langkah dari player (format UCI, misalnya 'e2e4')."""
        try:
            move = chess.Move.from_uci(move_uci)
            if move in self.board.legal_moves:
                self.board.push(move)
                return True
        except:
            return False
        return False

    def ai_move(self):
        """Langkah AI menggunakan Minmax + Alpha-Beta."""
        move = best_move(self.board, depth=3)
        if move:
            self.board.push(move)
        return move

    def is_game_over(self):
        return self.board.is_game_over()
