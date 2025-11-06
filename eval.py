import chess

# simple material evaluator (centipawn-like)
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000,
}

def evaluate(board: chess.Board) -> int:
    """
    Returns evaluation from White's perspective in centipawns.
    Positive = advantage for White, Negative = advantage for Black.
    """
    material = 0
    for piece_type in range(1, 7):
        material += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        material -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    # small mobility bonus
    try:
        mobility = len(list(board.legal_moves))
    except Exception:
        mobility = 0

    return material + (mobility if board.turn == chess.WHITE else -mobility)
