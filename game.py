import random

class Game:
    

    def switchPlayerTime(self,playerTime, nameplayer1, nameplayer2):
        if playerTime == nameplayer1:
            playerTime = nameplayer2
        elif playerTime == nameplayer2:
            playerTime = nameplayer1
        return playerTime
    
    def getRandomPlayerTime(self, player1 = object, player2 = object):
        if random.random() > 0.5:
            return player1.name
        else:
            return player2.name
        
    def getWhoWins(self, winnerSymbol, player1 = object, player2 = object):
        whoWins = ''
        if winnerSymbol == player1.symbol:
            whoWins = player1.name
        elif winnerSymbol == player2.symbol:
            whoWins = player2.name
        return whoWins