# juego de TA - TE - TI o "Triqui" como lo conozco yo
# Este juego es una prueba de un curso en linea que estoy haciendo
# Hecho por @auphireo

# Matriz base del tablero de juego.
# la variable @matriz es la base de la varible @tablero en blanco
# que será el inicio de la partida de este juego. @matriz no se modifica.
matriz = [
    ['|_|','|_|','|_|'],
    ['|_|','|_|','|_|'],
    ['|_|','|_|','|_|']
]
# Variables locales que se modifican dentro de alugnas funciones.
jugada=[]
marca=[]
jugadores={}
jugada_turno=[]
cambio = []

# Funcion que escribe la presentación del juego
def presentacion():
    print('*'*50)
    print('Presentación del tablero de Ta - Te - Ti.\n')
    print('El siguiente es un pequño juego de tres en\n')
    print('linea. Conocido tambíen como "Triqui". \n')

    print('*'*50)

# Las condiciones del algoritmos es que, el jugador que juegue con las "X"
# debe jugar de primero. 
def reglas():
    print('\nEl juego consiste en marcar en un tablero de 3x3')
    print('una "X" y un "O". El juego es para dos jugadores.')
    print('Se hace una marca por turno.')
    print('\nJugadores. Quien escoja "X" inicia el juego.')
    marca = input('¿Quien va primero? Escoje tu marca "X" u "O"? ')
    if marca == 'o':
        marca = marca.upper() # si la letra es minúscula, se pasa a mayúscula
    if marca == 'x':
        marca = marca.upper() # si la letra es minúscula, se pasa a mayúscula
    return marca

# Se imprime el tablero de juego. 
# @tablero es una copia de @matriz.
# Condición inicial de la partida. 
def imprime_tablero(tablero):
    m=""
    print(' \tcol 1\tcol 2\tcol 3')
    for j in range(3):
        for k in range(3):
            m+= str(tablero[j][k]+'\t')
        print('fila ' + str(j+1) + '  ' + m)
        m=""

# Recibe las coordenadas (fila, columna) para realizar la jugada del turno.
def hacer_jugada(turno):
    Fila=int(input('Jugador '+ turno +', haz tu jugada, escoje fila? '))
    Col=int(input('Ahora escoje columna? '))
    jugada = [Fila,Col]
    
    return jugada

# Hace el cambio de jugador para el turno (de 'O' a 'X') 
def le_toca_a_x(marca):
    global turno_x
    
    if marca == 'O':
        turno_x = 'X'
    
    else:
        turno_x = 'X'
   
    return turno_x

# Hace el cambio de jugador para el turno (de 'X' a 'O') 
def le_toca_a_o(marca):
    global turno_o
    
    if marca == 'X':
        turno_o = 'O'

    else:
        turno_o = 'O'

    return turno_o

# Parametriza las coordenadas de (1 a 3) a (0 - 2) para posicionar correctamente 
# en la matriz @partida 
def marcar_jugada(jugada, turno):
    if turno == 'X':
        partida[jugada[0]-1][jugada[1]-1]='|X|' # marca en la partida la jugada
    if turno == 'O':
        partida[jugada[0]-1][jugada[1]-1]='|O|' # marca en la partida la jugada

# Condición del algoritmo, solicitar a uno de los jugadores escoger
# su marca de juego en el tablero. Las 'X' juegan de primero.
def solicita_marca(intentos=3):
    while True:
        marca = reglas()
        if marca not in ('X','O'):
            print('Escoge X si quieres jugar de primero')
            intentos -= 1

        if intentos < 0:
            raise ValueError("Estas como aburrido. Intentalo mas tarde")
            
        if marca in ('X','O'):
            break

# Todas las condiciones en las que se puede ganar el juego. (8 en total)

def evalua_juego(tablero,turno):
    
    jugador = '|'+turno+'|'

    # verifica diagonal
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        print('gano jugador ',jugador,'...!')
        print('Fin del juego.')
        exit()
    # verifica diagonal        
    if tablero[2][0] == jugador and tablero[1][1] == jugador and tablero[0][2] == jugador:
        print('gano jugador ',jugador,'...!')
        print('Fin del juego.')
        exit()


    for j in range(len(tablero)):
        # verifica verticales
        if tablero[0][j] == jugador and tablero[1][j] == jugador and tablero[2][j] == jugador:
            print('gano jugador ',jugador,'...!')
            print('Fin del juego.')
            exit()

        # verifica horizontales    
        if tablero[j][0] == jugador and tablero[j][1] == jugador and tablero[j][2] == jugador:
            print('gano jugador ',jugador,'...!')
            print('Fin del juego.')
            exit()
            
           
#  +-------------------------------------+
#  | Inicio del juego para los usuarios  |
#  +-------------------------------------+

presentacion() # presentanción del juego
imprime_tablero(matriz) # condiciones iniciales ( tablero en blanco )
partida = matriz # crea una copia del tablero e inicia partida

solicita_marca()
turno = str(le_toca_a_x(marca)) # pone a @turno el valor de 'X' 
print('\nEl juego comienza realizando una marca')
print('seleccionando primero la fila y luego la')
print('columna donde se pondrá la marca.')
print('El juego pregunta primero el número de fila,')
print('luego el de la columna.')
jugada = hacer_jugada(turno) # escribe las reglas, pide las coordenadas y las entrega
marcar_jugada(jugada,turno) # recibe las coordenadas de la jugada y el turno 
imprime_tablero(partida) # muestra la primera jugada 

#######
num_jugadas = 8
turnos = 0

while turnos < num_jugadas:
    if turnos%2 == 0:
        turno= le_toca_a_o(marca) # pone a @turno el valor de 'O' 
        while True:
            # Verifica que la posición no se halla jugado
            jugada = hacer_jugada(turno)
            if partida[jugada[0]-1][jugada[1]-1] in ('|X|','|O|'):
                print('la posición ya se jugo')
            else: 
                break

        marcar_jugada(jugada,turno) # recibe las coordenadas de la jugada y el turno 
        imprime_tablero(partida) # Imprime la jugada 
        turnos += 1 # Cuenta las jugadas y funciona como "switch" para cambiar de jugador
        evalua_juego(partida,turno)
        print('van ',turnos+1, 'jugadas\n')

    if turnos%2 != 0:
        turno = le_toca_a_x(marca) # pone a @turno el valor de 'X' 
        while True:
            # Verifica que la posición no se halla jugado
            jugada = hacer_jugada(turno)
            if partida[jugada[0]-1][jugada[1]-1] in ('|X|','|O|'):
                print('la posición ya se jugo')
            else: 
                break

        marcar_jugada(jugada,turno) # recibe las coordenadas de la jugada y el turno 
        imprime_tablero(partida) # Imprime la jugada 
        turnos += 1 # Cuenta las jugadas y funciona como "switch" para cambiar de jugador
        evalua_juego(partida,turno)
        print('van ',turnos+1, 'jugadas\n')

# Si el juego no termina por las condiciones donde habría un ganador
# quiere decir que termina empatado.
print('El juego queda Empado. \nFin de la partida...!')
imprime_tablero(partida) # muestra la primera jugada

