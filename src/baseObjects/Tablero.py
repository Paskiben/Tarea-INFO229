from random import shuffle
from baseObjects.Celda import *
from baseObjects.Configuracion import *

#Hacer arreglo con bombas

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
            index = x*conf.height + y
            if(self.mapa[index].valor !=-1):
                self.mapa[index].valor=-1
                for j in range(x-1, x+2):
                    for k in range(y-1, y+2):
                        if ((j>=0 and k>=0 and j<conf.width and k<conf.height) and self.mapa[(j*conf.height)+k].valor!=-1): self.mapa[(j*conf.height)+k].valor+=1