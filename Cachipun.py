import random
opciones=["piedra","papel","tijera"]
print("¡Bienvenidxs al CACHIPÚN!")

while True:
    jugador=input("Elige: piedra, papel o tijera: ").lower()
    if jugador not in opciones:
        print("Opción no válida, intente nuevamente")
        continue
    computador=random.choice(opciones)
    print(f"El computador eligió: {computador}")
    if jugador==computador:
        print("¡EMPATE!")
    elif (jugador=="piedra" and computador=="tijera") or (jugador=="papel" and computador=="piedra") or (jugador=="tijera" and computador=="papel"):
        print("¡GANASTE!")
    else:
        print("¡PERDISTE!")
    

    continuar=input("¿Quieres seguir jugando? (si/no): ").lower()
    if continuar != "si":
        print("Gracias por jugar CACHIPÚN (L)")
        break
