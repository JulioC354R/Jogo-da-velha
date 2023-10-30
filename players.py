class Player:

    
    def player_config(self, name, symbol):
        self.name = name
        self.symbol = symbol
    


    def mark_on_board(self, board: dict, select: str, symbol : str):
        for key, value in board.items():
            if select == key:
                board[key] = symbol

        return board