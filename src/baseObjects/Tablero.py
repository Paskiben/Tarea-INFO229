from random import shuffle
from baseObjects.Celda import *
from baseObjects.Configuracion import *

class Tablero:
    #Constructor
    def __init__(self, configuracion):
        if(isinstance(configuracion, Configuracion)):
            self.__mapa = [Celda(0) for i in range(configuracion.width*configuracion.height)]
            self.__mines =[]
            self.__putMines(configuracion)
        else:
            print("El objeto entregado para configurar no es de clase configuracion")


    #Getters
    def __getMapa(self):
        return self.__mapa
    def __getMines(self):
        return self.__mines

    #Setters
    def __setMapa(self, config):
        if(isinstance(config, Configuracion)):
            self.__mapa = [Celda(0) for i in range(config.width*config.height)]
            self.putMines(config)
    def __setMines(self, index):
        if(isinstance(index, int)):
            self.mines.append(index)

    #Propertys (patron decorator)
    mapa = property(fget= __getMapa,
                    fset= __setMapa,
                    doc = "propiedades mapa")
    mines= property(fget=__getMines,
                    fset=__setMines,
                    doc= "propiedades mines")

    #Se inicializa con el contructor tomando en cuenta la configuracion dada.
    def __putMines(self, conf):
        pos = [(x,y) for x in range(conf.width) for y in range(conf.height)] #Se crea un vector con las posciciones (se utiliza como un stack).
        shuffle(pos) #Se revuelven
        for i in range(0, conf.mines):
            x,y = pos.pop() #Se obtiene y elimina la ultima poscicion.
            index = x*conf.height + y #Calculo de indice.
            self.mines = index   #Mines no es igual a indice, gracias al patron de diseño decorator, esta linea permite adjuntar al arreglo el ultimo indice de bomba.
            if(self.mapa[index].valor !=-1):
                self.mapa[index].valor=-1
                for j in range(x-1, x+2):
                    for k in range(y-1, y+2):
                        if ((j>=0 and k>=0 and j<conf.width and k<conf.height) and self.mapa[(j*conf.height)+k].valor!=-1): self.mapa[(j*conf.height)+k].valor+=1 #Se suma 1 a las celdas adyacentes de la mina.