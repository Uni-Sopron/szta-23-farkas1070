from Abstractcardpile import CardPile
class Discardpile(CardPile):
    def __init__(self,pilenum:int) ->None:
        """
        init function of the discardpile class. This class will have 5 instances of it

        Args:
            pilenum (int): because there are 5 discardpiles we need to differentiate them somehow, so this variable will solve that
       

        """
        super().__init__(0)
        self.cardarray = []
        self.pilenum = pilenum
        
    def iscardpileempty(self) -> bool:
        """Check if cardpile is empty

        Returns:
            bool: true if empty, false if not
        """
        return len(self.cardarray) == 0