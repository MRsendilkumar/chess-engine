import chess
from engine import get_best_move

board = chess.Board()

while not board.is_game_over():
    move = get_best_move(board, depth=2)
    if move is None:
        break
    board.push(move)
    print(board)
    print()

print("Game over:", board.result())
