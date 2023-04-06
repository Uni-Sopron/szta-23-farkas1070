from Wagercard import Wagercard
from Expeditioncard import Expeditioncard
class Drawpile():
    def __init__(self):
        
        self.cardarray = []
        colors = ["green","white","blue","red","yellow"]
        numbers =[2,3,4,5,6,7,8,9,10]
        for i in range(len(colors)):
            for _ in range(3):
                card = Wagercard(colors[i])
                self.cardarray.append(card)
        for i in range(len(colors)):
            for j in range(len(numbers)):
                anothercard = Expeditioncard(colors[i],numbers[j])
                self.cardarray.append(anothercard)
        
                
                
        
            