# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 10:59:31 2021

@author: Anders
"""

from random import randint
number = randint(1, 100)
forsøk = 1

gjett = int(input("Gjett et tall mellom 1 og 99: "))

while gjett != number:
	if gjett > number:
		print("ahh, det va for høyt ")
		gjett = int(input("gjett igjen buddy: "))
		forsøk = forsøk + 1
	elif gjett < number:
		print("det va for lavt")
		gjett = int(input("prøv igjen: "))
		forsøk = forsøk + 1
	
print ()
print ("ja det va", number,)
print("og det tok deg bare", forsøk, "forsøk!")

	