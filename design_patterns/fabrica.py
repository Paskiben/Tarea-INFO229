# Clase de Producto
class Pizza:
    def preparar(self):
        pass

    def hornear(self):
        pass

    def cortar(self):
        pass

    def empacar(self):
        pass

# Clases de Producto Concretas
class PizzaVegetariana(Pizza):
    def preparar(self):
        print("Preparando la pizza vegetariana")

class PizzaPepperoni(Pizza):
    def preparar(self):
        print("Preparando la pizza de pepperoni")

# Clase de Fábrica
class Pizzeria:
    def crear_pizza(self, tipo):
        if tipo == "vegetariana":
            return PizzaVegetariana()
        elif tipo == "pepperoni":
            return PizzaPepperoni()
        else:
            return None

# Uso del Patrón de Fábrica
if __name__ == "__main__":
    pizzeria = Pizzeria()

    pizza_vegetariana = pizzeria.crear_pizza("vegetariana")
    pizza_vegetariana.preparar()
    pizza_vegetariana.hornear()
    pizza_vegetariana.cortar()
    pizza_vegetariana.empacar()

    pizza_pepperoni = pizzeria.crear_pizza("pepperoni")
    pizza_pepperoni.preparar()
    pizza_pepperoni.hornear()
    pizza_pepperoni.cortar()
    pizza_pepperoni.empacar()
