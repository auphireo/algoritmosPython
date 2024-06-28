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
├── bucle_while_01.py
├── bucle_while_02.py
├── Excepciones.py
├── juego_triqui_v0.1.0.py
└── mapa-colegios.py

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