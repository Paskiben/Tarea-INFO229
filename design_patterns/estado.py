# Contexto
class Conexion:
    def __init__(self) -> None:
        self.estado = EstadoCerrado()

    def solicitar(self) -> None:
        self.estado.manipular()

    def transicion_estado(self, estado_nuevo) -> None:
        self.estado = estado_nuevo

# Estados
class EstadoCerrado:
    def manipular(self) -> None:
        print("Error! La conexión está cerrada.")

class EstadoAbriendo:
    def manipular(self) -> None:
        print("Abriendo la conexión.")

class EstadoAbierto:
    def manipular(self) -> None:
        print("La conexión está abierta. Realizando operaciones.")

class EstadoCerrando:
    def manipular(self) -> None:
        print("Cerrando la conexión.")

# Uso del patrón State
if __name__ == "__main__":
    conexion = Conexion()
    conexion.solicitar()

    conexion.transicion_estado(EstadoAbriendo())
    conexion.solicitar()

    conexion.transicion_estado(EstadoAbierto())
    conexion.solicitar()

    conexion.transicion_estado(EstadoCerrando())
    conexion.solicitar()
