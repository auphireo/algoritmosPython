# Ejemplos de tipos de datos
import sys

# Números enteros
print("Imprimiendo un número entero")
i = 12
print(i)
print(type(i))
print("\n")

x = 250**250
print("resultado de 250^250:{}\n".format(x))
print(type(x))
print("\n")

# después de el valor máximo que puede representar Pytnon, éste asigna el valor de "inf" 
print("Información de los números enteros en Python: \n {}\n".format(sys.int_info))
print("Información de los números flotantes en Python: \n {}\n".format(sys.float_info))

# Strings
s = "Esto es una cadena\n \153 123456789"
r = "Ejemplo de una cadena que tiene un\ncambio de línea" 
# se una \n dentro de la cadena para el cambio de línea
# la barra invertida '\' es un operador que le quita el valor a los caracteres especiales
# pero tambien permite escribri los caractes conociendo el código ASCI de esta forma \111 = o
print(s,r)
print("\n")

valores1 = list(range(33,126))
codigo1 = []
for i in valores1:
    codigo1.append(chr(i))
    print("Código ASCI: {}  ->  valor en caractér: {}".format(i,chr(i)))

valores2 = list(range(128,254))
codigo2 = []
for i in valores2:
    codigo2.append(chr(i))
    print("Código ASCI: {}  ->  valor en caractér: {}".format(i,chr(i)))
