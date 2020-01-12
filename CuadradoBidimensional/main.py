"""Este archivo es para probar el modulo es cuadrado.

Autor: Geordie Quiroa
"""

from escuadrado import es_cuadrado

coordenadas = [  # Esas coordenadas si forman un cuadrado.
                (2,3),
                (6,-1),
                (6,3),
                (2,-1)
            ]

print(es_cuadrado(coordenadas))