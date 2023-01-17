# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:33:04 2021

@author: Anders
"""

#Oppgave 2

condition = 99

while condition > 0:
	print(f"{condition} bottles of beer on the wall, {condition} bottles of beer, take one down pass it around, {condition -1} bottles of beer on the wall")
	condition -= 1
	if condition == 0:
		print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall...")
		
"""
slet lenge med oppgaven, forstod ikke hvordan jeg kunne skrive variabelen og få den til å forandre seg. 
Sjekket ut en del videoer angående for og while loops, så prøvde jeg å skrive en loop og det gikk egentlig ganske bra

"""
