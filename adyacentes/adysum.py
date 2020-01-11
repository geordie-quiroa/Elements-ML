"""Este modulo encuentra el camino con la suma mas larga.
"""

def procesar(path2file):
    lineas = open(path2file,'r').read().split('\n')
    arbol_limpio = [list(map(int,linea.split())) for linea in lineas if len(linea.split()) > 0]  # omite lineas vacias y convierte cada elemento a entero
    print(arbol_limpio)
    _recorrer(arbol_limpio)

def _adyacente(arreglo, indice_anterior, total_acum) -> list:
    max_len = len(arreglo)
    inf, sup = 0, max_len
    if indice_anterior != 0 and max_len > 3 :
        inf, sup = indice_anterior - 1, indice_anterior + 2 # + 2 porque el slicing de arreglos es excluyente [inf:sup)
    elif indice_anterior == 0 and max_len > 2:
        sup = indice_anterior + 2
        #sup = max_len
    total_acum += max(arreglo[inf:sup])
    idx = arreglo.index(max(arreglo[inf:sup]))

    
    return (idx,total_acum)

def _recorrer(arbol):
    total = 0
    for i in range(len(arbol)): # recorre cada linea del archivo
        if i == 0:
            total += arbol[0][0]
            idx = 0
        else:
            idx, total = _adyacente(arbol[i], idx, total)
        #adyacente(nivel)
    print(total)

