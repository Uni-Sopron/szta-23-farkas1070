from Abstractcardpile import CardPile
from Wagercard import Wagercard


class Playercardpile(CardPile):
    def __init__(self, color: str) -> None:
        """
        playercardpile class. both players have 5 playercardpiles

        Args:
            pilenum (int): we have to differentiate them so we give these a number as well.

        Member variables:
            self.expeditioncost (int) =the cost of the expedition
            self.sum (int) = the sum of the pile that will be calculated end of each round
            self.wagercount (int) = the amount of wagercards.
            self.result (int) = the final result in a number of the points in 1 column

        """
        super().__init__()
        self.color = color
        self.sum = 0
        self.wagercount = 0
        self.result = 0
        self.EXPEDITIONCOST = 20
        self.subtotal = 0

    def calculate_sum(self) -> None:
        """
        calculate the sum for the playercardpile. this will be integral for the scoring.

        Returns:
            int: the sum of the player's cards
        """

        for i in range(len(self.cardarray)):
            # check if the vaiable there is a wagercad
            if isinstance(self.cardarray[i], Wagercard):
                self.wagercount += 1
            else:
                self.sum += self.cardarray[i].value

    def calculate_result(self) -> int:
        """
        returns the calculated result for the playercardpile. this will be integral for the scoring

        Returns:
            int: the result score
        """

        self.calculate_sum()
        # we only subtract expeditioncost if there is at least 1 card
        if len(self.cardarray) > 0:
            self.subtotal = self.sum - self.EXPEDITIONCOST

        # if thre is 1 wagercard the multiplier is 2x, if there are 2 wagercards the multiplieris 3x etc...
        wager_multiplier = self.wagercount + 1
        self.result = self.subtotal * wager_multiplier
        # 8 card bonus
        if len(self.cardarray) > 8:
            self.result += 20

        return self.result
