import pygame
import sys

def creaVentana():
    pygame.init()
    win_width = 500
    win_height = 700
    ventana = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Buscaminas")

while True:
    for event in pygame.event.get():
    if (event.type == pygame.QUIT):
        pygame.quit()
        sys.exit()


pygame.display.flip()