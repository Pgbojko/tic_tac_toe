from tic_tac_toe import init_board, print_board, get_move

board = init_board()
board[2][0] = "x"
print_board(board)

get_move(board, "x")

