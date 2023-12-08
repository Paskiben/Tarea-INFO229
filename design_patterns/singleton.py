class Configuracion:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Configuracion, cls).__new__(cls)
            cls._instance.valores = {}
        return cls._instance

    def set_valor(self, clave, valor):
        self.valores[clave] = valor

    def get_valor(self, clave):
        return self.valores.get(clave, None)

# Ejemplo de uso del patrón Singleton
if __name__ == "__main__":
    config1 = Configuracion()
    config1.set_valor("idioma", "espanol")

    config2 = Configuracion()
    print(config2.get_valor("idioma"))  # Salida: espanol
