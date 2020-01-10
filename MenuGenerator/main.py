""" Archivo para probar el modulo generador de Menu

Autor: Geordie Quiroa
"""
from menugen import MenuGen

nombre_menu = "operaciones basicas"

opciones = {
                "Sumar": lambda x, y: x + y,
                "Restar": lambda x, y: x - y,
                "Multiplicar": lambda x, y: x * y,
                "Dividir": lambda x, y: x / y
            }

menu = MenuGen(opciones, nombre_menu)

menu.generar_menu()

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