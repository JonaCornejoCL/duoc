fa=int(input("ESCRIBA LA FILA DEL ALFIL: "))
ca=int(input ("ESCRIBA LA COLUMNA DEL ALFIL: "))
ft=int(input("ESCRIBA LA FILA DE LA TORRE: "))
ct=int(input("ESCRIBA LA COLUMNA DE LA TORRE: "))
if abs(fa-ft)==abs(ca-ct):
    print("ALFIL CAPTURA")
elif fa==ft or ca==ct:
    print("TORRE CAPTURA")
else:
    print("NO SE TOCAN")
