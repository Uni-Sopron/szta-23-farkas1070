from abc import ABC
from typing import List, Union

from .Expeditioncard import Expeditioncard
from .Wagercard import Wagercard


class CardPile(ABC):
    def __init__(self) -> None:
        """
        this is the abstract class for 3 of the different cardpiles.

        Member Variables:
            - self.cardarray (list[Union[Wagercard, Expeditioncard]]): list of cards
        """

        self.cardarray: List[Union[Wagercard, Expeditioncard]] = []

    def is_cardpile_empty(self) -> bool:
        """
        check if cardpile is empty.

        Returns:
            bool: true if empty false if not
        """
        return len(self.cardarray) == 0
