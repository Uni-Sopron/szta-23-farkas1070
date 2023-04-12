
from Abstractcardpile import CardPile


class Playercardpile(CardPile):
    def __init__(self,pilenum:int,playernum:int) -> None:
        super().__init__(0)
        self.sum = sum
        self.pilenum=pilenum
        self.expeditioncost=20
        self.wagercount=0
        self.result =0
        self.playernum = playernum
        


    def iscardpileempty(self) -> bool:
        return len(self.cardarray) == 0
    
    def createPile(self) -> None:
        pass
    def changewagercardnum(self) -> None:
        pass
    
    def calculatesum(self) -> int:
        pass
    def calculate8cardbonus(self) -> None:
        pass