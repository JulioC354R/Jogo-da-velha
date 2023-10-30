from board import Board

victory_list = []

board_instance = Board()

board = board_instance.get_clean_board()

board_instance.show_board(board)

board_instance.check_win_condition(board, victory_list)


