d=float(input("INGRESE DISTANCIA: "))
a=float(input("INGRESE ANGULO: "))
if d<=7 and a<360:
    print("CAE EN LA PILETA") 
elif d>7 and d<=47 and a>45 and a<90:
    print("CAE EN EL PÚBLICO")
elif d>=20 and d<=35 and ((a>=90 and a<=135) or (a>=0 and a<=45 ) or (a>=270 and a<=315) or (a>=180 and a<=225)):
    print("CAE EN UN ÁREA VERDE")
elif (d>35 and d<=47 and (a<=45 or a>=90)) or (d>7 and d<20 and (a<=45 or a>=90)) or (d>=20 and d<=35 and ((a>135 and a<180) or (a>225 and a<270) or (a>315 and a<360))):
    print("CAE EN EL CEMENTO (RIP)")
elif (d>47):
    print("CAE FUERA DE LA PLAZA")
else:
    print("VALOR ERRÓNEO")