x = int(input("Ingrese el primer numero: "))
y = int(input("Ingrese el segundo numero: "))
z = int(input("Ingrese el tercer numero: "))

if x>y and x>z:
    print "el numero mayor es:", x
elif y>x and y>z:
            print "el numero mayor es:", y
elif z>x and z>y:
            print "el numero mayor es:", z
else:
    print "los numeros son iguales"