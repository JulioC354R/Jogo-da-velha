class Board:

    def get_clean_board(self):
        self.board = {'a1' : 'X', 'a2' : 'X', 'a3' : 'X',
                      'b1' : ' ', 'b2' : ' ', 'b3' : ' ',
                      'c1' : ' ', 'c2' : ' ', 'c3' : ' '}
        return self.board


    #mostrar o tabuleiro
    def show_board(self, board: dict):

        linha ='------------'
        print(linha)    #0              #1          #2
        print(f' {board["a1"]} | {board["a2"]} | {board["a3"]}')
        print(linha)    #3              #4          #5
        print(f' {board["b1"]} | {board["b2"]} | {board["b3"]}')
        print(linha)    #6              #7          #8
        print(f' {board["c1"]} | {board["c2"]} | {board["c3"]}')
        print(linha)
    

    #atualizar o tabuleiro
    def update_board():
        pass

    #verificar se alguém venceu
    def check_win_condition(self, board: dict, victory_list : list):
        #Checando se X venceu
        victory = False
        winner = ''
        values_list = []
        where_wins = []

        #colocando os valores dentro de uma lista para fácil checagem:
        for keys, values in board.items():
            values_list.append(values)


        #checando linhas
        if values_list[0] and values_list[1] and values_list[2] != ' ':
            victory = True
            winner = values_list[0]
        elif values_list[3] and values_list[4] and values_list[5] != ' ':
            victory = True
            winner = values_list[3]
        if values_list[6] and values_list[7] and values_list[8] != ' ':
            victory = True
            winner = values_list[6]

        #checando colunas
        if values_list[0] and values_list[3] and values_list[6] != ' ':
            victory = True
            winner = values_list[0]

        elif values_list[1] and values_list[4] and values_list[7] != ' ':
            victory = True
            winner = values_list[1]        
        elif values_list[2] and values_list[5] and values_list[8] != ' ':
            victory = True
            winner = values_list[2]

        #checando diagonais
        if values_list[0] and values_list[4] and values_list[8] != ' ':
            victory = True
            winner = values_list[0]
        
        if values_list[2] and values_list[4] and values_list[6] != ' ':
            victory = True
            winner = values_list[2]


        if victory is True:
            print(f'Jogador {winner} venceu!')
            victory_list.append(winner)
            print(f'Onde pontuou: {where_wins}')
            print(values_list)

        """if board['a1'] and board['a2'] and board['a3'] == 'X':
            x_victory = True
        elif board['b1'] and board['b2'] and board['b3'] == 'X':
            x_victory = True
        elif board['c1'] and board['c2'] and board['c3'] == 'X':
            x_victory = True
        
        #checando colunas
        elif board['a1'] and board['b1'] and board['c1'] == 'X':
            x_victory = True

        if board['a1'] and board['a2'] and board['a3'] == 'O':
            o_victory = True"""
