from engine import find_best_move

# simple mate-in-1 position (white to move)
# famous: Fool's mate reversed or quick mate example:
# FEN where white can mate in 1: black king on e8, white queen on d7 and rook delivering mate, but simpler:
# Use a canonical mate-in-1: "r1bqkb1r/pppp1ppp/2n5/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 4"
# This is not necessarily mate-in-1; instead we test that function returns a move string for legal move.

def test_find_best_move_returns_move():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    res = find_best_move(fen, depth=1)
    assert res["best_move"] is not None
    assert isinstance(res["best_move"], str)
    assert res["depth"] == 1
