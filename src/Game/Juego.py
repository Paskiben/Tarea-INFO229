from baseObjects.Tablero import *
from Tools.Env import *

class Juego:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if (not cls._instance):
            cls._instance = super(Juego, cls).__new__(cls)
        return cls._instance
    
    #El contructor de la clase, inicializ todos los componenetes del juego y carga las variables de entorno.
    def __init__(self):
        setEnv()
        checkEnv()
        self.__conf = Configuracion(int(environ.get('WIDTH')),int(environ.get('HEIGHT')),int(environ.get('MINES')))
        self.__tablero = Tablero(self.conf)
        self.__win = False
        self.__vivo = True
        self.reveladas = 0
        self.marcadas = 0
    
    #Getters.
    def __getConf(self):
        return self.__conf
    def __getTablero(self):
        return self.__tablero
    def __getWin(self):
        return self.__win
    def __getVivo(self):
        return self.__vivo
    
    #Setters.
    def __setConf(self, conf):
        if(isinstance(conf, Configuracion)):
            self.__conf = conf
    def __setTablero(self,tablero):
        if(isinstance(tablero, Tablero)):
            self.__tablero = tablero
    def __setWin(self, win):
        if(isinstance(win, bool)):
            self.__win = win
    def __setVivo(self, vivo):
        if(isinstance(vivo, bool)):
            self.__vivo = vivo

    #Propertys (patron decorator).
    conf = property(fget= __getConf,
                    fset= __setConf,
                    doc = "propiedades configuracion")
    tablero = property(fget= __getTablero,
                    fset= __setTablero,
                    doc = "propiedades tablero")
    win = property(fget= __getWin,
                    fset= __setWin,
                    doc = "propiedades win")
    vivo = property(fget = __getVivo,
                    fset = __setVivo,
                    doc = "propiedades vivo")

    #Metodo de la para iniciar el juega con todas sus caracteristicas iniciales.
    def iniciarJuego(self, conf):
        if(isinstance(conf, Configuracion)):
            self.conf = conf
            self.tablero = Tablero(self.conf)
            self.reveladas = 0
            self.marcadas = 0
            self.win = False
            self.vivo = True

    def revelar_celda(self,fila,columna):
        index = columna*self.conf.height + fila
        if (not self.tablero.mapa[index].marca):
            if (self.tablero.mapa[index].valor == -1 and (not self.tablero.mapa[index].descubierta)):
                self.tablero.mapa[index].descubrir
                for i in self.tablero.mines:
                    self.tablero.mapa[i].descubrir
                self.vivo = False
            elif (self.tablero.mapa[index].valor == 0 and (not self.tablero.mapa[index].descubierta)):
                self.reveladas +=1
                self.tablero.mapa[index].descubrir
                for i in range(columna-1, columna+2):
                    for j in range(fila-1, fila+2):
                        if ((i>=0 and j>=0 and i<self.conf.width and j<self.conf.height) and (self.tablero.mapa[i*self.conf.height+j].valor>0 or (i==columna or j==fila))): self.revelar_celda(j,i)
                if (self.reveladas == self.conf.height * self.conf.width - self.conf.mines):
                    self.win = True
                    self.vivo= False
            elif (not self.tablero.mapa[index].descubierta):
                self.tablero.mapa[index].descubrir
                self.reveladas +=1 
                if (self.reveladas == self.conf.height * self.conf.width - self.conf.mines):
                    self.win = True
                    self.vivo = False
