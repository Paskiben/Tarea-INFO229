class Celda:
    #constructor
    def __init__(self, valor):
        self.__valor = valor if (valor>=-1 & valor<9) else 0
        self.__descubierta = False
        self.__marca = False
        
    #getters
    def __getValor(self):
        return self.__valor
    
    #setters
    def __setValor(self, valor):
        self.__valor = valor if (valor>=-1 & valor<9) else 0
    
    #propertys (patron decorator)
    valor = property(fget= __getValor,
                    fset= __setValor,
                    doc = "propiedades valor")
    
    #metodos
    @property
    def marcar(self):
        self.__marca = False if (self.__marca) else True

    @property
    def descubrir(self):
        if(- self.__descubierta):
            self.__descubierta = True
            return False if (self.valor == -1) else True