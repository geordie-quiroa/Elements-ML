"""Este modulo encuentra el camino de un triangulo cuya sumatoria de adyacentes sea la mas larga.

Autor: Geordie Quiroa

Retorna un string con el resultado de la sumatoria.
"""

# Metodo publico

def procesar(path2file) -> str:
    """Args
    path2file -- Path de un archivo .txt cuyos digitos formen un triangulo. 
    """
    lineas = open(path2file,'r').read().split('\n')
    arbol_limpio = [list(map(float,linea.split())) for linea in lineas if len(linea.split()) > 0]  # omite lineas vacias y convierte cada elemento a digito
    return ("Total: {}".format(_recorrer(arbol_limpio)))

# Metodos privados

def _adyacente(arreglo, indice_anterior, total_acum) -> list:
    max_len = len(arreglo)
    inf, sup = 0, max_len
    if indice_anterior != 0 and max_len > 3:  # caso en el que la linea tiene mas de 3 numeros, se puede indexar hacia ambos lados. 
        inf, sup = indice_anterior - 1, indice_anterior + 2  # + 2 porque el slicing de arreglos es excluyente [inf:sup)
    elif indice_anterior == 0 and max_len > 2:  # caso en el que el adyacente no tiene frontera izquierda
        sup = indice_anterior + 2
    total_acum += max(arreglo[inf:sup])
    idx = arreglo.index(max(arreglo[inf:sup]))
    return (idx,total_acum)

def _recorrer(arbol) -> int:
    idx, total = 0, 0
    for i in range(len(arbol)): # recorre cada linea del archivo
        idx, total = _adyacente(arbol[i], idx, total)
    return (total)

