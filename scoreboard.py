class Scoreboard:
    
    def __init__(self):
        self.matchHistory = []
        self.p1_victorys = 0
        self.p2_victorys = 0
        self.draws = 0

    
    def printScoreboard(self, player1, player2):
        matches = self.matchHistory

        self.p1_victorys = matches.count(player1.name)
        self.p2_victorys = matches.count(player2.name)
        self.draws = matches.count('DRAW')
        
        print(f'-------------   PLACAR   -------------')
        print(f'Vitórias {player1.name}: {self.p1_victorys}')
        print(f'Vitórias {player2.name}: {self.p2_victorys}')
        print(f'Empates: {self.draws}')


        