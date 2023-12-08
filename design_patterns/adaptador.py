# Subsistema de reproducción de archivos mp3
class ReproductorMP3:
    def reproducir_mp3(self, archivo):
        return f"Reproduciendo archivo mp3: {archivo}"

# Interfaz estándar para el reproductor de audio
class ReproductorAudio:
    def reproducir(self, tipo, archivo):
        pass

# Adaptador para el reproductor de audio
class AdaptadorReproductorAudio(ReproductorAudio):
    def __init__(self, reproductor_mp3):
        self.reproductor_mp3 = reproductor_mp3

    def reproducir(self, tipo, archivo):
        if tipo == "mp3":
            return self.reproductor_mp3.reproducir_mp3(archivo)
        else:
            return f"Formato de archivo no compatible: {tipo}"

# Uso del patrón de adaptador en el contexto de un reproductor de audio
if __name__ == "__main__":
    reproductor_mp3 = ReproductorMP3()
    adaptador_audio = AdaptadorReproductorAudio(reproductor_mp3)

    print(adaptador_audio.reproducir("mp3", "cancion1.mp3"))  # Salida: Reproduciendo archivo mp3: cancion1.mp3
    print(adaptador_audio.reproducir("wav", "cancion2.wav"))  # Salida: Formato de archivo no compatible: wav
