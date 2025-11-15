piece_values = {
    "P": 10, "N": 30, "B": 30, "R": 40, "Q": 60, "K": 100,
    "p": -10, "n": -30, "b": -30, "r": -40, "q": -60, "k": -100
}

def evaluate_board(board):
    """Hitung skor papan berdasarkan nilai heuristik bidak."""
    score = 0
    for square in board.piece_map().values():
        score += piece_values.get(square.symbol(), 0)
    return score
