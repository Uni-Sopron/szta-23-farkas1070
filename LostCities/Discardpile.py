from Abstractcardpile import CardPile


class Discardpile(CardPile):
    def __init__(self, color) -> None:
        """
        init function of the discardpile class. This class will have 5 instances of it

        Args:
            pilenum (int): because there are 5 discardpiles we need to differentiate them somehow, so this variable will solve that


        """
        self.color = color
        super().__init__(0)
