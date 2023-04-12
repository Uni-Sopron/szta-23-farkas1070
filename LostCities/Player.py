
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
        randomstartingarray= random.choices(other, k = 8)
        for i in range(len(randomstartingarray)):
            self.cardarray.append(randomstartingarray[i])
            other.remove(randomstartingarray[i])
        
        
    
    def Drawcard(self,other:Drawpile) -> None:
        self.cardarray.append(random.choice(other))
        
    def discardcard(self,other:Discardpile) -> None:
        pass
    def playcard(self) ->None:
        pass


        