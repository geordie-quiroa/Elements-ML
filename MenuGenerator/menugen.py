""" Generador de Menus dinamicos

Autor: Geordie Quiroa

Este modulo crea la estructura interna para generar cualquier menu de funciones numericas,
cuyas funciones tengan un maximo de 5 parametros, o la funcion lambda contenga menos de 3 argumentos.
"""

import inspect  # Para contar n parametros de una funcion, y solicitar n inputs.
from functools import reduce # Se utiliza para iterar y hacer calculos sobre listas

class MenuGen:

    # Inicializador / atributos de instancia
    def __init__(self, opciones_dict, nombre="Opciones"):
        """ Crea los atributos del menu.
        
        Keyword arguments:
        opciones_dict -- un diccionario cuya llave es el nombre de la funcionalidad, y su valor es la funcion lambda a ejecutar.
        nombre -- es el nombre del menu. 
        """
        
        # Atributos del menu
        self.dictionary = opciones_dict
        self.opciones = opciones_dict.items()
        self.nombre = nombre
        self.cantidad = len(opciones_dict)
        self.variables = []
        self.resultado = []
    
    # Metodos publicos

    def generar_menu(self):
        print(self._imprimir_opciones())
        _input_menu = self._recibir_opcion()
        self.variables, self.resultado = self._operar_n_parametros(input_menu = _input_menu)
        print(self._imprimir_resultado(opcion = _input_menu))
    
    # Metodos privados

    def _imprimir_opciones(self) -> str:
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
            return (self._input_invalido(str(exc)))
        if input_ not in [i+1 for i in range(self.cantidad)]:
            self._input_invalido(input_)
        else:
            return (input_ - 1) # para indexar correctamente en el diccionario

    def _input_invalido(self, p="X") -> None:
        print("Se ha ingresado un valor invalido. - {} - Intente de nuevo.".format(p))
        return (None)

    def _operar_n_parametros(self, input_menu) -> list:
        """Solicita parametros de cantidad variable.
        Dependiendo de la catidad de argumentos que la funcion en el diccionario utilice.

        Retorna una lista con los parametros ingresados, y el resultado de operar la funcion lambda.
        """
        _params = []
        _funcionalidad = list(self.dictionary.values())[input_menu] # Para acceder a las caracteristicas de la funcionalidad seleccionada.
        _n_args = len(inspect.getargspec(_funcionalidad)[0]) # cuenta la cantidad de argumentos de la funcion en el diccionario
        _lambda_regx = "<lambda>"
        for i in range(_n_args): 
            try:
                _params.append(float(input("Ingrese parametro {}: ".format(i+1))))
            except Exception as exc:
                return (self._input_invalido(str(exc)))

        if _funcionalidad.__name__ == _lambda_regx:
            return (_params, reduce(_funcionalidad, _params))
        else:  # Para otro tipo de funciones que no son lambda. 
            if _n_args == 1:
                return (_params, _funcionalidad(_params[0]))
            elif _n_args == 2:
                return (_params, _funcionalidad(_params[0], _params[1]))
            elif _n_args == 3:
                return (_params, _funcionalidad(_params[0], _params[1], _params[2]))
            elif _n_args == 4:
                return (_params, _funcionalidad(_params[0], _params[1], _params[2], _params[3]))
            elif _n_args == 5:
                return (_params, _funcionalidad(_params[0], _params[1], _params[2], _params[3], _params[4]))
                
    def _imprimir_resultado(self, opcion) -> str:
        return ("El resultado para {} es: {}".format(list(self.dictionary.keys())[opcion], self.resultado))


    
