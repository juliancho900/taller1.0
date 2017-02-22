vocal = raw_input("Ingrese letra:")
def evalue(letra):
    vocales = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

    if letra in vocales:
       return True
    else:
        return False
print evalue(vocal)