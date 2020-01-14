""" Archivo para probar el modulo generador de Menu

Autor: Geordie Quiroa
"""

import math  # Se utiliza para calcular raiz cuadrada en hipotenusa

from menugen import MenuGen

nombre_menu = "operaciones basicas"

def suma(x,y,z):
    return x+y+z

def aplicar_descuento(precio, descuento):
    if 0 < descuento <= 100:
        return precio - precio * descuento/100
    else: 
        return "Ingrese un descuento valido."

opciones = {
                "Sumar": lambda x, y: x + y,
                "Restar": lambda x, y: x - y,
                "Multiplicar": lambda x, y: x * y,
                "Dividir": lambda x, y: x / y,
                "Hipotenusa": lambda x, y: math.sqrt(x**2 + y**2),
                "Suma triple": suma,
                "Aplicar descuento porcentual": aplicar_descuento,
            }

menu = MenuGen(opciones, nombre_menu)

menu.generar_menu()