import random

from Abstractcardpile import CardPile
from Expeditioncard import Expeditioncard
from Wagercard import Wagercard


class Drawpile(CardPile):
    def __init__(self) -> None:
        """
        init function for drawpile class. this will be the drawpile the players can yhoose from, it has 60 cards in it at the start

        Member Variables:
            self.cardarray: the list variale of the cards.
            colors (list) = the colors that can be used for the cards
            numbers (list) = the numbers that can be used for the cards


        """
        super().__init__(14)
        self.cardarray = []
        colors = ["green", "white", "blue", "red", "yellow"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(len(colors)):
            for _ in range(3):
                card = Wagercard(colors[i])
                self.cardarray.append(card)
        for i in range(len(numbers)):
            for j in range(len(colors)):
                anothercard = Expeditioncard(numbers[i], colors[j])
                self.cardarray.append(anothercard)

        self.shuffle()

    def shuffle(self) -> None:
        """
        shuffle the cards in the deck.
        """
        random.shuffle(self.cardarray)
