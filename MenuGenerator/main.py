""" Archivo para probar el modulo generador de Menu

Autor: Geordie Quiroa
"""

import math  # Se utiliza para calcular raiz cuadrada en hipotenusa

from menugen import MenuGen

nombre_menu = "operaciones basicas"

opciones = {
                "Sumar": lambda x, y: x + y,
                "Restar": lambda x, y: x - y,
                "Multiplicar": lambda x, y: x * y,
                "Dividir": lambda x, y: x / y,
                "Hipotenusa": lambda x, y: math.sqrt(x**2 + y**2),
                "Triple producto": lambda x, y, z: x*y*z
            }

#menu = MenuGen(opciones, nombre_menu)

#menu.generar_menu()
#print(menu.variables)
#print(menu.resultado)

def suma(x,y,z):
    return x+y+z

import inspect

print(inspect.getargspec(suma))
variables = [[1],[2],[3]]

