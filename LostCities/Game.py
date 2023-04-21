
from Player import Player
from Drawpile import Drawpile
from Discardpile import Discardpile
from Playercardpile import Playercardpile


class Game():
    def __init__(self, maxrounds: int) -> None:
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

        self.Player1 = Player(input("add meg az első játékos nevét"), 1)
        self.Player2 = Player(input("add meg a második játékos nevét"), 2)
        self.drawpile = Drawpile()

        self.discardpiles = [Discardpile() for _ in range(5)]
        self.player1_piles = [Playercardpile(1) for _ in range(5)]
        self.player2_piles = [Playercardpile(2) for _ in range(5)]
        for _ in range(8):
            self.Player1.draw_card_from_drawpile(self.drawpile.cardarray)
            self.Player2.draw_card_from_drawpile(self.drawpile.cardarray)

        self.Player1.draw_card_from_discardpile(self.discardpiles[1].cardarray)
        print(len(self.Player1.cardarray))

        print(len(self.Player2.cardarray))
        print(len(self.drawpile.cardarray))

    def start_game(self) -> None:
        """
        start game function.

        """
        pass

    def is_game_over(self) -> bool:
        """
        check if game is over

        Returns:
            bool: yes if game is over no if its not. game over if round 3 has been completed
        """
        pass

    def end_turn(self) -> None:
        """
        end players turn. this happens when the player draws a card
        """
        pass

    def change_turn(self) -> None:
        """
        change turn
        """
        pass

    def end_game(self) -> None:
        """
        here every scoring things will be calculated
        """
        pass
