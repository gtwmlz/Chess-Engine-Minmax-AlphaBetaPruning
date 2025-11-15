from .evaluation import evaluate_board

def minmax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minmax(board, depth-1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float("inf")
        for move in board.legal_moves:
            board.push(move)
            eval = minmax(board, depth-1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def best_move(board, depth=3):
    """Cari langkah terbaik untuk AI menggunakan Minmax + Alpha-Beta."""
    best_eval = -float("inf")
    best_move = None
    alpha, beta = -float("inf"), float("inf")

    for move in board.legal_moves:
        board.push(move)
        eval = minmax(board, depth-1, alpha, beta, False)
        board.pop()
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move
