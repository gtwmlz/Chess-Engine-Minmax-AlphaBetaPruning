import chess

class Board:
    def __init__(self):
        # Inisialisasi papan catur standar
        self.board = chess.Board()

    def get_legal_moves(self):
        """Mengembalikan daftar langkah legal dalam format UCI (misalnya 'e2e4')."""
        return [move.uci() for move in self.board.legal_moves]

    def apply_move(self, move_uci):
        """Menerapkan langkah ke papan jika legal."""
        try:
            move = chess.Move.from_uci(move_uci)
            if move in self.board.legal_moves:
                self.board.push(move)
                return True
        except Exception:
            return False
        return False

    def undo_move(self):
        """Membatalkan langkah terakhir (pop stack)."""
        if self.board.move_stack:
            self.board.pop()

    def is_game_over(self):
        """Cek apakah permainan sudah selesai (checkmate, stalemate, dll)."""
        return self.board.is_game_over()

    def get_fen(self):
        """Mengembalikan representasi FEN dari papan saat ini."""
        return self.board.fen()

    def piece_map(self):
        """Mengembalikan dictionary {square: piece} untuk menggambar papan."""
        return self.board.piece_map()

    def turn(self):
        """Mengembalikan giliran saat ini: True=White, False=Black."""
        return self.board.turn
