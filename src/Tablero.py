import os
from Env import *
from Celda import *
from Configuracion import *

class Tablero:
    def __init__(self, configuracion) -> None:
        self.mapa = [Celda(0) for i in range(configuracion.width*configuracion.height)]
    #Generar minas y sumar valor en celdas adiacentes


setEnv()
conf = Configuracion(int(os.environ.get('WIDTH')),int(os.environ.get('HEIGHT')),int(os.environ.get('MINES')))
new_mapa = Tablero(conf)
print(new_mapa.mapa[0].valor)