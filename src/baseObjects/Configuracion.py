class Configuracion:
    _instance = None
    
    #Constructor
    def __new__(cls, *args, **kwargs):
        if (not cls._instance):
            cls._instance = super(Configuracion, cls).__new__(cls)
        return cls._instance

    def __init__(self, width, height, mines):
        if (width>=5):
            if (width<=25):
                self.__width = width 
            else:
                self.__width = 25 
        else:
            self.__width= 5

        if (height>=5):
            if (height<=25):
                self.__height = height 
            else:
                self.__height = 25 
        else:
            self.__height= 5

        if (mines >=1):
            if(mines <= self.__width*self.__height-1):
                self.__mines = mines
            else:
                self.__mines = self.__width*self.__height-1
        else:
            self.__mines = 1

    #Getters
    def __getWidth(self):
        return self.__width
    def __getHeight(self):
        return self.__height
    def __getMines(self):
        return self.__mines
    
    #Setters
    def __setWidth(self, width):
        self.__width = width if(width>=5) else 5
        self.__width = width if(width<=25) else 25
    def __setHeight(self, height):
        self.__height = height if(height>=5) else 5
        self.__height = height if(height<=25) else 25
    def __setMines(self, mines):
        self.__mines = mines if(mines>=1) else 1
        self.__mines = mines if(mines<=self.width*self.height-1) else self.width*self.height-1

    #Propertys (patron decorator)
    width = property(fget= __getWidth,
                    fset= __setWidth,
                    doc = "propiedades width")
    height = property(fget= __getHeight,
                    fset= __setHeight,
                    doc = "propiedades height")
    mines = property(fget= __getMines,
                    fset= __setMines,
                    doc = "propiedades width")
    #Metodos
    #Forma de setear las tres varaibles al mismo tiempo
    @property
    def actualConfig(self):
        return f"Ancho = {self.width} Largo = {self.height} numero de minas = {self.mines}"
    @actualConfig.setter
    def setConfig(self, width, height, mines):
        if (width>=5):
            if (width<=25):
                self.__width = width 
            else:
                self.__width = 25 
        else:
            self.__width= 5

        if (height>=5):
            if (height<=25):
                self.__height = height 
            else:
                self.__height = 25 
        else:
            self.__height= 5

        if (mines >=1):
            if(mines <= self.__width*self.__height-1):
                self.__mines = mines
            else:
                self.__mines = self.__width*self.__height-1
        else:
            self.__mines = 1