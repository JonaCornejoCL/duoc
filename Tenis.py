ja=int(input("INGRESE JUEGOS GANADOS POR JUGADOR A: "))
jb=int(input("INGRESE JUEGOS GANADOS POR JUGADOR B: "))
if (ja==6 and jb<=4) or (ja==7 and (jb==5 or jb==6)):
    print("JUGADOR A GANA")
elif (jb==6 and ja<=4) or (jb==7 and (ja==5 or ja==6)):
    print("JUGADOR B GANA")
elif (ja==6 and jb==6) or (ja<=6 and jb<=6):
    print("EL JUEGO AUN NO TERMINA")
else:
    print("INVÁLIDO")
