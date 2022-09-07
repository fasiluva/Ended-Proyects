from random import randrange, choice
from time import sleep

"""
TODO: Corregir error de que pueden salir 2 cartas iguales
TODO: Añadir la posiblidad de dividir las cartas si son iguales
TODO: Añadir mas jugadores a la mesa (bots)
TODO: Usar la libreria time y la funcion sleep para hacer turnos mas realistas
"""

#* Variables que se utilizaran en todas las funciones (o la mayoria):
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
sueldo = 1000 
sumaJugador = 0 
sumaCrupier = 0
opciones = "\n1- Pedir \n2- Doblar \n3- Retirarse"
apuesta = 0

def randomCard(calledBy, excludedCards):
    """ Asigna una nueva carta. El parametro calledBy indica a quien se le atribuye
    dicha carta """

    #? Creacion de carta y palo aleatorio:
    cartaRange = randrange(1, 13) 
    palo = choice(['picas', 'corazones', 'trebol', 'diamantes'])

    #? Chequeo de no repeticion de carta, indicada con los elementos de excludedCards:
    for [paloE, numero] in excludedCards:
        if paloE == palo and numero == cartaRange:
            palo = choice(['picas', 'corazones', 'trebol', 'diamantes'])
            cartaRange = randrange(1, 13)
    
    carta = cards[cartaRange]

    #? Asignacion de cuenta por jugador de partida:
    if calledBy == "jugador":
        global sumaJugador
        if type(carta) == str:
            sumaJugador += 10
        else: 
            sumaJugador += carta
    if calledBy == "crupier":
        global sumaCrupier
        if type(carta) == str:
            sumaCrupier += 10
        else: 
            sumaCrupier += carta

    #? Añade la carta agregada a la lista de cartas excluidas:
    excludedCards.append([palo, carta])    
    return [palo, carta]

def newCardMg_jugador(numero, palo):
    """ Mensaje predeterminado cuando el jugador pide una carta nueva """
    print(f"Se le da otra carta. Ha recibido un {numero} de {palo}.")

def newCardMg_crupier(numero, palo):
    """ Mensaje predeterminado cuando el crupier pide una carta nueva """
    print(f"El crupier se da otra carta. Ha recibido un {numero} de {palo}.")

def fase1():
    """ Funcion que inicia el juego, permitiendo seleccionar la apuesta, si el valor es valido. """

    try:
        global apuesta
        apuesta = int(input("Seleccione su apuesta: "))
    except:
        fase1()
    else:
        pass # Repite hasta que se de un valor valido

def fase2():
    #? Declaracion de lista con cartas excluidas:
    excludedCards = []

    #? Primer reparto de cartas al jugador:
    jugador = [randomCard('jugador', excludedCards)] # Primera carta
    jugador.append(randomCard('jugador', excludedCards)) # Segunda carta

    #? Primer reparto de cartas al crupier:
    crupier = [randomCard('crupier', excludedCards)] # Primera carta
    crupier.append(randomCard('crupier', excludedCards)) # Segunda carta

    #? Visualizacion de sus primeras 2 cartas:
    print(f"Usted tiene un {jugador[0][1]} de {jugador[0][0]} y un {jugador[1][1]} de {jugador[1][0]}")
    
    eleccion = 0
    #? Ciclo de reparto de cartas, hasta que se pierda o se retire y sea turno del crupier:
    while sumaJugador < 21 and eleccion != 3:
        print(opciones)
        eleccion = int(input())

        if eleccion == 1:
            #? Nueva carta y visualizacion de la misma:
            jugador.append(randomCard('jugador', excludedCards))
            newCardMg_jugador(jugador[-1][1], jugador[-1][0])

        if eleccion == 2:
            global apuesta
            #? Nueva carta, visualizacion de la misma y duplicado de la apuesta. Cambio de turno automatico:
            jugador.append(randomCard('jugador', excludedCards))
            newCardMg_jugador(jugador[-1][1], jugador[-1][0])
            apuesta *= 2
            eleccion = 3

        if eleccion == 3:
            #? Inicio del turno del crupier. Visualizacion de sus cartas:
            print(f"El crupier a revelado un {crupier[0][1]} de {crupier[0][0]} y un {crupier[1][1]} de {crupier[1][0]}")
            
            #? Si el crupier tiene menos de 17, añade mas cartas, hasta que se pueda plantar en 17 o mas:
            while sumaCrupier < 17:
                #? Nueva carta y visualizacion de la misma:
                crupier.append(randomCard('crupier', excludedCards))
                newCardMg_crupier(crupier[-1][1], crupier[-1][0])

    #? Determina el desenlace de la partida:
    if (sumaCrupier > 21) or (sumaJugador > sumaCrupier and sumaJugador <= 21):
        winnerLosser = f'ganado {apuesta}!. Ahora tiene {sueldo + apuesta}'
    if (sumaJugador > 21) or (sumaJugador < sumaCrupier and sumaCrupier <= 21):
        winnerLosser = f'perdido {apuesta}!. Ahora tiene {sueldo - apuesta}'
    if sumaJugador == sumaCrupier:
        winnerLosser = f'empatado. No gana ni pierde nada. Tiene {sueldo}'

    #? Muestra el desenlace de la partida:
    puntaje = f"Usted tiene {sumaJugador} y el crupier {sumaCrupier}. Ha"
    print(puntaje, winnerLosser)

def juego():
    """ Funcion que da inicio al juego. """
    fase1()
    print("Las cartas se reparten...")
    fase2()

juego()

"""
#! Manejo de errores (poner global jugador y global crupier en fase2):
print("\nCartas del jugador", jugador)
print("Suma del jugador", sumaJugador)
print("Cartas del crupier", crupier)
print("Suma del crupier", sumaCrupier)

* Ejemplo de jugador == [['trebol', 5], ['corazones', 'J']]  == list(list(String, Number|String), list(String, Number|String))
"""