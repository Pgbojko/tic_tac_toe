
import time
player = 0


def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    
    return board





def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    
    row, col = 0, 0
    is_invalid = True
    while is_invalid:
        print("Your coordinates are? (a1,b2,c3...): ")
        coords = input().upper()
        is_invalid = False
        if len(coords) == 2:
            if coords[0] == "A":
                row = 0
            elif coords[0] == "B":
                row = 1
            elif coords[0] == "C":
                row = 2
            else:
                is_invalid = True
                print("Invalid row!!!(Please use a, b or c!): ")
                # continue
            if coords[1] == "1":
                col = 0
            elif coords[1] == "2":
                col = 1
            elif coords[1] == "3":
                col = 2
            else:
                is_invalid = True
                print("Invalid col!!(Please use 1, 2 or 3): ")
                # continue
        else:
            is_invalid = True
            print("Coords are to long(please provide 2diggit blablabla")
            continue

        if is_invalid == True:
            continue
        

        if board[row][col] == ".":
            is_invalid = False
        else:
            print("This is already taken!: provide new blabla")
            is_invalid = True
       
            
    return (row, col)



def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    
 


    


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    dot = '.'
    if dot in board:
        return False
    else:
        return True
    
    
    

def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    
    column_numbers = 2*" " + "1" + 3*" " + "2" + 3*" " + "3"
    print(" " + column_numbers)
    borders = (2*" " + 3*"-" + "+" + 3*"-" + "+" + 3*"-")
    for i in range(len(board)):
        if i == 0:
            row_letter = "A "
        elif i == 1:
            row_letter = "B "
        else:
            row_letter = "C "
        print(row_letter, board[i][0], "|", board[i][1], "|", board[i][2])
        if i < len(board)-1:
            print(borders)
    print("\n")



def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    pass



def main_menu():
    # tictactoe_game(mode='HUMAN-HUMAN')
    print("Choose you option!: ")
    print("1.   1 vs 1 deathmatch!")
    print("2.   How to play?")
    print("3.   Quit")
    
    user_input = input("Enter a number: ")
    

    if user_input == "quit" or user_input == "3":   
        print("Thanks for playing our Tic Tac Toe game! See you next time ! ")
        quit()
    elif user_input == "1": 
        cokolwiek    # 1 na 1 tryb do zrobienia
        
    elif user_input == "2":     
        print(""" Classic Tic Tac Toe game on your computer! 2 players are marked with X or O.
 To choose your option you have to insert coordinates from a1 to c3.
 To win you have to mark 3 places in a row with your symbol (X or O).
 Goodluck!
        """)

        time.sleep(12)
        main_menu()
              #wybranie opcji how to play lub błędnego znaku powoduje informacje dla gracza oraz wraca do głównego menu po przerwie określonej w sekundach
    else:
        print("Unknown command, try again! ")
        time.sleep(2.5)
        main_menu()


