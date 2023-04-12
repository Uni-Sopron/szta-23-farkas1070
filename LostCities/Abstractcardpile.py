from abc import ABC, abstractmethod
from Wagercard import Wagercard
from Expeditioncard import Expeditioncard

class CardPile(ABC):
    def __init__(self,cardnum:int) -> None:
        
        self.cardnum = cardnum
        self.cardarray = [None] * cardnum

    
    @abstractmethod
    def iscardpileempty(self) -> bool:
        pass
 
