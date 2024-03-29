# Algoritmo que realiza control de bucles (continue y break)
# hecho por @auphireo

import random

def lanzar():
    '''
        Devuelve los valores aleatorios de una lista. 
        Simula un lanzamiento de dados y muestra la suma
        de ellos. El lanzamiento se realiza tantas veces 
        como el usuario quiera.
    '''
    return random.choice([1,2,3,4,5,6])

ciclo = 1

while ciclo > 0:
    # ciclo infinito para realizar los lanzamientos de dados

    dado1 = lanzar() # variable del dado uno
    dado2 = lanzar() # variable del dado dos
    print('Valor del dado uno es: {}'.format(dado1)) # se imprime el valor random del dado uno 
    print('Valor del dado dos es: {}'.format(dado2)) # se imprime el valor random del dado dos
    print('La suma de los dados es: {}'.format(dado1+dado2)) # se imprime el valor de la suma

    pregunta = input('Desea realizar un nuevo lanzamiento? S/N ...')

    if pregunta in ("n", "N", "no", "No", "NO"):
        ciclo = -1
        break

    if pregunta in ("s", "S", "si", "Si", "SI"):
        ciclo = 1
        continue

    else:
        print('la próxima vez escribe si o no')
        break
