
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

    def is_cardpile_empty(self) -> bool:
        """
        check if cardpile is empty. if yes expeditioncost will be 0

        Returns:
            bool: true if empty false if not
        """
        return len(self.cardarray) == 0

    def create_Pile(self) -> None:
        """
        create the piles.
        """
        pass

    def change_wager_card_num(self) -> None:
        """
        we have to check how many wagercards are there in every single playercardpile so we chnage number for them here.
        """
        pass

    def calculate_sum(self) -> int:
        """
        calculate the sum for the playercardpile. this will be integral for the scoring.

        Returns:
            int: _description_
        """
        pass

    def calculate_result(self) -> int:
        """returns the calculated result for the playercardpile. this will be integral for the scoring

        Returns:
            int: the result score
        """

        pass

    def calculate_8_cardbonus(self) -> None:
        """
        if there are 8 cards in a carpile, then you have to add an 8cardbonus to the result sum.
        """
        pass
