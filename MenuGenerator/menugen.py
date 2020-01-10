""" Generador de Menus

Autor: Geordie Quiroa

Este modulo crea la estructura interna para generar cualquier menu de funciones numericas,
cuyas funciones utilizen 2 parametros.
"""

class MenuGen:

    # Inicializador / atributos de instancia
    def __init__(self, opciones_dict, nombre="Opciones"):
        """ Crea los atributos del menu.
        
        Keyword arguments:
        opciones_dict -- un diccionario cuya llave es el nombre de la funcionalidad, y su valor es la funcion a ejecutar.
        nombre -- es el nombre del menu. 
        """
        
        # Atributos del menu
        self.dictionary = opciones_dict
        self.opciones = opciones_dict.items()
        self.nombre = nombre
        self.cantidad = len(opciones_dict)
        
        # Atributos internos
        self._variables = (0, 0)  # Es un menu para dos parametros de entrada
    
    # Metodos publicos

    def generar_menu(self):
        # self._imprimir_titulo()
        # self._imprimir_opciones()
        print(self._imprimir_opciones2())
        self._recibir_opcion()
        
    
    # Metodos privados

    def _imprimir_titulo(self):
        print(" ------ Bienvenido al Menu de {} ------\n Las opciones son las siguientes:\n".format(self.nombre))



    def _imprimir_opciones(self):
        #"\n".join(["{} --> {}".format(key, value) for key, value in self.opciones])
        for key, value in self.opciones:
           print(""" {} -> {} """.format(
                                    key,
                                    value
                                )
            )

    def _imprimir_opciones2(self):
        """Concatena cada elemento visual del menu, tomando en cuenta la variacion de opciones.
        
        Retorna un string con enters para la visualizacion del menu.
        """
        return ('\n'.join(
                            [
                                " ------ Bienvenido al Menu de {} ------ ".format(self.nombre),
                                " Las opciones son las siguientes:",
                                '\n'.join(
                                            [
                                                " {}. {}".format(
                                                                    i+1,
                                                                    list(self.dictionary.keys())[i]
                                                                ) for i in range(self.cantidad)
                                            ]
                                        ),
                                " Ingrese una opcion del (1-{}):".format(self.cantidad)
                            ]
                        )
                )
    
    def _recibir_opcion(self) -> int:
        
        try:
            input_ = int(input("> "))
        except Exception as exc:
            return self._input_invalido(str(exc))
        
        if input_ not in [i+1 for i in range(self.cantidad)]:
            self._input_invalido(input_)
        else:
            return (input_)
        
    def _input_invalido(self, p="X") -> None:
        print("Se ha ingrsado un valor invalido. - {} - es invalido".format(p))
    
