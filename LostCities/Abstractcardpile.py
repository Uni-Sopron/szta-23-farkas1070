from abc import ABC, abstractmethod
from Wagercard import Wagercard
from Expeditioncard import Expeditioncard

class CardPile(ABC):
    def __init__(self,cardnum:int) -> None:
        """
        this is the abstract class for 3 of the different cardpiles.

        Args:
            cardnum (int): how many cards are there in the carpile.
        """
        
        self.cardnum = cardnum
        self.cardarray = [None] * cardnum

    
    @abstractmethod
    def iscardpileempty(self) -> bool:
        """
        check if cardpile is empty.

        Returns:
            bool: true if empty false if not
        """
        pass
 
