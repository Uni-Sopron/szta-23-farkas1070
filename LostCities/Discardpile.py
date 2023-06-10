from .Abstractcardpile import CardPile


class Discardpile(CardPile):
    def __init__(self, color: str) -> None:
        """
        init function of the discardpile class. This class will have 5 instances of it

        Args:
            color (str): color of the discardpile (can be 5 different colors)


        """
        self.color = color
        super().__init__()

    def print_last_element(self, index: int) -> None:
        if len(self.cardarray) == 0:
            print(f"{self.color} Pile üres, erről nem tudsz húzni")
        else:
            print(
                f" {index} {self.color} oszlopról ezt tudod húzni: {self.cardarray[-1]}"
            )
