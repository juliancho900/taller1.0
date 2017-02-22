numero= int(input("Introduce un numero Min.1-Max.100000): "))
if(numero < 0 or numero > 100000 ):
    print "numero fuera de rango"
else:
    num=str(numero)
    cantidad=0;
    for i in num:
        cantidad=cantidad+1
    print ("la cantidad de digitos es:")
    print cantidad
