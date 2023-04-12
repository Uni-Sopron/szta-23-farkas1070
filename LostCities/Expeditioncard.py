class Expeditioncard():
    def __init__(self,value:int,color:str) -> None:
        self.value = value
        self.color = color
        
    def __str__(self) -> str:
        return f"MyClass object with color {self.color} and value {self.value}"