
from Player import Player
from Drawpile import Drawpile
from Discardpile import Discardpile
from Playercardpile import Playercardpile
class Game():
    def __init__(self, maxrounds:int,roundnum:int) ->None:
        self.maxrounds = maxrounds
        self.roundnum = roundnum
        
        name1 = 'marci'
        age1 = 9
        name2 = 'sanyi'
        age2 = 1
        self.Player1 = Player(name1,1,0)
        self.Player2 = Player(name2,2,0)
        self.drawpile = Drawpile()
        

        self.discardpile1 = Discardpile(1)
        self.discardpile2 = Discardpile(2)
        self.discardpile3 = Discardpile(3)
        self.discardpile4 = Discardpile(4)
        self.discardpile5 = Discardpile(5)
        player1_piles = [Playercardpile(i, 1) for i in range(5)]
        player2_piles = [Playercardpile(i, 2) for i in range(5)]
        
        self.Player1.createstartinghand(self.drawpile.cardarray)
        
        self.Player2.createstartinghand(self.drawpile.cardarray)
        print(len(self.drawpile.cardarray))
        print(len(self.Player1.cardarray))
        print(len(self.Player2.cardarray))

    def startgame(self) -> None:
        pass
    def isgameover(self) -> bool:
        pass
    def endTurn(self) -> None:
        pass
    def Changeturn(self) -> None:
        pass
    def endgame(self) -> None:
        pass
    