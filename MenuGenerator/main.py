from menugen import MenuGen

nombre_menu = "operaciones basicas"

opciones = {
                "Sumar": lambda x, y: x + y,
                "Restar": lambda x, y: x - y 
            }

menu = MenuGen(opciones, nombre_menu)

menu.generar_menu()

# array = ["a", "b", "c"]

# var = '\n'.join([
#             "{} --> {}".format(
#                                 i+1,
#                                 array[i]
#                         ) for i in range(len(array))
# ])

# print(var)