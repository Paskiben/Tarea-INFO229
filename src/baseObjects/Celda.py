class Celda:
    #Constructor de la clase, con los valores iniciales de las celdas.
    def __init__(self, valor):
        self.__valor = valor if (valor>=-1 and valor<9) else 0
        self.__descubierta = False
        self.__marca = False
        
    #Getters.
    def __getValor(self):
        return self.__valor
    def __getDescuierta(self):
        return self.__descubierta
    def __getMarca(self):
        return self.__marca
    
    #Setters.
    def __setValor(self, valor):
        self.__valor = valor if (valor>=-1 and valor<9) else 0
    
    #Propertys (patron decorator)
    valor = property(fget= __getValor,
                    fset= __setValor,
                    doc = "propiedades valor")
    marca = property(fget= __getMarca,
                    doc = "propiedades marca")
    descubierta = property(fget = __getDescuierta,
                            doc = "propiedades descubierta")
    #Metodos.
    #Marcar: Se encarga de cambiar los estados de las celdas respecto a las marcas/banderas.
    @property
    def marcar(self):
        self.__marca = False if (self.__marca) else True
    #Descubrir: Cambia el estado de la celda respecto si esta descubierta o no.
    @property
    def descubrir(self):
        if(not self.__descubierta):
            self.__descubierta = True
