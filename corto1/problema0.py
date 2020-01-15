""" Este modulo busca convertir digitos a su nomenclatura en palabras.

Retorna el digito ingresado, en palabras.
"""
import math

digito = 227
resultados = []
en_palabras = " ".join([
])
unidades = {
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro",
    "5":"cinco",
    "6":"seis",
    "7":"siete",
    "8":"ocho",
    "9":"nueve",
    "11":"once",
    "12":"doce",
    "13":"trece",
    "14":"catorce",
    "15":"quince",
}

decenas = {
    "1":"diez",
    "2":"veinte",
    "3":"treinta",
    "4":"cuarenta",
    "5":"cincuenta",
    "6":"sesenta",
    "7":"setenta",
    "8":"ochenta",
    "9":"noventa",
}
centenas = {
    "1":"ciento",
    "2":"doscientos",
    "3":"trescientos",
    "4":"cuatroscientos",
    "5":"quinientos",
    "6":"seiscientos",
    "7":"setescientos",
    "8":"ochoscientos",
    "9":"novescientos",
}

miles = {
    
}

if 0<digito<100:
    # caso especial de 1 a 15
    if digito < 16 and digito % 10 != 0:
        resultados.append(unidades.get(str(digito)))
    #print(decenas.get(str(math.floor(digito/10))))
    elif digito % 10 != 0 and digito > 15: # tiene residuo
        resultados.append(decenas.get(str(math.floor(digito/10))))
        resultados.append("y")
        resultados.append(unidades.get(str(math.floor(digito%10))))
elif 99 < digito < 999:
    resultados.append(centenas.get(str(math.floor(digito/100))))
    resultados.append(decenas.get(str(math.floor((digito%100)/10))))
    if digito % 100 != 0:
        resultados.append("y")
        resultados.append(unidades.get(str(math.floor((digito%100)%10))))

print(" ".join(resultados))