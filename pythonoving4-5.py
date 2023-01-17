# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:54:41 2021

@author: Anders
"""

def tall_til_karakter():
	karakter = int(input("Skriv karakter her: "))
	if karakter == 5:
		return("Karakteren er lik A")
	if karakter == 4:
		return("Karakter er lik B")
	if karakter == 3:
		return("Karakter er lik C")
	if karakter == 2:
		return("Karakter er lik D")
	if karakter == 1:
		return("Karakter er lik E")
	if karakter == 0:
		return("Karakter er lik F")
	else:
		return("Ugyldig karakter")

#print(tall_til_karakter())

def studentnummer():
	student = int(input("Skriv inn et studentnr, så vil det tilsvarende navnet bli gitt: "))
	if student == 1:
		return ("Ola Nordmann")
	if student == 2:
		return ("Kari Nordmann")
	else:
		return ("Ugyldig studentnummer")

#print(studentnummer())
		
def karakter_til_student():
	kombiner = (print(f"{studentnummer()} fikk karakter {tall_til_karakter()}"))
	return kombiner

print(karakter_til_student())


