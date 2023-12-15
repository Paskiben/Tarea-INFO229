from pygame import *
from moviepy.editor import VideoFileClip
import sys
from Tools.Env import *

class VentanaConfig:
    def __init__(self):
        self.width = 300
        self.height = 200
        self.ventana_config = Surface((self.width, self.height))
        self.ventana_config.fill((200, 200, 200))

        self.color_boton = (0, 128, 255)
        self.boton_easy = Rect(50, 50, 200, 50)
        self.boton_normal = Rect(50, 110, 200, 50)
        self.boton_hard = Rect(50, 170, 200, 50)
        self.boton_custom = Rect(50, 230, 200, 50)

    def dibujar(self, ventana):
        draw.rect(self.ventana_config, self.color_boton, self.boton_easy)
        draw.rect(self.ventana_config, self.color_boton, self.boton_normal)
        draw.rect(self.ventana_config, self.color_boton, self.boton_hard)
        draw.rect(self.ventana_config, self.color_boton, self.boton_custom)

        ventana.blit(self.ventana_config, ((win_width - self.width) // 2, (win_height - self.height) // 2))

class ConfigButton:
    def __init__(self):
        self.botonConfig = Rect(50, 50, 200, 50)
    

def main():
    init()
    win_width = 640
    win_height = 720
    ventana = display.set_mode((win_width, win_height))
    display.set_caption("Buscaminas")

    ruta_icono = "cutebomb.png"
    icono = image.load(ruta_icono)
    display.set_icon(icono)

    ruta_gif = "giphy.gif"
    clip = VideoFileClip(ruta_gif)

    frames = [transform.scale(image.fromstring(frame.tostring(), clip.size, "RGB"), (win_width, win_height)) for frame in clip.iter_frames()]

    ruta_barra_lateral = "barra.png"
    barra_lateral = image.load(ruta_barra_lateral)
    barra_lateral = transform.scale(barra_lateral, (win_width,win_height))

    ruta_iconos = "icons.png"
    icon_bar = image.load(ruta_iconos)
    icon_bar = transform.scale(icon_bar, (win_width, win_height))

    frame_rate = clip.fps

    boton_configuracion = Rect(50, 300, 200, 50)
    color_boton_principal = (255, 0, 0)

    ventana_config = VentanaConfig()
    ventana_config_open = False

    clock = time.Clock()

    while True:
        for event in event.get():
        if (event.type == QUIT):
            quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if boton_configuracion.collidepoint(event.pos):
                    ventana_config_open = not ventana_config_open
                    mouse.set_visible(not ventana_config_open)

        frame_actual = int(time.get_ticks() * frame_rate / 1000) % len(frames)

        ventana.blit(frames[frame_actual], (0,0))

        ventana.blit(barra_lateral, (0,0))

        ventana.blit(icon_bar, (0,0))

        if (ventana_config_open):
            ventana_config.dibujar(ventana_config.ventana_config)
        else:
            frame_actual = int(time.get_ticks() * frame_rate / 1000) % len(frames)
            ventana.blit(frames[frame_actual], (0, 0))
            ventana.blit(barra_lateral, (0, 0))
            ventana.blit(icon_bar, (0, 0))
            draw.rect(ventana, color_boton_principal, boton_configuracion)

        display.flip()

        clock.tick_busy_loop(60)

main()
