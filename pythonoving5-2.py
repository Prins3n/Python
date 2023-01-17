# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Oppgav 2

"""
Brukfunksjonenfraoppgave1oglageilistemedselvvalgtlengde.Summeralletallen.

"""
import random

#funksjon som skal ta imot et argument
def get_lengde(lengde):
    #lager vi en liste som skal ta imot tall.
    tall_liste = [] #variabelnavn med en liste som variabelverdi
    for tall in range(lengde): #forloop
        tall = random.randint(1, 10)
        tall_liste.append(tall) #append funksjonen legger til et element i en liste.
    
    return tall_liste #returnerer listen til print utsagnet lenger nede.


print(sum(get_lengde(8))) #bruker sum funskjonen til å summere listen