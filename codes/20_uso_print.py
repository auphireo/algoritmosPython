# Este pequeño código muestra las diferentes formas de usar 
# el comando "print".

nombre1 = "Mario"
edad1 = "25"

print(nombre1 + ' : ' +edad1)
print(nombre1, ':', edad1)
print(f'{nombre1} : {edad1}')
print('%s : %s' % (nombre1,edad1))
print('{} : {}'.format(nombre1,edad1))

nombre2 = "Julio"
edad2 = "35"

print('La edad de ' + nombre2 + ' es ' +edad2 + ' años.')
print('La edad de', nombre2, 'es', edad2, 'años.')
print(f'La edad de {nombre2} es {edad2} años.')
print('La edad de %s es %s años.' % (nombre2,edad2))
print('La edad de {} es {} años.'.format(nombre2,edad2))