from Wagercard import Wagercard
from Expeditioncard import Expeditioncard
from Abstractcardpile import CardPile
import random


class Drawpile(CardPile):
    def __init__(self) -> None:
        """
        init function for drawpile class. this will be the drawpile the players can yhoose from, it has 60 cards in it at the start

        Member Variables:
            self.cardarray: the list variale of the cards.
            colors (list) = the colors that can be used for the cards
            numbers (list) = the numbers that can be used for the cards


        """
        super().__init__(60)
        self.cardarray = []
        colors = ["green", "white", "blue", "red", "yellow"]
        numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        for i in range(len(colors)):
            for _ in range(3):
                card = Wagercard(colors[i])
                self.cardarray.append(card)
        for i in range(len(colors)):
            for j in range(len(numbers)):
                anothercard = Expeditioncard(colors[i], numbers[j])
                self.cardarray.append(anothercard)

    def is_cardpile_empty(self) -> bool:
        """
        check if cardpile is empty, if yes the round is over

        Returns:
            bool: yes if empty, false if not
        """
        return len(self.cardarray) == 0

    def shuffle(self) -> None:
        """
        shuffle the cards in the deck.
        """
        random.shuffle(self.cardarray)
