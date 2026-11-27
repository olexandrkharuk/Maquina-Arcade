import random
from robot import jugada_robot


def janken():
    print("\n--- JOC DE PEDRA, PAPER O TISORA ---")
    print("1. Primer a 3 victòries")
    print("2. Millor de 5 rondes")

    while True:
        mode = input("Tria una opció: ")

        if mode == "1":
            objectiu = 3
            break
        elif mode == "2":
            objectiu = 3
            break
        else:
            print("Opció incorrecta. Torna-ho a provar.")

    punts_jugador = 0
    punts_robot = 0

    while punts_jugador < objectiu and punts_robot < objectiu:
        jugador = input("\nTria pedra, paper o tisora: ").lower()

        if jugador not in ["pedra", "paper", "tisora"]:
            print("Opció incorrecta!")
            continue

        robot = jugada_robot()
        print("El robot ha triat:", robot)

        if jugador == robot:
            print("Empat!")
        elif (
            (jugador == "pedra" and robot == "tisora")
            or (jugador == "paper" and robot == "pedra")
            or (jugador == "tisora" and robot == "paper")
        ):
            print("Has guanyat aquesta ronda!")
            punts_jugador += 1
        else:
            print("El robot ha guanyat aquesta ronda!")
            punts_robot += 1

        print("Jugador:", punts_jugador, "- Robot:", punts_robot)

    if punts_jugador == objectiu:
        print("\nHas guanyat la partida!")
    else:
        print("\nEl robot ha guanyat la partida!")


def nana():
    print("\n--- ENDEVINA EL NÚMERO ---")
    numero_secret = random.randint(1, 100)
    intents = 0

    while True:
        resposta = input("Escriu un número entre 1 i 100: ")

        if not resposta.isdigit():
            print("Has d'escriure un número!")
            continue

        numero = int(resposta)
        intents += 1

        if numero < numero_secret:
            print("El número secret és més gran.")
        elif numero > numero_secret:
            print("El número secret és més petit.")
        else:
            print("Correcte! Has encertat el número!")
            print("Nombre d'intents:", intents)
            break
