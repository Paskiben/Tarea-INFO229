import pygame
from moviepy.editor import VideoFileClip
from random import randint
from Game.Juego import *


class GUI:
    blanco = (254, 174, 126)
    negro = (254, 126, 185)
    gris = (2, 200, 200)

    ancho_celda = 50
    alto_celda = 50

    def __init__(self):
        self.game = Juego()
        self.dataPath = environ.get('PATH_DATA')
        pygame.init()
        win_width = int(environ.get('WINDOW_WIDTH'))
        win_height = int(environ.get('WINDOW_HEIGHT'))
        self.ventana = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Buscaminas")

        ruta_icono = self.dataPath+"cutebomb.png"
        icono = pygame.image.load(ruta_icono)
        pygame.display.set_icon(icono)

        ruta_gif = self.dataPath+"giphy.gif"
        clip = VideoFileClip(ruta_gif)

        frames = [pygame.transform.scale(pygame.image.fromstring(frame.tostring(), clip.size, "RGB"), (win_width, win_height)) for frame in clip.iter_frames()]

        ruta_barra_lateral = self.dataPath+"barra.png"
        barra_lateral = pygame.image.load(ruta_barra_lateral)
        barra_lateral = pygame.transform.scale(barra_lateral, (win_width,win_height))

        ruta_iconos = self.dataPath+"icons.png"
        icon_bar = pygame.image.load(ruta_iconos)
        icon_bar = pygame.transform.scale(icon_bar, (win_width, win_height))

        frame_rate = clip.fps

        clock = pygame.time.Clock()

        while True:
            for evento in pygame.event.get():
                if (evento.type == pygame.QUIT):
                    pygame.quit()
                    exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    # Verificar si el jugador hizo clic en alguna celda
                        if(evento.button == 1):
                            for fila in range(self.game.conf.height):
                                for columna in range(self.game.conf.width):
                                    rectangulo = pygame.Rect(columna * self.ancho_celda + 70, fila * self.alto_celda + 110, self.ancho_celda, self.alto_celda)
                                    if rectangulo.collidepoint(evento.pos):
                                        self.revelar_celda(fila, columna)
                        elif(evento.button == 3):
                            for fila in range(self.game.conf.height):
                                for columna in range(self.game.conf.width):
                                    rectangulo = pygame.Rect(columna * self.ancho_celda + 70, fila * self.alto_celda + 110, self.ancho_celda, self.alto_celda)
                                    if rectangulo.collidepoint(evento.pos):
                                        self.game.tablero.mapa[columna*self.game.conf.height + fila].marcar

            frame_actual = int(pygame.time.get_ticks() * frame_rate / 1000) % len(frames)

            self.ventana.blit(frames[frame_actual], (0,0))
            self.ventana.blit(barra_lateral, (0,0))
            self.ventana.blit(icon_bar, (0,0))

            self.dibujar_tablero()

            pygame.display.flip()

            clock.tick_busy_loop(60)


    # Función para revelar celda
    def revelar_celda(self, fila, columna):
        # Marcar la celda como revelada
        index = columna*self.game.conf.height + fila
        self.game.tablero.mapa[index].descubrir
        print(self.game.tablero.mapa[index].valor)
        print(self.game.tablero.mapa[index].descubierta)
        if (self.game.tablero.mapa[index].valor == -1 and (not self.game.tablero.mapa[index].descubierta)):
            self.dibujar_tablero()
            #Terminar esta cosa uwu
        elif (self.game.tablero.mapa[index].valor == 0 and (not self.game.tablero.mapa[index].descubierta)):
            for i in range(columna-1, columna+2):
                for j in range(fila-1, fila+2):
                    if ((i>=0 and j>=0 and i<self.game.conf.heigth and j<self.game.conf.width)): self.revelar_celda(j,i)

    # Función para dibujar el tablero en la pantall1a
    def dibujar_tablero(self):
        bomba = pygame.image.load(self.dataPath+"bomba.png")
        bandera = pygame.image.load(self.dataPath+'flag.png')
        casilla_no_revelada = pygame.image.load(self.dataPath+'casilla.png')
        for fila in range(self.game.conf.height):
            for columna in range(self.game.conf.width):
                x = columna * self.ancho_celda + 70
                y = fila * self.alto_celda + 110
                index = columna*self.game.conf.height + fila

                if (self.game.tablero.mapa[index].marca):
                    self.ventana.blit(bandera, (x,y))
                elif (self.game.tablero.mapa[index].descubierta):
                    if self.game.tablero.mapa[index].valor == -1:
                        self.ventana.blit(bomba, (x,y))
                    elif self.game.tablero.mapa[index].valor != 0:
                        self.ventana.blit(pygame.image.load(self.dataPath+str(self.game.tablero.mapa[index].valor)+'.png') , (x,y))
                else:
                    self.ventana.blit(casilla_no_revelada, (x,y))
GUI()