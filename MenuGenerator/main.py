""" Archivo para probar el modulo generador de Menu

Autor: Geordie Quiroa
"""

import math  # Se utiliza para calcular raiz cuadrada en hipotenusa
import inspect


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
#print(menu.variables)
#print(menu.resultado)
