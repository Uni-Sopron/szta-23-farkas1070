from abc import ABC


class CardPile(ABC):
    def __init__(self, cardnum: int) -> None:
        """
        this is the abstract class for 3 of the different cardpiles.

        Args:
            cardnum (int): how many cards are there in the carpile.
        """

        self.cardnum = cardnum
        self.cardarray = [None] * cardnum

    def is_cardpile_empty(self) -> bool:
        """
        check if cardpile is empty.

        Returns:
            bool: true if empty false if not
        """
        return len(self.cardarray) == 0
