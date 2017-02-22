#!/usr/bin/env python
# -*- coding: utf-8 -*
A = input("Escriba un año para saber si es bisiesto: ")

def si_bisiesto(A):

    if A % 4 == 0 and (not(A % 100 == 0)):
        print "El año", A, "es un año bisiesto"
    elif A % 400 == 0:
        print "El año", A, "es un año bisiesto"
    else:
        print "El año", A, "no es bisiesto"

print si_bisiesto(A)



