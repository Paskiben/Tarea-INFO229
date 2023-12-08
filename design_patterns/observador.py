# Definición de la clase Sujeto observable
class Inventario:
    def __init__(self):
        self._observadores = []
        self._productos = {}

    def agregar_observador(self, observador):
        self._observadores.append(observador)

    def eliminar_observador(self, observador):
        self._observadores.remove(observador)

    def agregar_producto(self, producto, cantidad):
        if producto in self._productos:
            self._productos[producto] += cantidad
        else:
            self._productos[producto] = cantidad
        self.notificar_observadores(producto, cantidad)

    def notificar_observadores(self, producto, cantidad):
        for observador in self._observadores:
            observador.actualizar(producto, cantidad)


# Definición de la clase Observador
class Comprador:
    def __init__(self, nombre):
        self._nombre = nombre

    def actualizar(self, producto, cantidad):
        print(f"El comprador {self._nombre} ha sido notificado: Se ha agregado {cantidad} unidades del producto {producto} al inventario.")


# Ejemplo de uso del patrón de observador
if __name__ == "__main__":
    inventario = Inventario()
    comprador1 = Comprador("Comprador1")
    comprador2 = Comprador("Comprador2")

    inventario.agregar_observador(comprador1)
    inventario.agregar_observador(comprador2)

    # Agregar productos al inventario
    inventario.agregar_producto("Camiseta", 50)
    inventario.agregar_producto("Pantalón", 30)
