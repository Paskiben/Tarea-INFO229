class Estudiante:
    
    def __init__(self, nombre, apellido, edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self) -> str:
        return f"hola que tal, soy {self.nombre} {self.apellido} y tengo {self.edad} anos"
    
estudiante = Estudiante("victor", "cruz", 17)
print(f"{estudiante !r}")