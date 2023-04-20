
from Drawpile import Drawpile
from Discardpile import Discardpile
import random
class Player():
    def __init__(self,name:str,number:int) -> None:
        """
        Player class object. there can be only 2 players

        Args:
            name (str): name of player
            number (int): number of player
            expeditionpoint (int): expeditionpoints of player

        Member variables:
            self.cardarray (list): the card array of the player
        """
        self.name = name
        self.number = number
        self.expeditionpoint = 0
        self.cardarray = []
    
    def create_starting_hand(self,other:Drawpile) -> None:
        """
        create starting deck of players from drawpile.

        Args:
            other (Drawpile): drawpile class instance
        Member variables:
            randomstartingarray (list) = the random starting aray that is generated
        """
        randomstartingarray= random.sample(other, k = 8)
        for card in randomstartingarray:
            if card in other:
                self.cardarray.append(card)
                other.remove(card)
        
        
    
    def draw_card(self,other:Drawpile) -> None:
        """
        Draw random card from drawpile class instance

        Args:
            other (Drawpile): drawpile
        """
        self.cardarray.append(random.choice(other))
        
    def discard_card(self,other:Discardpile) -> None:
        """
        discard card into one of the 5 discard cardpiles

        Args:
            other (Discardpile): discarpile instance
        """
        pass
    def play_card(self) ->None:
        """
        play card which means the choosen card will be placed in one of the players's playercardpiles class instances
        """
        pass


        