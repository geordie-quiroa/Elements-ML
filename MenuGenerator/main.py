""" Archivo para probar el modulo generador de Menu

Autor: Geordie Quiroa
"""
from functools import reduce # Se utiliza para iterar y hacer calculos sobre listas
import math  # Se utiliza para calcular raiz cuadrada


from menugen import MenuGen

nombre_menu = "operaciones basicas"

opciones = {
                "Sumar": lambda x, y: x + y,
                "Restar": lambda x, y: x - y,
                "Multiplicar": lambda x, y: x * y,
                "Dividir": lambda x, y: x / y,
                "Hipotenusa": lambda x, y: math.sqrt(x**2 + y**2)
            }

menu = MenuGen(opciones, nombre_menu)

menu.generar_menu()

for val in opciones.values():
    print(val)

uno = (5,)
dos = (7,)

suma = lambda x, y: x + y
r = list(map(lambda x, y: x + y, uno,dos))
print(r)
# array = ["a", "b", "c"]

# var = '\n'.join([
#             "{} --> {}".format(
#                                 i+1,
#                                 array[i]
#                         ) for i in range(len(array))
# ])

# print(var)