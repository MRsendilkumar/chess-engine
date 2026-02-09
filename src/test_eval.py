import chess
from engine import evaluate_board

board = chess.Board()
print("Starting position score:", evaluate_board(board))

board.push_san("e4")
print("After e4:", evaluate_board(board))

board.push_san("d5")
print("After d5:", evaluate_board(board))

board.push_san("exd5")
print("After exd5:", evaluate_board(board))
