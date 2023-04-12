class Wagercard():
    def __init__(self,color:str) -> None:
        """
        wagercard. this kind of card has only a color attribute

        Args:
            color (str): _description_
        """
        self.color = color
    def __str__(self) -> str:
        """
        just like the expeditioncard we also have to write a string function so that we can get the color of the wagercard back

        Returns:
            str: the string we want.
            
        """
        return f"MyClass object with value {self.color}"