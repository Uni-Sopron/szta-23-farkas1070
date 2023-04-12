from Abstractcardpile import CardPile
class Discardpile(CardPile):
    def __init__(self,pilenum):
        super().__init__(0)
        self.cardarray = []
        self.pilenum = pilenum
        
    def iscardpileempty(self) -> bool:
        return len(self.cardarray) == 0