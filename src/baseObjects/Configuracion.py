class Configuracion:
    _instance = None
    #constructor
    def __new__(cls, *args, **kwargs):
        if (not cls._instance):
            cls._instance = super(Configuracion, cls).__new__(cls)
        return cls._instance

    def __init__(self, width, height, mines):
        self.__width = width if(width>=5) else 5
        self.__height = height if(height>=5) else 5
        self.__mines = mines if(mines>=1) else 1
        self.__width = width if(width<=25) else 25
        self.__height = height if(height<=25) else 25
        self.__mines = mines if(mines<=25*25-1) else 25*25-1

    #getters
    def __getWidth(self):
        return self.__width
    def __getHeight(self):
        return self.__height
    def __getMines(self):
        return self.__mines
    
    #setters
    def __setWidth(self, width):
        self.__width = width if(width>=5) else 5
        self.__width = width if(width<=25) else 25
    def __setHeight(self, height):
        self.__height = height if(height>=5) else 5
        self.__height = height if(height<=25) else 25
    def __setMines(self, mines):
        self.__mines = mines if(mines>=1) else 1
        self.__mines = mines if(mines<=25*25-1) else 25*25-1

    #propertys (patron decorator)
    width = property(fget= __getWidth,
                    fset= __setWidth,
                    doc = "propiedades width")
    height = property(fget= __getHeight,
                    fset= __setHeight,
                    doc = "propiedades height")
    mines = property(fget= __getMines,
                    fset= __setMines,
                    doc = "propiedades width")
    
    @property
    def actualConfig(self):
        return f"Ancho = {self.width} Largo = {self.height} numero de minas = {self.mines}"
    @actualConfig.setter
    def setConfig(self, width, height, mines):
        self.__width = width if(width>=5) else 5
        self.__height = height if(height>=5) else 5
        self.__mines = mines if(mines>=1) else 1
        self.__width = width if(width<=25) else 25
        self.__height = height if(height<=25) else 25
        self.__mines = mines if(mines<=25*25-1) else 25*25-1