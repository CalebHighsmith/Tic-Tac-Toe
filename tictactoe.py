#global variables
Player = "X"
Game_running = True
winner = None

#We need a:
#board

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#display the board

def display_board():
    print(board[6]+ "|" + board[7]+ "|" + board[8])
    print(board[3]+ "|" + board[4]+ "|" + board[5])
    print(board[0]+ "|" + board[1]+ "|" + board[2])
    return
def check_if_game_over():
    return




# play the game
def play_game():
    global Game_running
    display_board()
    ready_up = input("Welcome Player1, are you ready to begin?: ")
    ready_up2 = input("Welcome Player2, are you ready to begin?: ")
    if ready_up == "Yes" and ready_up2 == "Yes":
        print('Welcome!')

    else:
        if ready_up == "No" or ready_up2 == "No":
            Game_running = False

    while Game_running == True:

        Player_Turns()
        chec_winner()
        check_tie()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " Won!")
    elif winner == None:
        print("Fuck you for making me right this shitty code since you were dumb enough to tie.")
    return

    #Game Ending Message



def Player_Turns():
    Position = input("Choose a position from 1-9 : ")
    Position = int(Position) - 1
    board[Position] = Player
    display_board()
# play the game
#PASTE TH

def chec_winner():

    global winner
    row_winner = check_rows()

    column_winner = check_columns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
       winner = None
    return
def check_rows():
    global Game_running
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        Game_running = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global Game_running
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        Game_running = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
def check_tie():
    global Game_running
    if "-" not in board:
        Game_running = False
        return True
    else:
        return False
    return
def check_diagonals():
    global Game_running
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[2] == board[4] == board[6] != '-'

    if diagonal_1 or diagonal_2:
        Game_running = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[8]
    return
def flip_player():
    global Player
    if Player == "X":
        Player = "O"
    elif Player == "O":
        Player = "X"
    return

play_game()
