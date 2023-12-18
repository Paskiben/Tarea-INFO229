import pygame
import pygame_gui
from moviepy.editor import VideoFileClip
from Game.Juego import *

#-------------------------------------------------------------------------------#

#                              COMENTARIOS
#         |) image_x = pygame.image.load(ruta_imagen) -> cargar imagen
#         |) image_x = pygame.transform.scale(image_x, (w,h)) -> rescalar imagen
#         |) rectangulo_image_x -> crear rectangulo que luego servira como boton sobre la imagen.
#         |) frames -> cargar gif con ayuda de la biblioteca VideoFileClip de moviepy.
#         |) pygame.mixer.init(), esto se usara para el Sound, reproduce sonidos importados con pygame.mixer.Sound(ruta_sonido).
#         |) manager -> usa un json para estilos y este manejara mas adelante gracias al UITextEntryLine, las cajas de texto en la ventana config.
#         |) En el while True se manejan otros dos sub-whiles para cambiar entre pantalla de juego a pantalla de configuracion.
#         |) La funcion draws_lider() se encarga de dibujar y controlar el slider que se ve en la pantalla de configuracion.
#         |) La funcion dibujar_tablero() se encarga de dibujar el tablero de juego y actualizarlo constantemente.

#--------------------------------------------------------------------------------#


class GUI:
    blanco = (254, 174, 126)
    negro = (254, 126, 185)
    gris = (2, 200, 200)

    slider_value = 2
    font = pygame.font.Font(None, 36)

    def __init__(self):
        self.game = Juego()
        pygame.mixer.init()
        self.dataPath = environ.get('PATH_DATA')
        factor= max(self.game.conf.width, self.game.conf.height)
        self.ancho_celda = 500/factor
        self.alto_celda = 500/factor
        
        pygame.init()
        win_width = int(environ.get('WINDOW_WIDTH'))
        win_height = int(environ.get('WINDOW_HEIGHT'))
        self.ventana = pygame.display.set_mode((win_width, win_height))
        pygame.display.set_caption("Buscaminas")

        self.lose_sound = pygame.mixer.Sound(self.dataPath+"sounds/lose_sound.wav")
        self.lose_sound.set_volume(0.5)
        self.won_sound = pygame.mixer.Sound(self.dataPath+"sounds/won_sound.wav")
        self.won_sound.set_volume(0.3)
        reveal_sound = pygame.mixer.Sound(self.dataPath+"sounds/reveal_sound.wav")
        reveal_sound.set_volume(0.5)
        difficulty_change_sound = pygame.mixer.Sound(self.dataPath+"sounds/difficulty_change_sound.wav")
        difficulty_change_sound.set_volume(0.5)
        flag_sound = pygame.mixer.Sound(self.dataPath+"sounds/flag_sound.wav") 
        flag_sound.set_volume(0.5)
        button_sound = pygame.mixer.Sound(self.dataPath+"sounds/button_sound.wav")
        button_sound.set_volume(0.5)

        manager = pygame_gui.UIManager((win_width, win_height), self.dataPath+'theme.json')

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
        imagen_boton_reinicio = pygame.transform.scale(imagen_boton_reinicio, (60, 60))  
    
        rectangulo_boton_reinicio = imagen_boton_reinicio.get_rect()
        rectangulo_boton_reinicio.center = (win_width // 2, 40)

        imagen_boton_exit = pygame.image.load(self.dataPath+"exit.png")
        imagen_boton_exit = pygame.transform.scale(imagen_boton_exit, (60, 60))  
        
        rectangulo_boton_exit = imagen_boton_exit.get_rect()
        rectangulo_boton_exit.center = (win_width-40, 40)

        imagen_boton_return = pygame.image.load(self.dataPath+"return.png")
        imagen_boton_return = pygame.transform.scale(imagen_boton_return, (60,60))

        rectangulo_boton_return = imagen_boton_return.get_rect()
        rectangulo_boton_return.center = (40, 40)

        imagen_boton_config = pygame.image.load(self.dataPath+"config.png")
        imagen_boton_config = pygame.transform.scale(imagen_boton_config, (60, 60))  
    
        rectangulo_boton_config = imagen_boton_config.get_rect()
        rectangulo_boton_config.center = (40, 40)

        dif_1 = pygame.image.load(self.dataPath+"easy.png")
        dif_2 = pygame.image.load(self.dataPath+"normal.png")
        dif_3 = pygame.image.load(self.dataPath+"expert.png")

        imagen_boton_custom = pygame.image.load(self.dataPath+"custom_button.png")
        rectangulo_boton_custom = imagen_boton_custom.get_rect()
        rectangulo_boton_custom.center = (320,499)

        imagen_boton_okey = pygame.image.load(self.dataPath+"okey_button.png")
        rectangulo_boton_okey = imagen_boton_okey.get_rect()
        rectangulo_boton_okey.center = (320,667)

        imagen_star = pygame.image.load("data/star.png")
        imagen_won_star = pygame.image.load(self.dataPath+"win_star.png")
        imagen_lose_star = pygame.image.load(self.dataPath+"lose_star.png")

        cuadro_alto = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((150, 550), (100, 40)), 
            manager=manager, 
            placeholder_text="Alto",
            object_id="custom_text_entry",
        )

        cuadro_ancho = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((270, 550), (100, 40)), 
            manager=manager, placeholder_text="Ancho",
        )

        cuadro_bombas = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((390, 550), (100, 40)), 
            manager=manager, placeholder_text="N° bombas",
        )

        cuadro_ancho.set_allowed_characters('numbers')
        cuadro_alto.set_allowed_characters('numbers')
        cuadro_bombas.set_allowed_characters('numbers')

        frame_rate = clip.fps

        cursor_rect = pygame.Rect(0,0,50,50)

        ingame = True
        inconfig = False

        custom_visible = False

        font = pygame.font.Font(None, 56)

        start_time = pygame.time.get_ticks()

        clock = pygame.time.Clock()
        
        while True:
            while ingame:
                for evento in pygame.event.get():
                    if (evento.type == pygame.QUIT):
                        pygame.quit()
                        exit()
                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        
                        if(evento.button == 1):
                            if rectangulo_boton_reinicio.collidepoint(evento.pos):
                                pygame.mixer.Sound.play(button_sound)
                                self.game.iniciarJuego(self.game.conf)
                                self.game.vivo=True
                                start_time = pygame.time.get_ticks()
                            elif rectangulo_boton_exit.collidepoint(evento.pos):
                                pygame.mixer.Sound.play(button_sound)
                                pygame.quit()
                                exit()
                            elif rectangulo_boton_config.collidepoint(evento.pos):
                                pygame.mixer.Sound.play(button_sound)
                                inconfig = True
                                ingame = False
                                paused_time = pygame.time.get_ticks() - start_time
                            for fila in range(self.game.conf.height):
                                for columna in range(self.game.conf.width):
                                    rectangulo = pygame.Rect(columna * self.ancho_celda + 70, fila * self.alto_celda + 110, self.ancho_celda, self.alto_celda)
                                    if(self.game.vivo):
                                        if (rectangulo.collidepoint(evento.pos) and (not self.game.tablero.mapa[columna*self.game.conf.height+fila].marca)):
                                            pygame.mixer.Sound.play(reveal_sound)
                                            self.game.revelar_celda(fila, columna)
                                            self.reaccion()
                                    
                        elif(evento.button == 3):
                            for fila in range(self.game.conf.height):
                                for columna in range(self.game.conf.width):
                                    rectangulo = pygame.Rect(columna * self.ancho_celda + 70, fila * self.alto_celda + 110, self.ancho_celda, self.alto_celda)
                                    if(self.game.vivo):
                                        if (rectangulo.collidepoint(evento.pos) and (not self.game.tablero.mapa[columna*self.game.conf.height+fila].descubierta)):
                                            pygame.mixer.Sound.play(flag_sound)
                                            if(self.game.tablero.mapa[columna*self.game.conf.height + fila].marca):
                                                self.game.tablero.mapa[columna*self.game.conf.height + fila].marcar 
                                                self.game.marcadas -= 1
                                            elif(self.game.conf.mines - self.game.marcadas > 0):
                                                self.game.tablero.mapa[columna*self.game.conf.height + fila].marcar  
                                                self.game.marcadas += 1     

                if (self.game.vivo):
                    time = pygame.time.get_ticks()
                formatted_time = "{:02}:{:02}".format(
                     (time-start_time) // 60000,  (time-start_time) % 60000 //1000
                )

                frame_actual = int(pygame.time.get_ticks() * frame_rate / 1000) % len(frames)

                self.ventana.blit(frames[frame_actual], (0,0))
                self.ventana.blit(barra_lateral, (0,0))
                self.ventana.blit(icon_bar, (0,0))
                self.ventana.blit(imagen_boton_reinicio, rectangulo_boton_reinicio)
                self.ventana.blit(imagen_boton_exit, rectangulo_boton_exit)
                self.ventana.blit(imagen_boton_config, rectangulo_boton_config)

                bombs_ammount = font.render((str(self.game.conf.mines - self.game.marcadas)), True, (254,126,185))
                self.ventana.blit(bombs_ammount, (560,654))

                if(not self.game.win and self.game.vivo):
                    self.ventana.blit(imagen_star, (275, 625))
                elif(self.game.win and not self.game.vivo):
                    
                    self.ventana.blit(imagen_won_star, (275, 625))
                elif(not self.game.win and not self.game.vivo):
                    
                    self.ventana.blit(imagen_lose_star, (275, 625))

                self.dibujar_tablero()

                text = font.render(formatted_time, True, (254, 126, 185))
            
                self.ventana.blit(text, (115, 654)) 

                pygame.display.flip()

                clock.tick_busy_loop(60)
            
            while inconfig:
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if(event.button == 1):
                            if(rectangulo_boton_return.collidepoint(event.pos)):
                                inconfig = False
                                ingame = True
                                start_time = pygame.time.get_ticks() - paused_time
                                pygame.mixer.Sound.play(button_sound)
                            elif(rectangulo_boton_exit.collidepoint(event.pos)):
                                pygame.mixer.Sound.play(button_sound)
                                pygame.quit()
                                exit()
                            elif(rectangulo_boton_custom.collidepoint(event.pos)):
                                pygame.mixer.Sound.play(button_sound)
                                custom_visible = not custom_visible
                                cuadro_alto.visible = custom_visible
                                cuadro_ancho.visible = custom_visible
                                cuadro_bombas.visible = custom_visible
                            elif(rectangulo_boton_okey.collidepoint(event.pos)):
                                pygame.mixer.Sound.play(button_sound)
                                if(custom_visible):
                                    alto = int(cuadro_alto.get_text()) if (cuadro_alto.get_text() !=  '') else 5
                                    ancho = int(cuadro_ancho.get_text()) if (cuadro_ancho.get_text() !=  '') else 5
                                    bombas = int(cuadro_bombas.get_text()) if (cuadro_bombas.get_text() !=  '') else 1
                                else:
                                    if(self.slider_value == 1):
                                        alto, ancho, bombas = (10, 10, 10)
                                    elif(self.slider_value == 2):
                                        alto, ancho , bombas = (18, 18, 40)
                                    elif(self.slider_value == 3):
                                        alto, ancho, bombas = (24, 24, 99)
                                self.game.iniciarJuego(Configuracion(int(alto),int(ancho),int(bombas)))
                                factor= max(self.game.conf.width, self.game.conf.height)
                                self.ancho_celda = 500/factor
                                self.alto_celda = 500/factor
                                inconfig = False
                                ingame = True
                                start_time = pygame.time.get_ticks()
                            x, y = event.pos
                            self.slider_value
                            if(65 <= x <= 193 and 195 <= y <= 317):
                                pygame.mixer.Sound.play(difficulty_change_sound)
                                self.slider_value = 1
                            elif(193 <= x <= 448 and 195 <= y <= 317):
                                pygame.mixer.Sound.play(difficulty_change_sound)
                                self.slider_value = 2
                            elif(448 <= x <= 575 and 195 <= y <= 317):
                                pygame.mixer.Sound.play(difficulty_change_sound)
                                self.slider_value = 3   
                    manager.process_events(event)
                
                frame_actual = int(pygame.time.get_ticks() * frame_rate / 1000) % len(frames)

                self.ventana.blit(frames[frame_actual], (0,0))

                self.ventana.blit(barra_lateral, (0,0))
                self.ventana.blit(imagen_boton_custom, rectangulo_boton_custom)
                self.ventana.blit(imagen_boton_okey, rectangulo_boton_okey)
                self.ventana.blit(imagen_boton_exit, rectangulo_boton_exit)
                self.ventana.blit(imagen_boton_return, rectangulo_boton_return)
                
                if custom_visible:
                    manager.update(1 / 60.0)
                    manager.draw_ui(self.ventana)

                if(self.slider_value == 1):
                    self.ventana.blit(dif_1, (68,186))
                elif(self.slider_value == 2):
                    self.ventana.blit(dif_2, (284, 186))
                elif(self.slider_value == 3):
                    self.ventana.blit(dif_3, (492, 180))

                self.draw_slider(self.slider_value, cursor_rect)
                pygame.display.flip()
                
                clock.tick_busy_loop(60)         

    def draw_slider(self, slider_value, cursor_rect):
        
        barra = pygame.image.load(self.dataPath+"level_bar.png")
        indicador = pygame.image.load(self.dataPath+"cursor_bar.png")

        self.ventana.blit(barra, (0,0))

        indicador_x = 280
        if(slider_value == 1):
            indicador_x = 64
        elif(slider_value == 2):
            indicador_x = 280
        elif(slider_value == 3):
            indicador_x = 496
        indicador_y = 248

        self.ventana.blit(indicador, (indicador_x, indicador_y))



    def reaccion(self):
        if (not self.game.win and not self.game.vivo):
            self.dibujar_tablero()
            pygame.mixer.Sound.play(self.lose_sound)
        elif (self.game.win):
                    pygame.mixer.Sound.play(self.won_sound)

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

                
                
                if (self.game.tablero.mapa[index].marca):
                    self.ventana.blit(bandera, (x,y))
                elif (self.game.tablero.mapa[index].descubierta):
                    if self.game.tablero.mapa[index].valor == -1:
                        self.ventana.blit(bomba, (x,y))
                    elif self.game.tablero.mapa[index].valor != 0:
                        icono_imagen = pygame.image.load(self.dataPath+str(self.game.tablero.mapa[index].valor)+'.png')
                        icono_imagen = pygame.transform.scale(icono_imagen, (self.ancho_celda, self.alto_celda))
                        self.ventana.blit(icono_imagen , (x,y))
                else:
                    self.ventana.blit(casilla_no_revelada, (x,y))
GUI()