
def cuadrado(tuplas):
    _abscisas = []
    _ordenadas = []
    for tupla in tuplas:
        x,y = tupla
        _abscisas.append(abs(x))
        _ordenadas.append(abs(y))

    if len(set(_abscisas)) == len(set(_ordenadas)):
        return ("Si es cuadrado.")
    else:
        return ("No es cuadrado.")