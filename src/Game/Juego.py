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
        self.__win = False
        self.__vivo = True
        self.reveladas = 0
        self.marcadas = 0
    
    #getters
    def __getConf(self):
        return self.__conf
    def __getTablero(self):
        return self.__tablero
    def __getWin(self):
        return self.__win
    def __getVivo(self):
        return self.__vivo
    
    #setters
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

    #propertys (patron decorator)
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

    
    def iniciarJuego(self, conf):
        if(isinstance(conf, Configuracion)):
            self.conf = conf
            self.tablero = Tablero(self.conf)
            self.reveladas = 0
            self.marcadas = 0
            self.win = False
            self.vivo = True
