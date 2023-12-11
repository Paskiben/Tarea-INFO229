import math
class Pastel:
    def __init__(self, ingredientes, porte) -> None:
        self.ingredientes = ingredientes
        self.porte = porte
    
    def __repr__(self) -> str:
        return (f"Pastel {self.ingredientes}, "f"{self.porte}")
    
    def radio(self):
        return self.porte_radio(self.porte)
    
    @staticmethod
    def porte_radio(radio):
        return radio**2*math.pi
    
pastel = Pastel(["harina", "leche", "azucar", "crema"],4)
print(pastel.radio())