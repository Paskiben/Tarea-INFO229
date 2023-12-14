import os
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
        os.environ [var[0]]= var[1]
    print("Variables de entorno cargadas correctamente")