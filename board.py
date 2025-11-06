import chess

class BoardWrapper:
    def __init__(self, fen=None):
        self.board = chess.Board(fen) if fen else chess.Board()

    def legal_moves(self):
        return list(self.board.legal_moves)

    def push(self, move_uci):
        move = chess.Move.from_uci(move_uci)
        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        return False

    def push_move(self, move):
        self.board.push(move)

    def pop(self):
        self.board.pop()

    def is_game_over(self):
        return self.board.is_game_over()

    def result(self):
        return self.board.result()

    def fen(self):
        return self.board.fen()

    def copy(self):
        new = BoardWrapper()
        new.board = self.board.copy()
        return new
