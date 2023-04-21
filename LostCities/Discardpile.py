from Abstractcardpile import CardPile


class Discardpile(CardPile):
    def __init__(self) -> None:
        """
        init function of the discardpile class. This class will have 5 instances of it

        Args:
            pilenum (int): because there are 5 discardpiles we need to differentiate them somehow, so this variable will solve that


        """
        super().__init__(0)

    def is_cardpile_empty(self) -> bool:
        """Check if cardpile is empty

        Returns:
            bool: true if empty, false if not
        """
        return len(self.cardarray) == 0
