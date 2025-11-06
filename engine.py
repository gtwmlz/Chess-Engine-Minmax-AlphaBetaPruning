import chess
import time
from eval import evaluate

nodes_searched = 0

def negamax(board: chess.Board, depth: int, alpha: int, beta: int) -> int:
    global nodes_searched
    nodes_searched += 1

    if depth == 0 or board.is_game_over():
        return evaluate(board)

    max_score = -10**9
    for move in board.legal_moves:
        board.push(move)
        score = -negamax(board, depth - 1, -beta, -alpha)
        board.pop()

        if score > max_score:
            max_score = score
        if max_score > alpha:
            alpha = max_score
        if alpha >= beta:
            break  # alpha-beta cutoff
    return max_score

def find_best_move(fen: str, depth: int = 3):
    global nodes_searched
    board = chess.Board(fen)
    best_move = None
    best_score = -10**9
    nodes_searched = 0
    start = time.time()

    alpha = -10**9
    beta = 10**9

    for move in board.legal_moves:
        board.push(move)
        score = -negamax(board, depth - 1, -beta, -alpha)
        board.pop()
        if score > best_score:
            best_score = score
            best_move = move
        if score > alpha:
            alpha = score

    elapsed = time.time() - start
    return {
        "best_move": best_move.uci() if best_move else None,
        "score": best_score,
        "nodes": nodes_searched,
        "time": elapsed,
        "depth": depth,
    }
