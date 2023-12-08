# Componente interface
class Cafe:
    def get_cost(self):
        pass

    def get_ingredients(self):
        pass

# Componente concreto
class CafeSimple(Cafe):
    def get_cost(self):
        return 1.0

    def get_ingredients(self):
        return "Cafe"

# Decorador abstracto
class DecoradorCafe(Cafe):
    def __init__(self, cafe):
        self._cafe = cafe

    def get_cost(self):
        return self._cafe.get_cost()

    def get_ingredients(self):
        return self._cafe.get_ingredients()

# Decorador concreto
class Leche(DecoradorCafe):
    def __init__(self, cafe):
        super().__init__(cafe)

    def get_cost(self):
        return self._cafe.get_cost() + 0.5

    def get_ingredients(self):
        return self._cafe.get_ingredients() + ", Leche"

# Uso del patrón de decorador
if __name__ == "__main__":
    cafe_simple = CafeSimple()
    print(f"Cafe: {cafe_simple.get_ingredients()}, Costo: ${cafe_simple.get_cost()}")

    cafe_con_leche = Leche(cafe_simple)
    print(f"Cafe: {cafe_con_leche.get_ingredients()}, Costo: ${cafe_con_leche.get_cost()}")
