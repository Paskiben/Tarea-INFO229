from os import environ
from random import shuffle
from Celda import *
from Configuracion import *

class Tablero:
    def __init__(self, configuracion):
        if(isinstance(configuracion, Configuracion)):
            self.__mapa = [Celda(0) for i in range(configuracion.width*configuracion.height)]
            self.putMines(configuracion)
        else:
            print("El objeto entregado para configurar no es de clase configuracion")


    #getters
    def __getMapa(self):
        return self.__mapa
    #setters
    def __setMapa(self, config):
        if(isinstance(config, Configuracion)):
            self.__mapa = [Celda(0) for i in range(config.width*config.height)]
            self.putMines(config)

    #propertys (patron decorator)
    mapa = property(fget= __getMapa,
                    fset= __setMapa,
                    doc = "propiedades mapa")

    def putMines(self, conf):
        pos = [(x,y) for x in range(conf.width) for y in range(conf.height)]
        shuffle(pos)
        for i in range(0, conf.mines):
            x,y = pos.pop()
            index = x*conf.height+y
            if(self.mapa[index].valor !=-1):
                self.mapa[index].valor=-1
                for i in range(x-1, x+2):
                    for j in range(y-1, y+2):
                        if ((i>=0 & j>=0 & i<conf.width & j<conf.height) & self.mapa[i+j].valor!=-1): self.mapa[i+j].valor+=1