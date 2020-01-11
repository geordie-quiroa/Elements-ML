"""Este modulo encuentra el camino con la suma mas larga.
"""

def procesar(path2file):
    lineas = open(path2file,'r').read().split('\n')
    matriz_limpia = [list(map(int,linea.split())) for linea in lineas if len(linea.split()) > 0]
    for linea in matriz_limpia:
        linea = list(map(int,linea))
        #print(linea)
    print(matriz_limpia)
