import os
from Env import *
from Celda import *
from Configuracion import *

class Tablero:
    def __init__(self, configuracion) -> None:
        self.mapa = [Celda(0) for i in range(configuracion.width*configuracion.height)]
minesNum = 0
while(minesNum<configuracion.mines)
    minePosx = random()%configuracion .width
    minePosy = random()%configuracion.hight
    if(Tablero.mapa[minePosx*configuracion.width+minePosy].value !=-1)
        Tablero.mapa[minePosx*configuracion.width+minePosy].value=-1
        minesNum+=1
        for i in rage(minePosx*width-1, minePosx*width+2)
            for j in range(minePosy-1, minePosy+2)
                if (Tablero.mapa[i+j].valor!=-1) Celda+=1


setEnv()
conf = Configuracion(int(os.environ.get('WIDTH')),int(os.environ.get('HEIGHT')),int(os.environ.get('MINES')))
new_mapa = Tablero(conf)
print(new_mapa.mapa[0].valor)