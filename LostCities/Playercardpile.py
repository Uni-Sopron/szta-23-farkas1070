
from Abstractcardpile import CardPile


class Playercardpile(CardPile):
    def __init__(self,pilenum:int,playernum:int) -> None:
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
        self.sum = 0
        self.pilenum=pilenum
        self.expeditioncost=20
        self.wagercount=0
        self.result =0
        self.playernum = playernum
        


    def iscardpileempty(self) -> bool:
        """
        check if cardpile is empty. if yes expeditioncost will be 0

        Returns:
            bool: true if empty false if not
        """
        return len(self.cardarray) == 0
    
    def createPile(self) -> None:
        """
        create the piles.
        """
        pass
    def changewagercardnum(self) -> None:
        """
        we have to check how many wagercards are there in every single playercardpile so we chnage number for them here.
        """
        pass
    
    def calculatesum(self) -> int:
        """
        calculate the sum for the playercardpile. this will be integral for the scoring.

        Returns:
            int: _description_
        """
        pass
    def calculate8cardbonus(self) -> None:
        """
        if there are 8 cards in a carpile, then you have to add an 8cardbonus to the result sum.
        """
        pass