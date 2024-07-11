# Algoritmos Python

**Última fecha de actualización: _junio-2024_**

Lo que hay aquí alojado son diferentes algoritmos en _python_ de interes y que seguramente se pueden aprovechar. A veces es dificil encontrar 'la función' que uno necesita o 'la alternativa' que se requiere. Espero ir acumulando varios códigos de Python, Bash y Github. 

## El Zen de Python 

Para conocer mejor el lenguaje que estaremos aprendiendo les compartimos una colección de los 19 principios que influyen en el diseño del lenguaje Python. De alguna manera, muestran la filosofía del mismo:

1) Bello es mejor que feo.
2) Explícito es mejor que implícito.
3) Simple es mejor que complejo.
4) Complejo es mejor que complicado.
5) Plano es mejor que anidado.
6) Espaciado es mejor que denso.
7) La legibilidad es importante.
8) Los casos especiales no son lo suficientemente especiales como para romper las reglas.
9) Sin embargo la practicidad gana a la pureza.
10) Los errores nunca deben pasar silenciosamente.
11) A menos que se silencien explícitamente.
12) Frente a la ambigüedad, evitar la tentación de adivinar.
13) Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
14) A pesar de que esa manera no sea obvia a menos que seas Holandés (el creador lo era)
15) Ahora es mejor que nunca.
16) A pesar de que nunca es muchas veces mejor que ahora mismo.
17) Si la implementación es difícil de explicar, es una mala idea.
18) Si la implementación es fácil de explicar, puede que sea una buena idea.
19) Los namespaces son una gran idea, ¡tengamos más de esos!

## Recursos adicionales

* [Introducción al Pensamiento Computacional] (https://github.com/karlbehrensg/introduccion-pensamiento-computacional)
* [Entrenamiento Básico] (https://entrenamiento-python-basico.readthedocs.io/es/latest)
* [El Libro de Python] (https://ellibrodepython.com/)
* [Python para todos] (https://www.py4e.com)
* [Curso Python Videos] (https://youtu.be/G2FCfQj-9ig)
* [Visualizar tu código] (https://memlayout.com/)
* [Visualizar tu código] (https://pythontutor.com/visualize.html#mode=edit)



## Contenido de los directorios

### Contenido de la carperta _codes_

Son algunos algoritmos con algunos ejemplos sencillos. La intención de code es recopilar muchos códigos que pueda utilizar como biblioteca o fuente de referencia.

```text
codes/
├── 01_tipos_de_datos.py
├── 02_bucle_for_01.py
├── 03_bucle_while_01.py
├── 04_bucle_while_02.py
├── 10_excepciones.py
├── 20_uso_print.py
└── 80_juego_triqui_V0.1.0.py

```

### Contenido de la carpeta _add_

Para algunos algoritmos se requiere manipular archivos con extención tipo ".csv", "xlsx", "txt", ".jpg", entre otros. Estos archivos se irán sumando a esta carpeta.

```text
add/
└── colegios-medellin.xlsx

```

## Comando Python

Información básica de Syntaxis en Python y empezamos con la asignación de una variable.
Con un `=` se define una variable tanto numérica como una cadena (cadena de texto o string). Además, se puede agignar una lista, un diccionario entre otros tipos de estructura de datos.

```python
x = "El resultado de (a+b)*c es: " # Esto es una variable.
a, b ,c = 4, 3, 2 # Esto es una asignación de variables múltiples.
d = (a + b) * c # Realizamos una operación y asginamod el resultado en otra variable.
print(x,d)

```

Como se puede observar, todos los comentarios inician con el `#`. Todo lo que es un comentario no se ejecuta por Python.
Otra forma de hacer comentarios es por medio del uso de comillas triples sencillas `'''` o dobles `"""`.

```python
'''
Esto es un bloque de 
comentario escrito en 
varias lineas de código.
'''

```

Dentro de las infinitas posibilidades para darle un nombre a una variable, Python tiene una serie de palabras reservadas que no se pueden usar para asignar variables. Para conocer las palabras puedes ejecutar el siguinte comando.

```python
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

```
## Flujos de Control

### Condicionales

Los condicionales son bloques de código que se ejecutan únicamente si se cumple una condición. 
El resultado de esta condición debe ser booleano (True o False).
Esto se logra mediante la sentencia **if**.
Con la sentencia **elif** se puede agregar un número arbitrario de condiciones. 
Por otra parte, se puede ejecutar código si la/s condición/es no se cumple/n con la sentencia **else**.


```python
>>> valor = 0
>>> if (valor < 0):
>>>     print('El número es negativo')
>>> elif (valor > 0):
>>>     print('El número es positivo')
>>> else:
>>>     print('El número es igual a cero')
El número es igual a cero
```

### Ciclos Iterativos o Loops

Son bloques de código que se repiten una cierta cantidad de veces en función de ciertas condiciones.

Un ciclo **for** repite un bloque de código tantas veces como elementos haya dentro del rango entre 1 y 10:

```python
>>> for n in range(1,10):
>>>     print(n)
1
2
3
4
5
6
7
8
9
```

Un ciclo **while** repite un bloque de código mientras que cierta condición se cumpla:

```python
>>> n = 1
>>> while (n < 10):
>>>     print(n)
>>>     n = n + 1
1
2
3
4
5
6
7
8
9
```

<hr width="75%">
  <p align="center">
  Hemos llegado hasta este punto y se repasaron algunos de los conceptos más fundamentales de la programación y de Python, pero es necesario detenerse en algunos detalles, que tienen que ver precisamente con el lenguaje que estamos utilizando:

  * En Python es importante la indentación, notar que el código que se ejecuta dentro de una sentencia if, for o while está indentado.
  * También es importante notar los ":"
  * En Python, cada vez que hagamos referencia a un rango, por ejemplo "1,10" el primer número se incluye y el último no.
  </p>
<hr width="75%">

### Sentencia Break

La sentencia break permite alterar el comportamiento de los bucles while y for. Concretamente, permite terminar con la ejecución del bucle. Esto significa que una vez se encuentra la palabra break, el bucle se habrá terminado.
Veamos cómo podemos usar el break con bucles for. El range(5) generaría 5 iteraciones, donde la i valdría de 0 a 4. Sin embargo, en la primera iteración, terminamos el bucle prematuramente.
El break hace que nada más empezar el bucle, se rompa y se salga sin haber hecho nada.

```python
>>> for i in range(5):
>>>   print(i)
>>>   break
0
```

Un ejemplo un poco más útil, sería el de buscar una letra en una palabra. Se itera toda la palabra y en el momento en el que se encuentra la letra que buscábamos, se rompe el bucle y se sale. Esto es algo muy útil porque si ya encontramos lo que estábamos buscando, no tendría mucho sentido seguir iterando la lista, ya que desperdiciaríamos recursos.

```python
>>> cadena = 'Python'
>>> for letra in cadena:
>>>     if letra == 'h':
>>>         print("Se encontró la h")
>>>         break
>>>     print(letra)
P
y
t
Se encontró la h
```

El break también nos permite alterar el comportamiento del while. En el ejemplo, la condición while True haría que la sección de código se ejecutará indefinidamente, pero al hacer uso del break, el bucle se romperá cuando x valga cero.

```python
>>> x = 5
>>> while True:
>>>     x -= 1
>>>     print(x)
>>>     if x == 0:
>>>         break
>>> print("Fin del bucle")
4
3
2
1
0
Fin del bucle
```

Por norma general, y salvo casos muy concretos, si ves un while True, es probable que haya un break dentro del bucle.

### Sentencia Continue

El uso de continue al igual que el ya visto break, permite modificar el comportamiento de de los bucles while y for.
Concretamente, la sentencia continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.
La diferencia con la sentencia break es que el continue no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.
En el siguiente ejemplo vemos como al encontrar la letra P se llama al continue, lo que hace que se salte el print(). Es por ello por lo que no vemos la letra P impresa en pantalla.

```python
>>> cadena = 'Python'
>>> for letra in cadena:
>>>     if letra == 'P':
>>>         continue
>>>     print(letra)
y
t
h
o
n
```

## Creación de entornos virtuales

El paquete que manipula y administra los entornos virtuales en _Linux_ es **venv**.
Comando para crear un entorno virtual desde la terminal de Linux (Ubuntu)
`$ python -m venv ruta/al/entorno/virtual`

Comando para activar el entorno virtual desde la terminal.
`$ source ruta/al/entorno/virtual/bin/activate`

Comando para desactivar el entorno virtual.
`$ deactivate`

Elimnar un entorno virtual.
`$ rm -rf ruta/al/entorno/virtual`

Lista de paquetes instalados.
`$ pip list`

Existe otro comando que lista los paquetes en formato del archivo _requirements.txt_. Este archivo contiene un listado de las versiones de los paquetes necesarios para ejecutar un proyecto en Python.
`$ pip freeze`

Si usamos macOS o Linux podemos guardar la salida directamente en un fichero de texto.
`$ pip freeze > requirements.txt`

## Comandos Github

Además, también hay que tener una lista de unos cuantos comandos de _github_ que debo recordar:

- `$ git config --global user.name` # Muestra el nombre del usuario asociado a la cuenta de Git
- `$ git config --global user.email` # Muestra el email asociado a la cuenta de Git
- `$ git remote show origin` # Muestra la rama remota (dirección web del repositorio).
- `$ git log --pretty="%cn committed %h on %cs"` # Muestra los commits realizados (la respuesta tiene formato).
- `$ git add archivo` # Adiciona archivo al rastreo de git.
- `$ git add *` # Adiciona todos los archivos al rastreo de git.
- `$ git pull` # Extrae información de la rama (actualiza la rama).
- `$ git branch nueva_rama` # Crear nueva rama.
- `$ git checkout nueva_rama` # Cambiar de ramas.
- `$ git checkout -b nueva_rama` # Crear rama nueva y cambiar al mismo tiempo.

El archivo _.gitignore_ especifica archivos y directorios sin seguimiento intencional.

El siguiente enlace tiene toda la información sobre la configuración de los repositorios remotos en github.
[Info a repositorios remotos en Github](https://docs.github.com/es/get-started/getting-started-with-git/managing-remote-repositories)