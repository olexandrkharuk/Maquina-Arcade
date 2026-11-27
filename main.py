
from jocs import janken, nana

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1. Joc 1 - Pedra, paper o tisora")
    print("2. Joc 2 - Endevina el número")
    print("3. Sortir")

    opcio = input("Tria una opció: ")

    if opcio == "1":
        janken()
    elif opcio == "2":
        nana()
    elif opcio == "3":
        print("Fins aviat!")
        break
    else:
        print("Opció incorrecta. Torna-ho a provar.")
