from typing import List, Union

from Expeditioncard import Expeditioncard
from Wagercard import Wagercard


class Player:
    def __init__(self, number: int) -> None:
        """
        Player class object. there can be only 2 players

        Args:
            name (str): name of player
            number (int): number of player
            expeditionpoint (int): expeditionpoints of player

        Member variables:
            cardarray (List[Union[Wagercard, Expeditioncard]]): the card array of the player
        """
        self.number = number
        self.name = input(f"add meg a neved jatekos {self.number} :")
        self.age = input(f"add meg az életkorod játékos {self.number} :")

        self.expeditionpoint = 0
        self.cardarray: List[Union[Wagercard, Expeditioncard]] = []
