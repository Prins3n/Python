# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Oppgav 4

"""
Brukfunksjonenfraoppgave1oglageilistemedselvvalgtlengde.Finnmaksimimumsverdi.

"""
import random

#funksjon som skal ta imot et argument
def get_lengde(lengde):
    #lager vi en liste som skal ta imot tall.
    tall_liste1 = [] #variabelnavn med en liste som variabelverdi
    for tall in range(lengde): #forloop
        tall = random.randint(1, 10)
        tall_liste1.append(tall) #append funksjonen legger til et element i en liste.
       
    
    return tall_liste1 #returnerer listen til print utsagnet lenger nede.


print(max(get_lengde(8)))