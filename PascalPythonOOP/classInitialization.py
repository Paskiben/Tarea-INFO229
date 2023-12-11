class Matematica:
    def __init__(self, x, y):
        self.sum = x+y
        self.rest = x-y
        self.product = x*y
        self.div = x/y

x = int(input("Ingrese x: "))
y = int(input("Ingrese y: "))
mat = Matematica(x,y)
print(f"{mat.div}")