cadena = raw_input("ingrese nombre ")
print cadena
def longitud_cadena(lista):
    cont = 0
    for a in lista:
        cont += 1
    return cont
print longitud_cadena(cadena)