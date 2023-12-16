class Celda:
    #constructor
    def __init__(self, valor):
        self.__valor = valor if (valor>=-1 and valor<9) else 0
        self.__descubierta = False
        self.__marca = False
        
    #getters
    def __getValor(self):
        return self.__valor
    def __getDescuierta(self):
        return self.__descubierta
    def __getMarca(self):
        return self.__marca
    
    #setters
    def __setValor(self, valor):
        self.__valor = valor if (valor>=-1 and valor<9) else 0
    
    #propertys (patron decorator)
    valor = property(fget= __getValor,
                    fset= __setValor,
                    doc = "propiedades valor")
    marca = property(fget= __getMarca,
                    doc = "propiedades marca")
    descubierta = property(fget = __getDescuierta,
                            doc = "propiedades descubierta")
    #metodos
    @property
    def marcar(self):
        self.__marca = False if (self.__marca) else True

    @property
    def descubrir(self):
        if(not self.__descubierta):
            self.__descubierta = True
