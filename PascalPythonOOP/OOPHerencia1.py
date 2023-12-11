class pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def description(self):
        return f"{self.nombre} es un pokemon de tipo: {self.tipo}"

class pikachu(pokemon):
    def ataque(self, tipoataque):
        return f"{self.nombre} tipo de ataque: {tipoataque}"

nuevo_pokemon = pikachu("pokachu", "electrico")
print(nuevo_pokemon.description())
print(nuevo_pokemon.ataque("Thundershock"))