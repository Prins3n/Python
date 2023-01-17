# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 20:17:38 2021

@author: Anders
"""

"""
ag en funksjon som tar inn antall ganger en skal trille en terning. 
Funksjonen skal skrive ut summen av alle kastene til terningen. 
For å få et tilfeldig tall fra 1 til 6 
kan enbruke følgende kode:import randomrandom.randint(1,6)
"""

import random

def tall():
	return random.randint(1, 6)

antall_kast = int(input("Fortell meg hvor mange ganger terningen skal kastes: "))
		
def terning_kast(antall):
	total = 0
	oyne = []
	for i in range(antall):
		kast = tall()
		oyne.append(kast)
		total += kast
		print(oyne)
	return total

print(f"du har valgt å kaste terningen {antall_kast} ganger og totalsummen ble: {terning_kast(antall_kast)}")

		
		
		
		
		
	
