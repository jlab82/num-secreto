#!/usr/bin/env python
# -*- coding: utf-8 -*-
# mi número secreto es 9
num_secreto = 9
x = raw_input("Adivina el número secreto, tienes una oportunidad: ")
x = int(x)
print "Tu número seleccionado ha sido:"
print x

if x == num_secreto:
    print "Enhorabuena, has adivinado el número secreto"
else:
    print "Lo sentimos, el número es incorrecto"

