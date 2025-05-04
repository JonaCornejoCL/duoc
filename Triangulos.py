l1=float(input("ESCRIBA EL LADO 1: "))
l2=float(input("ESCRIBA EL LADO 2: "))
l3=float(input("ESCRIBA EL LADO 3: "))
if l1>=l2+l3 or l2>=l3+l1 or l3>=l2+l1:
    print("EL TRIANGULO NO ES VALIDO")
elif l1==l2 or l2==l3 or l1==l3:
    print("ES UN TRIANGULO ISOCELES")
elif l1!=l2 and l2!=l3 and l1!=l3:
    print("EL TRIANGULO ES ESCALENO")
else:
    print("ALGO ESTA MAL")
