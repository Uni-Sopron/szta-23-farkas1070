class Expeditioncard():
    def __init__(self,value,color):
        self.value = value
        self.color = color
        
    def __str__(self):
        return f"MyClass object with color {self.color} and value {self.value}"