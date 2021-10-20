game_ongoing=True

winner = None

current_player = "X"

board = [ "-","-","-",
          "-","-","-",
          "-","-","-", ]

def display_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):
    print(player + "'s turn ")
    position = input("Choose a number between 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input ("invalid please select a number 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there go again: ")
            1
    board[position] = player
    display_board()

def check_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    col_win = check_cols()
    diag_win = check_diag()
    row_win = check_rows()
    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diag_win:
        winner = diag_win
    else:
        winner = None
    return 

def check_rows():
    global game_ongoing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_ongoing = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return
    

def check_cols():
    global game_ongoing
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_ongoing = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return

def check_diag():
    global game_ongoing
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_ongoing = False
    if diag_1:
        return board[0]
    if diag_2:
        return board[2]
    return

def check_tie():
    global game_ongoing
    if "-" not in board:
        game_ongoing = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return



def play_game():
    global current_player
    display_board()
    current_player = "X"
    while game_ongoing:
        handle_turn(current_player)
        check_game_over()
        flip_player()

    #game has ended
    if winner == "X" or winner =="O":
        print(winner + " won ")
    elif winner == None:
        print("Tie")
    
    

play_game()
#Board
#Display
#Play game
#check win -> check rows -> check cols -> check diags
#chekc tie
#flip player

