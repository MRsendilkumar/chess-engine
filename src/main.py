import chess
from engine import get_best_move

def play():
    board = chess.Board()
    print(board)

    while not board.is_game_over():
        if board.turn:
            move = input("Your move (e.g. e2e4): ")
            try:
                board.push_uci(move)
            except:
                print("Invalid move.")
                continue
        else:
            move = get_best_move(board, depth=3)
            print(f"Engine plays: {move}")
            board.push(move)

        print(board)
        print()

    print("Game over:", board.result())

if __name__ == "__main__":
    play()
