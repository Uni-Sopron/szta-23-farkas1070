
from Drawpile import Drawpile
from Discardpile import Discardpile
from Playercardpile import Playercardpile
import random


class Player():
    def __init__(self, name: str, number: int) -> None:
        """
        Player class object. there can be only 2 players

        Args:
            name (str): name of player
            number (int): number of player
            expeditionpoint (int): expeditionpoints of player

        Member variables:
            self.cardarray (list): the card array of the player
        """
        self.name = name
        self.number = number
        self.expeditionpoint = 0
        self.cardarray = []

    def draw_card_from_drawpile(self, other: Drawpile) -> None:
        """
        Draw random card from drawpile class instance

        Args:
            other (Drawpile): “Card deck to draw cards from”
        """
        if len(other) == 0:
            print("you cannot draw from this pile, because there are no cards to draw from")
        else:
            card = random.choice(other)
            self.cardarray.append(card)
            other.remove(card)

    def draw_card_from_discardpile(self, other: Discardpile) -> None:
        """
        Daw from one of the discardpiles. you can only draw the top card.

        Args:
            other (Discardpile): “Card deck to draw cards from”
        """
        if len(other) == 0:
            print("you cannot draw from this pile, because there are no cards to draw from")
        else:
            card = other[-1]
            self.cardarray.append(card)
            other.remove(card)

    def discard_card(self, other: Discardpile) -> None:
        """
        discard card into one of the 5 discard cardpiles

        Args:
            other (Discardpile): discarpile instance
        """
        pass

    def play_card(self, other: Playercardpile) -> None:
        """_summary_

        Args:
            other (Playercardpile): The playercardpile instance that the player want to place the card onto
        """
        pass
