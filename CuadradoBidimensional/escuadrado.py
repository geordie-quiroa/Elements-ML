
def cuadrado(tuplas):
    _abscisas = []
    _ordenadas = []
    for tupla in tuplas:
        x,y = tupla
        _abscisas.append(x)
        _ordenadas.append(y)

    if (len(set(_abscisas)) == len(set(_ordenadas)))\ 
        and (max(set(_abscisas))-min(set(_abscisas))) == (max(set(_ordenadas))-min(set(_ordenadas))):
        return ("Las coodenadas si forman un cuadrado.")
    else:
        return ("Las coordenadas no forman un cuadrado.")