from Discardpile import Discardpile
from Drawpile import Drawpile
from Player import Player
from Playercardpile import Playercardpile


class Game:
    def __init__(self) -> None:
        """The game class. Here every other class will be made and the game itself will be written


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
            self.current_round (int): which round are we currently in.
            self.MAXROUNDS (int): 3 max rounds in game
            self.current_player (Player): the current player


        """

        self.MAXROUNDS = 3
        self.current_round = 1

        self.Player1 = Player(1)
        self.Player2 = Player(2)

        self.current_player = (
            self.Player1 if self.Player1.age > self.Player2.age else self.Player2
        )

        self.drawpile = Drawpile()

        self.discardpiles = [Discardpile() for _ in range(5)]
        self.player1_piles = [Playercardpile(1) for _ in range(5)]
        self.player2_piles = [Playercardpile(2) for _ in range(5)]
        for _ in range(8):
            self.Player1.draw_card_from_drawpile(self.drawpile.cardarray)
            self.Player2.draw_card_from_drawpile(self.drawpile.cardarray)

        print(len(self.Player1.cardarray))

        print(len(self.Player2.cardarray))
        print(len(self.drawpile.cardarray))
        print(self.drawpile.is_cardpile_empty())

    def draw_card_from_drawpile(self, other: Drawpile, player: Player) -> None:
        """
        Draw random card from drawpile class instance

        Args:
            other (Drawpile): “Card deck to draw cards from”
        """
        if len(other) == 0:
            print(
                "you cannot draw from this pile, because there are no cards to draw from"
            )
        else:
            card = other[-1]
            player.cardarray.append(card)
            other.remove(card)

    def draw_card_from_discardpile(self, other: Discardpile, player: Player) -> None:
        """
        Daw from one of the discardpiles. you can only draw the top card.

        Args:
            other (Discardpile): “Card deck to draw cards from”
        """
        if len(other) == 0:
            print(
                "you cannot draw from this pile, because there are no cards to draw from"
            )
        else:
            card = other[-1]
            player.cardarray.append(card)
            other.remove(card)

    def discard_card(self, other: Discardpile, player: Player) -> None:
        """
        The function used to discard a specific player's card

        Args:
            other (Discardpile): the chosen discardpile that the player wants to discard their card onto
            player (Player): The current player
        """
        choice_str = input(
            "here are your cards, choose which one you want to discard: "
        )
        choice = int(choice_str)
        for i in range(len(player.cardarray)):
            print(f"{i +1}. card: {player.cardarray[i]}")
        if choice <= 0 or choice > len(player.cardarray):
            print("bad choice, choose again")
            choice_str = input()
            choice = int(choice_str)
        else:
            other.cardarray.append((player.cardarray[choice - 1]))
            player.cardarray.pop(choice - 1)

    def play_card(self, other: Playercardpile, player: Player) -> None:
        """
        The function used if the player wants to play their card

        Args:
            other (Playercardpile): the playercardpile which the player want to put their card on
            player (Player): the current player
        """
        pass

    def is_game_over(self) -> bool:
        """
        check if game is over

        Returns:
            bool: yes if game is over no if its not. game over if round 3 has been completed
        """
        return self.current_round == self.MAXROUNDS

    def end_turn(self) -> None:
        """
        end players turn. this happens when the player draws a card
        """
        pass

    def change_turn(self) -> None:
        """
        changes the turn which means that the self.currentplayer variable will be changed to the other player
        """

    def end_game(self) -> None:
        """
        here every scoring things will be calculated
        """
        pass

    def game(self) -> None:
        """
        start game function.

        """

        while self.current_round != self.MAXROUNDS:
            while not self.drawpile.is_cardpile_empty():
                # itt indul majd a game
                pass
