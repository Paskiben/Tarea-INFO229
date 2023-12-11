class Telefono:
    def __init__(self) -> None:
        pass
    def llamar(self):
        print("lamando...")
    def ocupado(self):
        print("ocupado...")

class Camara:
    def __init__(self) -> None:
        pass
    def fotografia(self):
        print("tomando fotos..")

class Reproduccion:
    def __init__(self) -> None:
        pass
    def reproduccionDeMusica(self):
        print("reproduciendo musica")
    def reprdoducirVideo(self):
        print("reproducir un video...")

class smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print("telefono apagado")

movil = smartphone()
movil.llamar()