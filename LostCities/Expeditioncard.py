class Expeditioncard():
    def __init__(self,value:int,color:str) -> None:
        """
        init function for expeditioncartd class. this is the card type that has values as well.


        Args:
            value (int): value of card
            color (str): color of card
        """
        self.value = value
        self.color = color
        
    def __str__(self) -> str:
        """
        str function so that values and colors can be displayed nicely

        Returns:
            str: the str we want
        """
        return f"MyClass object with color {self.color} and value {self.value}"