# Manejo de excepciones 
# Realizado por @auphireo
'''
    El siguiente algoritmos hace un uso de excepciones 
    con un ejemplo de una operación de división entre dos
    números. 
'''
def division(num1,num2):
    # Función que realiza la división entre dos números
    resul = num1/num2
    return resul

print('*'*60)
print('El siguiente algoritmo realiza la división entre dos números')
print('\n X = A / B')
print('*'*60)

try:
    num1 = float(input('ingresa A: ')) 
    num2 = float(input('ingresa B: '))
    x = division(num1,num2)
except ZeroDivisionError:
    print("No se puede dividir entre cero!")
except ValueError:
    print('A y B tienen que ser números, no letras!')
else:
    print('El valor de X es: {:.2f}'.format(x))
finally:
    print('\nFin del algoritmo')
