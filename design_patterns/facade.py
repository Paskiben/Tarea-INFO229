# Subsistemas
class Luces:
    def encender(self):
        print("Luces encendidas")

    def apagar(self):
        print("Luces apagadas")


class Sonido:
    def activar(self):
        print("Sonido activado")

    def desactivar(self):
        print("Sonido desactivado")


class Proyeccion:
    def reproducir(self):
        print("Proyección en curso")

    def detener(self):
        print("Proyección detenida")


# Fachada
class FachadaCine:
    def __init__(self):
        self.luces = Luces()
        self.sonido = Sonido()
        self.proyeccion = Proyeccion()

    def empezar_pelicula(self):
        self.luces.encender()
        self.sonido.activar()
        self.proyeccion.reproducir()

    def terminar_pelicula(self):
        self.luces.apagar()
        self.sonido.desactivar()
        self.proyeccion.detener()


# Uso del patrón de fachada
if __name__ == "__main__":
    fachada_cine = FachadaCine()
    fachada_cine.empezar_pelicula()
    # El cliente disfruta de la película
    fachada_cine.terminar_pelicula()
