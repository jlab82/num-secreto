#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
num_secreto = random.randint(1, 10)
x = int(raw_input("Adivina el número secreto del 1 al 10, tienes una oportunidad para ganar 300 bitcoin: "))
while True:
    if x > num_secreto:
        print "El número secreto es menor que {}" .format(x)
        x = int(raw_input("Introduzca otro número: "))
    elif x < num_secreto:
        print "El número secreto es mayor que {}" .format(x)
        x = int(raw_input("Introduzca otro número: "))
    else:
        print "Enhorabuena, {} es el número secreto!" .format(x)
        break
