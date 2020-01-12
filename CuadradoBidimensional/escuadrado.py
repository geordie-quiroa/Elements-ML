""" Este modulo determina si las coordenadas forman un cuadrado o no.

Para lograro, utiliza las siguientes
"""
def es_cuadrado(tuplas) -> str:
    _abscisas = [x[0] for x in tuplas]  # Puntos en el eje x 
    _ordenadas = [y[1] for y in tuplas]  # Puntos en el eje y
    
    if ( _n_valores_unicos(_abscisas) == _n_valores_unicos(_ordenadas)) \
        and ( _distancia(_abscisas) == _distancia(_ordenadas)):
        return ("Las coodenadas si forman un cuadrado.")
    else:
        return ("Las coordenadas no forman un cuadrado.")

def _n_valores_unicos(puntos):
    return (len(set(puntos)))

def _distancia(puntos):
    return (max(set(puntos))-min(set(puntos)))