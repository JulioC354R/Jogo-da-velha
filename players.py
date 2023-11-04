class Player:

    
    def player_config(self, name, symbol):
        self.name = name
        self.symbol = symbol
    


    def mark_on_board(self, board: dict, select: str, symbol : str):
        for key, value in board.items():
            if select == key:
                board[key] = symbol

        return board
    
    def switchPlayerTime(self,playerTime, player1, player2):
        if playerTime == player1:
            playerTime = player2
        elif playerTime == player2:
            playerTime = player1
        return playerTime
