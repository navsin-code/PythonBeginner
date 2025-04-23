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


def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]


def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 1
    if check_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -float("inf")
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            best_move = (i, j)
    return best_move


def tic_tac_toe_with_ai():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic Tac Toe vs AI!")
    print("You are X, AI is O")
    print("Enter row (0-2) and column (0-2) separated by a space")

    while True:
        print_board(board)
        try:
            row, col = map(int, input("Your move (row and column): ").split())

            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be 0, 1, or 2")
                continue

            if board[row][col] != " ":
                print("That cell is already taken!")
                continue

            board[row][col] = "X"

            if check_winner(board, "X"):
                print_board(board)
                print("You win!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            print("AI's move:")
            ai_row, ai_col = ai_move(board)
            board[ai_row][ai_col] = "O"

            if check_winner(board, "O"):
                print_board(board)
                print("AI wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

        except ValueError:
            print("Invalid input! Please enter two numbers separated by a space")
        except IndexError:
            print("Invalid input! Row and column must be 0, 1, or 2")


if __name__ == "__main__":
    tic_tac_toe_with_ai()