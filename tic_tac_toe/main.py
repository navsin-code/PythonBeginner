def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True


    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Enter row (0-2) and column (0-2) separated by a space")

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column: ").split())

            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be 0, 1, or 2")
                continue

            if board[row][col] != " ":
                print("That cell is already taken!")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space")
        except IndexError:
            print("Invalid input! Row and column must be 0, 1, or 2")


if __name__ == "__main__":
    tic_tac_toe()