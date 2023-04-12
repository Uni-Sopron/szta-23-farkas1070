class Wagercard():
    def __init__(self,color:str) -> None:
        self.color = color
    def __str__(self) -> str:
        return f"MyClass object with value {self.color}"