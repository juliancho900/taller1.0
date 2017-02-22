
numero = int(raw_input("Ingrese un numero\n"))
binario = ""
if (numero > 0):
    while(numero > 0):
        if (numero%2 == 0):
            binario = "0" + binario
        else:
            binario = "1" + binario
        numero = int(numero/2)
else:
    if (numero == 0):
        binario = "0"
    else:
        binario = "No se pude convertir el numero"
print("El resultado es: "+binario)
raw_input()