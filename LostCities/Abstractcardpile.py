from abc import ABC, abstractmethod
class CardPile(ABC):
    def __init__(self,wagercard,expeditioncard,cardnum):
        self.wagercard = wagercard
        self.expeditioncard = expeditioncard
        self.cardnum = cardnum
    
 
