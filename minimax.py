def show_board(board_values: dict) -> None:
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board_values[1], board_values[2], board_values[3]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board_values[4], board_values[5], board_values[6]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(board_values[7], board_values[8], board_values[9]))
    print("\t     |     |")
    print("-----------------------------------------------")


def add_letter(board: dict, position: int, letter: str) -> dict:
    board[position] = letter
    show_board(board)
    is_finish(board, letter)
    return board


def check_free_space(board: dict, position: int) -> bool:
    if board[position] == " ":
        return True
    return False


def is_finish(board: dict, letter: str) -> bool:
    if is_win(board, letter):
        print(f"{letter} wins!")
        return True
    elif is_draw(board):
        print("Draw :)))")
        return True
    return False


def is_draw(board: dict) -> bool:
    for position in board.keys():
        if board[position] == " ":
            return False
    return True


def is_win(board: dict, letter: str) -> bool:
    for i in [1, 4, 7]:
        if board[i] == board[i + 1] == board[i + 2] == letter:
            return True
    for i in [1, 2, 3]:
        if board[i] == board[i + 3] == board[i + 6] == letter:
            return True
    if board[1] == board[5] == board[9] == letter:
        return True
    if board[3] == board[5] == board[7] == letter:
        return True
    return False


def get_children(board: dict, letter: str) -> list:
    boards = list()
    for key in board.keys():
        if board[key] == " ":
            board[key] = letter
            boards.append(board.copy())
            board[key] = " "
    return boards


def get_valid_positions(board: dict) -> list:
    valid_positions = []
    for position in board.keys():
        if board[position] == " ":
            valid_positions.append(position)
    return valid_positions


def minimax(board: dict, turn: int) -> int:
    global count_simple_move
    count_simple_move += 1
    if is_win(board, "X"):
        return 1
    elif is_win(board, "O"):
        return -1
    elif is_draw(board):
        return 0

    if turn == 1:
        return max_value(board)

    else:
        return min_value(board)


def max_value(board: dict) -> int:
    best_score = -10
    for child in get_children(board, "X"):
        current_score = minimax(child, 0)
        best_score = max(current_score, best_score)
    return best_score


def min_value(board: dict) -> int:
    best_score = +10
    for child in get_children(board, "O"):
        current_score = minimax(child, 1)
        best_score = min(current_score, best_score)
    return best_score


def minimax_alpha_beta(board: dict, turn: int, alpha: float, beta: float) -> int:
    global count_alpha_beta_move
    count_alpha_beta_move += 1
    if is_win(board, "X"):
        return 1
    elif is_win(board, "O"):
        return -1
    elif is_draw(board):
        return 0

    if turn == 1:
        return max_alpha_beta(board, alpha, beta)

    else:
        return min_alpha_beta(board, alpha, beta)


def max_alpha_beta(board: dict, alpha: float, beta: float) -> int:
    best_score = -10
    for child in get_children(board, "X"):
        current_score = minimax_alpha_beta(child, 0, alpha, beta)
        best_score = max(current_score, best_score)
        if best_score >= beta:
            return best_score
        alpha = max(alpha, best_score)
    return best_score


def min_alpha_beta(board: dict, alpha: float, beta: float) -> int:
    best_score = +10
    for child in get_children(board, "O"):
            current_score = minimax_alpha_beta(child, 1, alpha, beta)
            best_score = min(current_score, best_score)
            if best_score <= alpha:
                return best_score
            beta = min(beta, best_score)
    return best_score


def computer_move(board: dict, alpha_beta: bool) -> dict:
    best_score = -10
    best_position = 0
    for key in board.keys():
        if board[key] == " ":
            board[key] = "X"
            if alpha_beta:
                current_score = minimax_alpha_beta(board, 0, -100, +100)
            else:
                current_score = minimax(board, 0)
            board[key] = " "
            if current_score > best_score:
                best_score = current_score
                best_position = key
    board = add_letter(board, best_position, "X")
    return board


board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
count_simple_move = 0
count_alpha_beta_move = 0
while not (is_finish(board, "O") or is_finish(board, "X")):
    user_position = int(input(f"please enter a position from {get_valid_positions(board)}...\n"))
    if not check_free_space(board, user_position):
        print("please select an empty space !!")
        continue
    board = add_letter(board, user_position, "O")
    if is_draw(board):
        break
    board = computer_move(board, alpha_beta=True)
# print("total number:", count_simple_move)
# print("total number using alpha-beta:", count_alpha_beta_move)
#
#
# count_simple_move = 0
# count_alpha_beta_move = 0
# board = {1: "O", 2: "O", 3: "X", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
# show_board(board)
# computer_move(board.copy(), True)
# computer_move(board.copy(), False)
# print("total number:", count_simple_move)
# print("total number using alpha-beta:", count_alpha_beta_move)