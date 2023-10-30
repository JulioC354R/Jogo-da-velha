import random
from board import Board
from players import Player

board_instance = Board()
player1 = Player()
player2 = Player()
players = [player1, player2]

victory_list = []


turn = 1

victory = False

name1 = input(f'Insira o nome do Player 1: ')
inp = input(' Insira 0 para "O" ou 1 para "X": ')
name2 = input(f'Insira o nome do Player 2: ')

if inp == 0:
    print('O player 2 ficou com "O"!')
    symbol1 = 'X'
    symbol2 = 'O'

else:
    print('O player 2 ficou com "X"!')
    symbol1 = 'O'
    symbol2 = 'X'

player1.player_config(name1, symbol1)
player2.player_config(name2, symbol2)

player_time = player1.name
if random.random() > 0.5:
    player_time = player2.name


board = board_instance.get_clean_board()

while victory == False:
    
    board_instance.show_board(board)

    victory = board_instance.check_win_condition(board, victory_list)
    
    ok = False
    print(f'Turno: {turn} Jogador da vez {player_time}')
    
    if player_time == player1.name:
            while ok == False:
                selected = input('Selecione onde deseja marcar: ')
                if selected in board and board[selected] == ' ':
                    board = player1.mark_on_board(board, selected, player1.symbol)
                    player_time = player2.name
                    ok =  True
                else: 
                    print('Por ensira em uma posição válida e desocupada!!!')

    elif player_time == player2.name and victory == False:
        while ok == False:
                selected = input('Selecione onde deseja marcar: ')
                if selected in board and board[selected] == ' ':
                    board = player2.mark_on_board(board, selected, player2.symbol)
                    player_time = player1.name
                    ok = True
                else: 
                    print('Por ensira em uma posição válida e desocupada!!!')
        
    turn +=1

    if victory == True:
        board_instance.show_board(board)
         
    
    



