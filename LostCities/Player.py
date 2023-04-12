
from Drawpile import Drawpile
from Discardpile import Discardpile
import random
class Player():
    def __init__(self,name:str,number:int,expeditionpoint:int) -> None:
        self.name = name
        self.number = number
        self.expeditionpoint = expeditionpoint
        self.cardarray = []
    
    def createstartinghand(self,other:Drawpile) -> None:
        randomstartingarray= random.sample(other, k = 8)
        for card in randomstartingarray:
            if card in other:
                self.cardarray.append(card)
                other.remove(card)
        
        
    
    def Drawcard(self,other:Drawpile) -> None:
        self.cardarray.append(random.choice(other))
        
    def discardcard(self,other:Discardpile) -> None:
        pass
    def playcard(self) ->None:
        pass


        