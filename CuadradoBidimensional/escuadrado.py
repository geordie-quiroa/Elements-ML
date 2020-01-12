""" Este modulo determina si las coordenadas forman un cuadrado o no.

Autor: Geordie Quiroa

Para lograrlo, utiliza las siguientes propiedades:
    - La cantidad de valores unicos en los ejes X y Y seran iguales para cada uno de los ejes debido a que forman un cuadrado.
    - La distancia para los puntos en el eje X es la misma que la de los puntos en el eje Y.

Retorna un string con un enunciado afirmativo o negativo.
"""
# Metodo publico

def es_cuadrado(tuplas) -> str:
    _abscisas = [x[0] for x in tuplas]  # Puntos en el eje x 
    _ordenadas = [y[1] for y in tuplas]  # Puntos en el eje y
    
    if ( _n_valores_unicos(_abscisas) == _n_valores_unicos(_ordenadas)) \
        and ( _distancia(_abscisas) == _distancia(_ordenadas)):
        return ("Las coodenadas si forman un cuadrado.")
    else:
        return ("Las coordenadas no forman un cuadrado.")

# Metodos privados

def _n_valores_unicos(puntos) -> int:
    return (len(set(puntos)))

def _distancia(puntos) -> int:
    return (max(set(puntos))-min(set(puntos)))