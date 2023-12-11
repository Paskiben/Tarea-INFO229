class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
    
    def ingresaDato(self):
        self.datos = [int(input(f"Ingresar dato {i+1}: ")) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        super().__init__(2)
    
    def suma(self):
        x,y, = self.datos
        s = x+y
        print("El resultado es: ",s)
    
    def resta(self):
        x,y = self.datos
        r = x-y
        print("El resultado es: ",r)

class raiz(Calculadora):
    def __init__(self):
        super().__init__(1)
    
    def cuadrada(self):
        import math
        x, = self.datos
        print("El resultado es: ",math.sqrt(x))

obj = op_basicas()
print(isinstance(obj,raiz))
print(issubclass(op_basicas,Calculadora))