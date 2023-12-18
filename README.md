# Tarea-INFO299
Integrantes: Rodrigo Erlandsen, Patricio Lobos, Pascal Salinas, Renton Tapia.
Tarea final arquitectura en software.

Para ejecutar este juego es necesario tener instalado:
pygame
pygame_gui
moviepy

Ademas de tener instalado python3, puede instalar las librerias mencionadas anteriormente usando pip3

La configuración base está presente en el archivo .env, el programa está visualmente optimizado para las dimensiones establecidas por lo que pueden haber errores
al modificarlas.

Ejecucion:
    Ejecutar objeto GUI desde la carpeta raiz, es decir, fuera de la carpeta source. en ubuntu sería: "python3 'src/GUI.py'"

Tutorial:
    Puede usar Click izquierdo para revelar una celda.
    Puede usar Click derecho para marcar una celda.

    Al revelar una celda se mostrará un numero que representará cuantas bombas hay en las 8 celdas adyacentes a la revelada, en caso de que sea 0 también se revelaran automaticamente sus celdas adyacentes.

    En la esquina inferior derecha se mostraran la cantidad de banderas disponibles, que al inicio siempre es igual a la cantidad de minas presentes en el tablero.

    Utilizando esta información, su objetivo será liberar todas las celdas que no sean minas pero mucho cuidado pues si libera una mina, explotaran todas las que no esten marcadas.

    Puede cambiar la configuración al hacer click en el engranaje donde puede seleccionar uno de los 3 niveles de dificultad ya establecidos o establecer un modo personalizado.