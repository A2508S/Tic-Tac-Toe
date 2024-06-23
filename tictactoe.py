
#restart
import random

#variable
board_list = [1, 2,3,4,5,6,7,8,9]
marker1 = ''
marker2 = ''
full_board = False
post = '1'
win = "False"


#functions
def board(board_list = board_list):
    print("",board_list[6], "|",board_list[7], "|",board_list[8], "")
    print("---|---|---")
    print("",board_list[3], "|",board_list[4], "|",board_list[5], "")
    print("---|---|---")
    print("",board_list[0], "|",board_list[1], "|",board_list[2], "")


def player_input():
    global marker1
    global marker2
    p_1 = input("Which symbol will player 1 take? (X/O): ")
    while p_1.upper() not in "XO":
        print("Invalid symbol selected!")

        p_1 = input("Select X or O: ")

    if p_1.upper() == "X":
        marker1 = "X"
        marker2 = "O"
    else:
        marker1 = "O"
        marker2 = "X"
    print("Player 1- ", marker1, "Player 2-", marker2)


def place_marker(marker, position,board_list = board_list):
    while str(position) not in "123456789":
        print("No such position found!")
    
    board_list[int(position)-1] = marker


def win_check(mark ,board_list = board_list):
    global win
    if board_list[0] == board_list[1] == board_list[2] == mark or board_list[3] == board_list[4] == board_list[5]== mark or board_list[6] == board_list[7] == board_list[8] == mark or board_list[0] == board_list[3] == board_list[6] == mark or board_list[1] == board_list[4] == board_list[7] == mark or board_list[2] == board_list[5] == board_list[8] == mark or board_list[0] == board_list[4] == board_list[8] == mark or board_list[2] == board_list[4] == board_list[6] == mark :
        board()
        win = True
    else:
        win = False


def go_first():
    a = random.randint(0,1)
    if a == 0:
        print("P1 will go first")
        return 1
    else:
        print("P2 will go first")
        return 2       


def space_check(position, board_list = board_list):
    if str(board_list[int(position)-1]) not in "XO":
        return True;
    else:
        return False


def full_board_check(board_list = board_list):
    global full_board
    for i in range(0, len(board_list)):
        if str(board_list[i]) not in "XO":
            full_board = False
            break;
        else:
            full_board = True
            


def player_choice():
    global post
    while True:
        try:
            post = int(input("Where would you like to place the symbol? (1-9): "))
            break;
        except ValueError:
            print("Enter a NUMBER!")
    while int(post) not in (range(1,10)):
        print("Invalid position for the symbol")
        try:
            post = input("Place for symbol? (1-9): ")
        except:
            print("Enter a NUMBER!")
    else:
        while space_check(post) == False:
            print("Space occupied by a symbol!")
            post = input("Choose another position (1-9): ")
            while int(post) not in (range(1,10)):
                print("Invalid position for the symbol")
                try:
                    post = input("Place for symbol? (1-9): ")
                except:
                    print("Enter a NUMBER!")
        

def start():
    global post
    global full_board
    global win
    print('Welcome to Tic Tac Toe!')
    while True:
        board_list = [1, 2,3,4,5,6,7,8,9]
        player_input()
        turn = go_first()
        while True:
            if turn == 1:
                board()
                player_choice()
                place_marker(marker1, post)
                full_board_check()
                win_check(marker1)
                if win:
                    print("Player 1 has won! ggs")
                    return False
                elif full_board:
                    print("The game is a tie, the board is full!")
                    break;
                else:
                    turn = 2
            if turn == 2:
                board()
                player_choice()
                place_marker(marker2, post)
                full_board_check()
                win_check(marker2)
                if win:
                    print("Player 2 has won! ggs")
                    return False
                elif full_board:
                    print("The game is a tie, the board is full!")
                    break;
                else:
                    turn = 1   

#code 
start()
