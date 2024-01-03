#funcion de fibonacci
# Realizado por @auphireo

def fib(n): # escribe la funcion de fibonacci hasta (n)
    """ Escribe los "n" números de la seria de Fibonacci """
    a,b = 0,1
    z=0
    result=[]
    while z < n:
        # print(a, end=" ")
        a, b = b, a + b
        result.append(a)
        z+=1

    return result
  


print('*'*60)
print('El siguiente algoritmo muestra los "n" números de la secuencia')
print('Fibonacci, hasta el número ingresado por pantalla')
print('*'*60)

try:
    num = int(input('Ingresa el número "n": '))
    if num > 2:
        serie = fib(num)
    if num < 2:
        raise NameError('El número que escogiste no se desarrolla la serie de Fibonacci')
           
except ValueError:
    print("Debes escribir un número!")
except NameError as NaE:
    print(NaE)   

else:
    print('{0} Estos son los {1} primeros números de la serie fibonacci.'.format(serie, num))
finally:
    print('\nFin del algoritmo')
