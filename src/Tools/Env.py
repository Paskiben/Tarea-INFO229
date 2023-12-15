from os import environ
def setEnv():
    var=[]
    try:
        file = open('./.env', 'r')
    except(FileNotFoundError):
        print("Error al abrir .env!")
        return
    
    for line in file:
        line.strip()
        var = line.split("=")
        environ [var[0]]= var[1]

def checkEnv():
    class Errores(Exception):
        pass
    class VarNotDefined(Errores):
        pass
    try:
        if (environ.get('WIDTH') == None):
            print('La variable de entorno WIDTH no fue definida') 
            raise VarNotDefined
        if (environ.get('HEIGHT') == None):
            print('La variable de entorno WIDTH no fue definida')
            raise VarNotDefined
        if (environ.get('MINES') == None):
            print('La variable de entorno WIDTH no fue definida')
            raise VarNotDefined
        else:
            print("Variables de entorno cargadas correctamente")
    except(VarNotDefined):
        exit()