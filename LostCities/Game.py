
from Player import Player
from Drawpile import Drawpile
from Discardpile import Discardpile
from Playercardpile import Playercardpile
class Game():
    def __init__(self, maxrounds:int) ->None:
        """The game class. Here every other class will be made and the game itself will be written

        Args:
            maxrounds (int): 3 max rounds in game
            self.roundnum (int): which round are we currently in.

        Member variables:
            self.Player1 (Player): player1
            self.Player2 (Player): player2
            self.drawpile (Drawpile): the drawpile of the game
            self.discardpile1 (Discardpile) = the first discardpile
            self.discardpile2 (Discardpile) = the second discardpile
            self.discardpile3 (Discardpile) = the third discardpile
            self.discardpile4 (Discardpile) = the fourth discardpile
            self.discardpile5 (Discardpile) = the fifth discardpile
            self.player1_piles (array) = player1-s playercardpiles
            self.player2_piles (array) = player2-s playercardpiles


        """
        
        self.maxrounds = maxrounds
        self.roundnum = 1
        
        
        
        self.Player1 = Player(input("add meg az első játékos nevét"),1,0)
        self.Player2 = Player(input("add meg a második játékos nevét"),2,0)
        self.drawpile = Drawpile()
        

        self.discardpile1 = Discardpile(1)
        self.discardpile2 = Discardpile(2)
        self.discardpile3 = Discardpile(3)
        self.discardpile4 = Discardpile(4)
        self.discardpile5 = Discardpile(5)
        self.player1_piles = [Playercardpile(i, 1) for i in range(5)]
        self.player2_piles = [Playercardpile(i, 2) for i in range(5)]
        
        self.Player1.createstartinghand(self.drawpile.cardarray)
        
        self.Player2.createstartinghand(self.drawpile.cardarray)
        print(len(self.drawpile.cardarray))
        print(len(self.Player1.cardarray))
        print(len(self.Player2.cardarray))
        print(len(self.player1_piles))
        print(len(self.player2_piles))

    def startgame(self) -> None:
        """
        start game function.
    
        """
        pass
    def isgameover(self) -> bool:
        """
        check if game is over

        Returns:
            bool: yes if game is over no if its not. game over if round 3 has been completed
        """
        pass
    def endTurn(self) -> None:
        """
        end players turn. this happens when the player draws a card
        """
        pass
    def Changeturn(self) -> None:

        """
        change turn
        """
        pass
    def endgame(self) -> None:
        """
        here every scoring things will be calculated
        """
        pass
    