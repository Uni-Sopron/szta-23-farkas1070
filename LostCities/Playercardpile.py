from Abstractcardpile import CardPile


class Playercardpile(CardPile):
    EXPEDITIONCOST = 20

    def __init__(self, playernum: int) -> None:
        """
        playercardpile class. both players have 5 playercardpiles

        Args:
            pilenum (int): we have to differentiate them so we give these a number as well.

            playernum (int): the player's number because we also have to differentiate which player'S playercardpile is this
        Member variables:
            self.expeditioncost (int) =the cost of the expedition
            self.sum (int) = the sum of the pile that will be calculated end of each round
            self.wagercount (int) = the amount of wagercards.
            self.result (int) = the final result in a number of the points in 1 column

        """
        super().__init__(0)

        self.playernum = playernum
        self.sum = 0
        self.wagercount = 0
        self.result = 0

    def calculate_sum(self) -> int:
        """
        calculate the sum for the playercardpile. this will be integral for the scoring.

        Returns:
            int: the sum of the player's cards
        """
        # calculation not done yet, I'm just returning the sum in itself so mypy doesn't give errors
        return self.sum

    def calculate_result(self) -> int:
        """
        returns the calculated result for the playercardpile. this will be integral for the scoring

        Returns:
            int: the result score
        """
        # calculation not done yet, I'm just returning the result in itself so mypy doesn't give errors
        return self.result
