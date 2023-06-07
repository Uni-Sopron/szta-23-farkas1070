import random

from Abstractcardpile import CardPile
from Expeditioncard import Expeditioncard
from Wagercard import Wagercard


class Drawpile(CardPile):
    def __init__(self, colors: list[str], numbers: list[int]) -> None:
        """
        init function for drawpile class. this will be the drawpile the players can yhoose from, it has 60 cards in it at the start


        Args:
            colors (list[str]): the list of colors used to generate the cards
            numbers (list[int]): the list of numbers used to generate the cards
        """
        super().__init__()

        for i in range(len(colors)):
            for _ in range(3):
                card = Wagercard(colors[i])
                self.cardarray.append(card)
        for i in range(len(numbers)):
            for j in range(len(colors)):
                anothercard = Expeditioncard(numbers[i], colors[j])
                self.cardarray.append(anothercard)

        print(self.cardarray)
        print(len(self.cardarray))

        self.shuffle()

    def shuffle(self) -> None:
        """
        shuffle the cards in the deck.
        """
        random.shuffle(self.cardarray)
