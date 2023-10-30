class Board:

    def get_clean_board(self):
        self.board = {'a1' : ' ', 'a2' : ' ', 'a3' : ' ',
                      'b1' : ' ', 'b2' : ' ', 'b3' : ' ',
                      'c1' : ' ', 'c2' : ' ', 'c3' : ' '}
        return self.board


    #mostrar o tabuleiro
    def show_board(self, board: dict):

        linha ='------------'
        
        print()         #0              #1          #2
        print(f' {board["a1"]} | {board["a2"]} | {board["a3"]}')
        print(linha)    #3              #4          #5
        print(f' {board["b1"]} | {board["b2"]} | {board["b3"]}')
        print(linha)    #6              #7          #8
        print(f' {board["c1"]} | {board["c2"]} | {board["c3"]}')
        print()

    

    #atualizar o tabuleiro
    def update_board():
        pass

    #verificar se alguém venceu
    def check_win_condition(self, board: dict, victory_list : list):
        #Checando se X venceu
        victory = False
        winner = ''
        winning_positions = [('a1','a2','a3'), ('b1','b2','b3'), ('c1','c2','c3'),
                             ('a1','b1','c1'), ('a2','b2','c2'), ('a3','b3','c3'),
                             ('a1','b2','c3'),('a3','b2','c1')]

        #checando linhas
        if board['a1'] == board['a2'] == board['a3'] and board['a1'] != ' ':
            victory = True
            winner = board['a1']
            where_wins = winning_positions[0]

        elif board['b1'] == board['b2'] == board['b3'] and board['b1']!= ' ':
            victory = True
            winner = board['b1']
            where_wins = winning_positions[1]

        if board['c1'] == board['c2'] == board['c3'] and board['c1'] != ' ':
            victory = True
            winner = board['c1']
            where_wins = winning_positions[2]


        #checando colunas
        if board['a1'] == board['b1'] == board['c1'] and board['a1'] != ' ':
            victory = True
            winner =  board['a1']
            where_wins = winning_positions[3]

        elif board['a2'] == board['b2'] == board['c2'] and board['a2'] != ' ':
            victory = True
            winner =  board['a2']
            where_wins = winning_positions[4]

        elif board['a3'] == board['b3'] == board['c3'] and board['a3'] != ' ':
            victory = True
            winner =  board['a3']
            where_wins = winning_positions[5]


        #checando diagonais
        if  board['a1'] == board['b2'] == board['c3'] and board['a1'] != ' ':
            victory = True
            winner =  board['a1']
            where_wins = winning_positions[6]
        
        if board['a3'] == board['b2'] == board['c1'] and board['a3'] != ' ':
            victory = True
            winner = board['a3']
            where_wins = winning_positions[7]


        if victory is True:
            print(f'Jogador {winner} venceu!')
            victory_list.append(winner)
            print(f'Onde pontuou: {where_wins}')

        return victory

