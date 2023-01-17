# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:17:46 2021

@author: Anders
"""

#OPPGAVE 1

#Skriv ut (vha. løkke) alle tall fra 1 til 15, bortsett fra 4 og 9.

for x in range(16):
	if x == 4:
		continue
	if x == 9:
		continue
	print (x)

"""
Slet litt med denne, forstod ikke hva jeg hadde gjort feil i og med at
programmet skrev kun ut siste tallet, som her ble 15. Problemet viste seg å 
være at jeg hadde glemt å identitere print statementen
"""
