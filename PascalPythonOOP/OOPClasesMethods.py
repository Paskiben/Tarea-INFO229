class Pastel:
    
    def __init__(self, ingredientes) -> None:
        self.ingredientes = ingredientes
    
    def __repr__(self) -> str:
        return f"pastel {self.ingredientes !r}"
    
    @classmethod
    def Pastel_chocolate(cls):
        return cls(["harina", "huevos", "leche", "chocolate"])
    
    @classmethod
    def Pastel_vainilla(cls):
        return cls(["harina", "huevos", "leche", "vainilla"])

print(Pastel.Pastel_chocolate())