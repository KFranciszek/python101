#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random

ileliczb = int(raw_input("Podaj ilość typowanych liczb: "))
maksliczba = int(raw_input("Podaj maksymalną losowaną liczbę: "))
# print "Wytypuj %s z %s liczb: " % (ileliczb, maksliczba)

liczby = []
for i in range(ileliczb):
    liczba = random.randint(1, maksliczba)
    liczby.append(liczba)

print "Wylosowane liczby:", liczby
