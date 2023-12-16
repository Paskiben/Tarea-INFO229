import pygame
from moviepy.editor import VideoFileClip
from random import randint
from Game.Juego import *
from math import sqrt

class GUI:
    blanco = (254, 174, 126)
    negro = (254, 126, 185)
    gris = (2, 200, 200)

    def __init__(self):
        self.game = Juego()
        self.dataPath = environ.get('PATH_DATA')
        self.vivo=True
        factor= max(self.game.conf.width, self.game.conf.height)
        self.ancho_celda = 500/factor
        self.alto_celda = 500/factor
        
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

        imagen_boton_reinicio = pygame.image.load(self.dataPath+"reload.png")
        imagen_boton_reinicio = pygame.transform.scale(imagen_boton_reinicio, (60, 60))  # Ajustar el tamaño según sea necesario
        # Definir el rectángulo del botón de reinicio
        rectangulo_boton_reinicio = imagen_boton_reinicio.get_rect()
        rectangulo_boton_reinicio.center = (win_width // 2, 40)

        imagen_boton_exit = pygame.image.load(self.dataPath+"exit.png")
        imagen_boton_exit = pygame.transform.scale(imagen_boton_exit, (60, 60))  # Ajustar el tamaño según sea necesario
        # Definir el rectángulo del botón de reinicio
        rectangulo_boton_exit = imagen_boton_exit.get_rect()
        rectangulo_boton_exit.center = (win_width-40, 40)

        imagen_boton_config = pygame.image.load(self.dataPath+"config.png")
        imagen_boton_config = pygame.transform.scale(imagen_boton_config, (60, 60))  # Ajustar el tamaño según sea necesario
        # Definir el rectángulo del botón de reinicio
        rectangulo_boton_config = imagen_boton_config.get_rect()
        rectangulo_boton_config.center = (40, 40)

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
                            if rectangulo_boton_reinicio.collidepoint(evento.pos):
                                self.game.iniciarJuego(self.game.conf)
                                self.vivo=True
                            elif rectangulo_boton_exit.collidepoint(evento.pos):
                                pygame.quit()
                                exit()
                                
                            for fila in range(self.game.conf.height):
                                for columna in range(self.game.conf.width):
                                    rectangulo = pygame.Rect(columna * self.ancho_celda + 70, fila * self.alto_celda + 110, self.ancho_celda, self.alto_celda)
                                    if(self.vivo):
                                        if (rectangulo.collidepoint(evento.pos) and (not self.game.tablero.mapa[columna*self.game.conf.height+fila].marca)):
                                            self.revelar_celda(fila, columna)
                                    
                        elif(evento.button == 3):
                            for fila in range(self.game.conf.height):
                                for columna in range(self.game.conf.width):
                                    rectangulo = pygame.Rect(columna * self.ancho_celda + 70, fila * self.alto_celda + 110, self.ancho_celda, self.alto_celda)
                                    if(self.vivo):
                                        if (rectangulo.collidepoint(evento.pos) and (not self.game.tablero.mapa[columna*self.game.conf.height+fila].descubierta)):
                                            self.game.tablero.mapa[columna*self.game.conf.height + fila].marcar      
                                    
            frame_actual = int(pygame.time.get_ticks() * frame_rate / 1000) % len(frames)

            self.ventana.blit(frames[frame_actual], (0,0))
            self.ventana.blit(barra_lateral, (0,0))
            self.ventana.blit(icon_bar, (0,0))
            self.ventana.blit(imagen_boton_reinicio, rectangulo_boton_reinicio)
            self.ventana.blit(imagen_boton_exit, rectangulo_boton_exit)
            self.ventana.blit(imagen_boton_config, rectangulo_boton_config)

            self.dibujar_tablero()

            pygame.display.flip()

            clock.tick_busy_loop(60)


    # Función para revelar celda
    def revelar_celda(self, fila, columna):
        # Marcar la celda como revelada
        index = columna*self.game.conf.height + fila
        if (self.game.tablero.mapa[index].valor == -1 and (not self.game.tablero.mapa[index].descubierta)):
            self.game.tablero.mapa[index].descubrir
            for i in self.game.tablero.mines:
                self.game.tablero.mapa[i].descubrir
            self.dibujar_tablero()
            self.vivo = False
            #Terminar esta cosa uwu
        elif (self.game.tablero.mapa[index].valor == 0 and (not self.game.tablero.mapa[index].descubierta)):
            self.game.tablero.mapa[index].descubrir
            for i in range(columna-1, columna+2):
                for j in range(fila-1, fila+2):
                    if ((i>=0 and j>=0 and i<self.game.conf.width and j<self.game.conf.height) and (self.game.tablero.mapa[i*self.game.conf.height+j].valor>0 or (i==columna or j==fila))): self.revelar_celda(j,i)
        else:
            self.game.tablero.mapa[index].descubrir

    # Función para dibujar el tablero en la pantall1a
    def dibujar_tablero(self):
        bomba = pygame.image.load(self.dataPath+"bomba.png")
        bomba = pygame.transform.scale(bomba, (self.ancho_celda, self.alto_celda))
        bandera = pygame.image.load(self.dataPath+'flag.png')
        bandera = pygame.transform.scale(bandera, (self.ancho_celda, self.alto_celda))
        casilla_no_revelada = pygame.image.load(self.dataPath+'casilla.png')
        casilla_no_revelada = pygame.transform.scale(casilla_no_revelada, (self.ancho_celda, self.alto_celda))
        for fila in range(self.game.conf.height):
            for columna in range(self.game.conf.width):
                x = columna * self.ancho_celda + 70
                y = fila * self.alto_celda + 110
                index = columna*self.game.conf.height + fila

                
                if (self.game.tablero.mapa[index].descubierta):
                    if self.game.tablero.mapa[index].valor == -1:
                        self.ventana.blit(bomba, (x,y))
                    elif self.game.tablero.mapa[index].valor != 0:
                        icono_imagen = pygame.image.load(self.dataPath+str(self.game.tablero.mapa[index].valor)+'.png')
                        icono_imagen = pygame.transform.scale(icono_imagen, (self.ancho_celda, self.alto_celda))
                        self.ventana.blit(icono_imagen , (x,y))
                elif (self.game.tablero.mapa[index].marca):
                    self.ventana.blit(bandera, (x,y))
                else:
                    self.ventana.blit(casilla_no_revelada, (x,y))
GUI()