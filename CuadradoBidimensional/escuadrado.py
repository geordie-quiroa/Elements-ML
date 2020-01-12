
def cuadrado(tuplas):
    _abscisas = [x[0] for x in tuplas]
    _ordenadas = [y[1] for y in tuplas]
    
    if (len(set(_abscisas)) == len(set(_ordenadas)))\
        and (max(set(_abscisas))-min(set(_abscisas))) == (max(set(_ordenadas))-min(set(_ordenadas))):
        return ("Las coodenadas si forman un cuadrado.")
    else:
        return ("Las coordenadas no forman un cuadrado.")