import chess
from eval import evaluate

def test_starting_position_eval():
    board = chess.Board()  # starting pos
    val = evaluate(board)
    # starting position should be near zero (only mobility differences)
    assert abs(val) < 500
