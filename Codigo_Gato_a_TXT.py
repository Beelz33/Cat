datos = """import random

def imprimir_tablero(tablero):
    for fila in tablero: #fila(listas del tablero)
        for i in range(len(fila)): #I es cada elemento de la fila 
            if i == len(fila)-1:
                print(fila[i], end="\n")
            else:
                print(fila[i], end="  ")

def cambiar_tablero(tablero, posicion, jugador): #Estado del tablero, posicion de jugada y de quien es el turno
    if jugador:
        simbolo = "x"
    else:
        simbolo = "o"
    
    if posicion == 1:
        if tablero[4][0] == " ":  #Con esto se elige la ultima lista y la columna que quiera elegir el jugador
            tablero[4][0] = simbolo  # Corrección aquí, debe ser "=" en lugar de "=="
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 2:
        if tablero[4][2] == " ":   
            tablero[4][2] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 3:
        if tablero[4][4] == " ":   
            tablero[4][4] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 4:
        if tablero[2][0] == " ":   
            tablero[2][0] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 5:
        if tablero[2][2] == " ":   
            tablero[2][2] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 6:
        if tablero[2][4] == " ":   
            tablero[2][4] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 7:
        if tablero[0][0] == " ":   
            tablero[0][0] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 8:
        if tablero[0][2] == " ":   
            tablero[0][2] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    elif posicion == 9:
        if tablero[0][4] == " ":   
            tablero[0][4] = simbolo
            return 0
        else:
            return "Esta posicion ya esta ocupada."
    else:
        return "esa posicion no existe."

def ganador(tablero):
    for simbolo in ["x","o"]:
        fila0 = tablero[0][0] == simbolo and tablero[0][2] == simbolo and tablero [0][4] == simbolo
        fila2 = tablero[2][0] == simbolo and tablero[2][2] == simbolo and tablero [2][4] == simbolo
        fila4 = tablero[4][0] == simbolo and tablero[4][2] == simbolo and tablero [4][4] == simbolo
        columna0 = tablero[0][0] == simbolo and tablero[2][0] == simbolo and tablero [4][0] == simbolo
        columna2 = tablero[0][2] == simbolo and tablero[2][2] == simbolo and tablero [4][2] == simbolo
        columna4 = tablero[4][0] == simbolo and tablero[2][4] == simbolo and tablero [4][4] == simbolo
        diagonal_arriba = tablero[0][0] == simbolo and tablero[2][2] == simbolo and tablero [4][4] == simbolo
        diagonal_abajo = tablero[4][0] == simbolo and tablero[2][2] == simbolo and tablero [0][4] == simbolo
        
        if fila0 or fila2 or fila4 or columna0 or columna2 or columna4 or diagonal_arriba or diagonal_abajo:
            if simbolo == "x":
                return 1
            elif simbolo == "o":
                return 2
            break

def nueva_partida():
    global tablero
    tablero = [
        [" ","|"," ","|"," "],
        ["-------------"],
        [" ","|"," ","|"," "],
        ["-------------"],
        [" ","|"," ","|"," "]
    ]
    return tablero

def jugador_vs_com():
    nueva_partida()
    jugador = input("Nombre del jugador (x): ")
    print("Bienvenido", jugador, "! Eres el jugador (x).")
    while True:
        print("Tu turno, elige la posición del tablero (1-9): ")
        jugada = int(input())
        valor = cambiar_tablero(tablero, jugada, True)
        if valor == 0:
            imprimir_tablero(tablero)
            if ganador(tablero) == 1:
                print("¡Felicidades,", jugador, "has ganado!")
                break
            elif ganador(tablero) == 2:
                print("¡Lo siento,", jugador, "has perdido!")
                break
            else:
                print("Turno de la computadora.")
                # Lógica de la jugada de la computadora
                jugada_computadora = random.randint(1, 9)
                valor_computadora = cambiar_tablero(tablero, jugada_computadora, False)
                if valor_computadora == 0:
                    imprimir_tablero(tablero)
                    if ganador(tablero) == 1:
                        print("¡Felicidades,", jugador, "has ganado!")
                        break
                    elif ganador(tablero) == 2:
                        print("¡La computadora ha ganado!")
                        break
        else:
            print(valor)

def versus():
    nueva_partida()
    jugador1 = input("Nombre del jugador 1 (x): ")
    jugador2 = input("Nombre del jugador 2 (o): ")
    print("Bienvenidos,", jugador1, "y", jugador2 + "!")
    turno1 = True
    turno = 0
    while turno < 9:
        if turno1:
            print(jugador1 + ", elige la posición del tablero.")
        else:
            print(jugador2 + ", elige la posición del tablero.")
        
        jugada = int(input())

        valor = cambiar_tablero(tablero, jugada, turno1)
        if valor == 0:
            turno1 = not turno1
            turno += 1 
            imprimir_tablero(tablero)
            if ganador(tablero) == 1:
                print(jugador1 + "Ganaste crack.")
                break
            elif ganador(tablero) == 2:
                print(jugador2 + "Ganaste crack.")
                break
        else:
            print(valor)
    
        if turno == 9:
            print ("empate")    

def menu():
    while True:
        print("\nMENU")
        print("i. Nueva partida (Player 1 VS COM)")
        print("ii. Versus (P1 VS P2)")
        print("iii. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "i":
            jugador_vs_com()
        elif opcion == "ii":
            versus()
        elif opcion == "iii":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor selecciona de nuevo.")

menu()
"""
with open('Gato1.txt', 'w') as archivo:
    archivo.write(datos)
