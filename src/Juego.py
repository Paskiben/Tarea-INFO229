from baseObjects.Tablero import *
from Tools.Env import *
class Juego:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if (not cls._instance):
            cls._instance = super(Juego, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        setEnv()
        checkEnv()
        self.__conf = Configuracion(int(environ.get('WIDTH')),int(environ.get('HEIGHT')),int(environ.get('MINES')))
        self.__tablero = Tablero(self.conf)
        self.__time = 0; #Modify pos GUI integration
    
    #getters
    def __getConf(self):
        return self.__conf
    def __getTablero(self):
        return self.__tablero
    def __getTime(self):
        return self.__time
    #setters
    def __setConf(self, conf):
        self.__conf = conf
    def __setTablero(self,tablero):
        self.__tablero = tablero
    def __setTime(self,time):
        self.__time = time
    #propertys (patron decorator)
    conf = property(fget= __getConf,
                    fset= __setConf,
                    doc = "propiedades configuracion")
    tablero = property(fget= __getTablero,
                       fset= __setTablero,
                    doc = "propiedades tablero")
    time = property(fget= __getTime,
                    fset= __setTime,
                    doc = "propiedades time")
    
    def iniciarJuego(self, conf):
        if(isinstance(conf, Configuracion)):
            self.conf = conf
            self.tablero = Tablero(self.conf)
            self.time = 0;
Juego()