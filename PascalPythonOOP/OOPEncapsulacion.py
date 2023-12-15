class Empleado:
    def __init__(self, nombre, apellido, salario) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario = salario
    
    #getters
    def __getNombre(self):
        return self.__nombre
    def __getApellido(self):
        return self.__apellido
    def __getSalario(self):
        return self.__salario
    
    #setters
    def __setNombre(self, nombre):
        self.__nombre = nombre
    def __setApellido(self, apellido):
        self.__apellido = apellido
    def __setSalario(self, salario):
        self.__salario = salario
    
    #erasers
    def __delNombre(self):
        del self.__nombre
    def __delApellido(self):
        del self.__apellido
    def __delSalario(self):
        del self.__salario
    
    def __cuenta(self):
        print("Cuenta de procesamiento")

    @property
    def email(self):
        return f"{self.nombre}@gmail.com"
    
    @property
    def fullname(self):
        return f"{self.nombre} {self.apellido}" 
    @fullname.setter
    def fullname(self, name):
        nombre, apellido = name.split(" ")
        self.nombre = nombre
        self.apellido = apellido
    @fullname.deleter
    def fullname(self):
        self.nombre = None
        self.apellido = None
    
    nombre = property(fget= __getNombre,
                    fset= __setNombre,
                    fdel= __delNombre,
                    doc = "soy la propiedad del nombre")
    salario = property(fget= __getSalario,
                    fset= __setSalario,
                    fdel= __delSalario,
                    doc = "soy la propiedad del salario")
    apellido = property(fget= __getApellido,
                    fset= __setApellido,
                    fdel= __delApellido,
                    doc = "soy la propiedad del apellido")
    
    # def __add__(self, other):
    #     return self.salario + other.salario

emp1 = Empleado("Victor","Torres", 3000)
emp2 = Empleado("Sarina","Sarosa", 7000)
#Acceso a variables ocultas
# print(emp1._Empleado__nombre)
# emp1._Empleado__cuenta()
emp1.fullname = "Sara Ramos"
print(emp1.fullname, emp1.salario, emp1.email)
print(emp1 + emp2)
