#!/usr/bin/env python
# -*- coding: utf-8 -*-
palabra=raw_input("Ingrese Palabra: ")
c_mayusculas="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
cont=0
for i in palabra:
     if i in c_mayusculas:
       cont=cont+1
print cont

print "La palabra tiene", cont, "mayusculas"