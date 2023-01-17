# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:17:02 2021

@author: Anders
"""

"""
Nora ønsker å lage en funksjon der brukeren kan skrive inn tilfeldige tall,
 men tallene blir kun gyldige dersom de er fra 1 til 6. 
 Det vil si, brukeren skriver inn et tall, dersom tallet er gyldig, 
 får brukeren skrive inn et tall til. 
 For å få input fra brukeren så kan en bruke input()-funksjonen. 
 Slik fortsetter det helt til brukeren skriver inn et ugyldig tall. 
 Kod løsningen. 

"""
number = int(input("Tast inn et tall: "))

def valid_input(number):
  if number < 7 and number > 0:
    return True
  return False


while valid_input(number):
	if True:
		print("Fint tall, nå kan du gjør det igjen: ")
		number = input("Tast inn et tall: ")
	else:
		print("det var feil")

